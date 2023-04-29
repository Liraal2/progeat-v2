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
import time
import xml.etree.ElementTree

import pyautogui
import pyperclip
import pywinauto


#╭─────────────────────────────────────────────╮
#│ │          PROCESS CML FILE               │ │
#╰─────────────────────────────────────────────╯

class FileProcessor:
    def __init__(self, config):
        self.config = config

    #Send appropriate keystrokes for avogadro version 1.97
    #Calling this function requires that the avogadro window be in focus
    def manipulateAvogadro(self):
        #Send appropriate keystrokes
        pyautogui.hotkey('alt', 'i') #open Interface menu
        for i in range(7): #7x do...
            pyautogui.press('down') #...press Down arrow
        pyautogui.press('enter') #enter menu
        pyautogui.hotkey('shift', 'tab') #go back 1 tab in tab order
        pyautogui.hotkey('ctrl', 'a') #select all
        pyautogui.hotkey('ctrl', 'c') #copy
        
        #Wait for clipboard to populate
        time.sleep(1) # Adjust the delay if needed
        
        #Return system clipboard content
        return pyperclip.paste()

    def openAvogadro(self, path):
        #Open the file with its default application
        os.startfile(path)
        #Wait for the application to start
        time.sleep(3) # Adjust the delay if needed
        #Connect to the application window
        app = pywinauto.Application().connect(title_re=r"Avogadro")
        #Bring window into focus
        app.top_window().set_focus()
        #Send required keystrokes & extract text via clipboard
        avogadroOutput = self.manipulateAvogadro()
        #Kill application
        app.kill()
        #Extract table from clipboard output
        table = avogadroOutput.replace('\r','').split("0 1\n", 1)[1].rstrip()
        return table

    def openXML(self, path):
        #Parse the XML file
        tree = xml.etree.ElementTree.parse(path)
        #Get the root element of the XML tree
        root = tree.getroot()
        #Create output string
        result = ""
        #Iterate through the atom elements
        for atom in root.find('{http://www.xml-cml.org/schema}atomArray').findall('{http://www.xml-cml.org/schema}atom'):
            result = result + "{:6}{: 6f}   {: 6f}   {: 6f}\n".format(atom.get('elementType'), float(atom.get('x3')),float(atom.get('y3')),float(atom.get('z3')))
        return result.rstrip()

    #Process singular .cml file
    #Calling this function requires that avogadro be the default app associated with .cml
    def processFile(self, path, override01String, filename = None):
        cmlFileContent = self.openAvogadro(path) if self.config.get('use_avogadro') else self.openXML(path)
        
        #Extract filename from path
        filename = os.path.splitext(os.path.basename(path))[0]
        
        #Get base output dir from outputDirPath or input dir if outputDirPath not set
        outputPath = self.config.get('output_dir_path') if self.config.get('output_dir_path') is not None else os.path.split(path)[0]
        #Attach dir name
        outputPath = os.path.join(outputPath, filename)
        #Check if dir exists
        if not os.path.exists(outputPath):
            #If not, create it
            os.makedirs(outputPath)
        
        #Create .com file
        filepath = os.path.join(outputPath, filename+".com")
        comFilePattern = self.config.getPattern("com")
        if comFilePattern is None:
            return
        with open(filepath, 'w') as f:
            f.write(comFilePattern.format(fname = filename, overrideString = override01String, content = cmlFileContent))
        
        #Create .sh file
        filepath = os.path.join(outputPath, filename+".sh")
        shFilePattern = self.config.getPattern("sh")
        if shFilePattern is None:
            return
        with open(filepath, 'w') as f:
            f.write(shFilePattern.format(fname = filename))
