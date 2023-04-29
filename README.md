# Progeat-v2.0
Progeat-v2.0 is a Python-based application that processes .cml files and generates output in a specific format. It provides a simple GUI for user interaction and supports the use of Avogadro or XML for file processing.

## Features
- Process .cml files using Avogadro or XML
- Generate .com and .sh files
- Simple GUI for easy user interaction
- Customizable configuration using a JSON file
- Prerequisites
    - Python 3.6 or higher
    - PyQt5
    - PyAutoGUI
    - PyWinAuto
    - Pyperclip
    - Avogadro (optional)
## Installation
1. Clone the repository or download the source files.
2. Install the required dependencies:
```
pip install -r requirements.txt
```
## Configuration
Create a config.json file in the project directory and customize the settings according to your requirements. Here's a sample configuration:
```
{
  "output_dir_path": "path/to/output/directory",
  "use_avogadro": trues
}
```
## Usage
Run the main.py script to launch the application:

```
python main.py
```
Use the GUI to input the required information:

- Filepath: The path to the .cml file you want to process.
- Override filename: An optional filename to use instead of the original .cml file's name.
- Override [0 1]: Override string to be included in the output.
- Use Avogadro?: Enable or disable the use of Avogadro for file processing.
Click the "RUN" button to process the .cml file and generate the output files (.com and .sh) in the specified output directory.

## License
This project is licensed under the Evil General Public License v1.0 (EvilGPL) as included.