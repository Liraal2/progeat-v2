# Copyright 2023 by Liraal2
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the Evil GPL License as published by
# Liraal. You should have received a copy of the
# Evil GPL License along with this program.

#╭─────────────────────────────────────────────╮
#│ │          IMPORT LIBRARIES               │ │
#╰─────────────────────────────────────────────╯

import json
import os

#╭─────────────────────────────────────────────╮
#│ │          HANDLE CONFIG FILE             │ │
#╰─────────────────────────────────────────────╯

class Config:
    def __init__(self, config_file):
        with open(config_file, 'r') as f:
            self.config_data = json.load(f)

    def get(self, key, default=None):
        return self.config_data.get(key, default)
    
    def set(self, key, value=None):
        self.config_data[key] = value
    
    def getPattern(self, pattern):
        patternPath = os.path.join('.\\patterns\\', pattern+'.ptrn.txt')
        if not os.path.exists(patternPath):
            print(f"Error: pattern file {pattern} does not exist")
            return None
        with open(patternPath, 'r') as file:
            file_contents = file.read()
        return file_contents
