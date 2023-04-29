# Copyright 2023 by Liraal2
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the Evil GPL License as published by
# Liraal. You should have received a copy of the
# Evil GPL License along with this program.

#╭─────────────────────────────────────────────╮
#│ │          IMPORT LIBRARIES               │ │
#╰─────────────────────────────────────────────╯

import os
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPainter, QBrush
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QCheckBox, QFileDialog

from config import Config
from file_processor import FileProcessor

#╭─────────────────────────────────────────────╮
#│ │                GUI CODE                 │ │
#╰─────────────────────────────────────────────╯

class ProgeatApp(QWidget):
    """
    Main app class, handles UI processing
    """
    def __init__(self):
        super().__init__()
        
        self.config = config
        self.file_processor = file_processor

        # Set the window title
        self.setWindowTitle('Progeat-v2.0')
        # Set the window geometry
        self.setGeometry(300, 300, 600, 500)
        
        #create fonts
        labelFont = QFont()
        labelFont.setBold(True)
        titleFont = QFont()
        titleFont.setPointSize(18)
        # Title Label
        titleLabel = QLabel('Progeat v2.0', self)
        titleLabel.setFont(titleFont)
        titleLabel.move(200, 40)
        # Filepath label + field
        pathLabel = QLabel('Filepath:', self)
        pathLabel.move(10, 183)
        pathLabel.setFont(labelFont)
        self.pathField = QLineEdit(self)
        self.pathField.move(180, 180)
        self.pathField.setFixedWidth(400)
        # Filename label + field
        nameLabel = QLabel('Override filename:', self)
        nameLabel.move(10, 223)
        nameLabel.setFont(labelFont)
        self.nameField = QLineEdit(self)
        self.nameField.move(180, 220)
        self.nameField.setFixedWidth(400)
        # Override label + field
        overrideLabel = QLabel('Override [0 1]:', self)
        overrideLabel.move(10, 263)
        overrideLabel.setFont(labelFont)
        self.overrideField = QLineEdit(self)
        self.overrideField.setText("0 1")
        self.overrideField.move(180, 260)
        self.overrideField.setFixedWidth(400)
        # Avogadro checkbox
        cb = QCheckBox('Use Avogadro?', self)
        cb.move(10, 300)
        cb.toggle() # Set checkbox to checked by default
        cb.stateChanged.connect(self.changeTitle)
        # Create a button widget
        button = QPushButton('RUN', self)
        button.move(10, 340)
        button.setFixedSize(580, 60)
        button.setFont(labelFont)
        button.clicked.connect(self.on_button_click)
        # Done Label
        self.doneLabel = QLabel('...', self)
        self.doneLabel.setFont(titleFont)
        self.doneLabel.setFixedWidth(400)
        self.doneLabel.move(40, 410)

    def on_button_click(self):
        """
        Handles user clicking on run button
        """
        path = self.pathField.text()
        if not path:
            dialog = QFileDialog()
            dialog.setFileMode(QFileDialog.AnyFile)
            dialog.setNameFilter('Cml files (*.cml)')
            dialog.setOption(QFileDialog.DontUseNativeDialog, True)
            if dialog.exec_():
                path = dialog.selectedFiles()[0]
            else: 
                return
            self.pathField.setText(path)
        filename = self.nameField.text() if self.nameField.text() else None
        self.file_processor.processFile(path, self.overrideField.text(), filename)
        self.doneLabel.setText("F|{0}|Complete".format(os.path.basename(path)))
        
    def changeTitle(self, state):
        """
        Handles user interacting with checkbox
        """
        self.config.set('use_avogadro', state == Qt.Checked)
        
    def paintEvent(self, event):
        """
        Draws graphic symbol
        """
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
        qp.drawPie(10, 10, 140, 140, 45 * 16, 270 * 16)
        qp.end()

if __name__ == '__main__':
    config = Config('config.json')
    file_processor = FileProcessor(config)
    # Create a new application object
    app = QApplication(sys.argv)
    # Create a new window object
    window = ProgeatApp()
    # Show the window
    window.show()
    # Run the event loop
    sys.exit(app.exec_())
