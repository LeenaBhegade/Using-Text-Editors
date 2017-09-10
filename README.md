# Using Text Editors

## Vim Editor
Vim is a command line editor use extensively for quick file edits. 
It only open in two modes
1. Command Mode 
2. Insert Mode
When you open a file it will open in command mode. If the file contains data, user should be able to move up and down using cursor and type commands.

Type  `vim filename`  to open a vim editor. Opens file if it exists else creates a new file.

### Generic Commands in Vim

* i - After opening vim it does not open in editable mode, type "i"  to switch from command mode to insert mode 
* o - Opens a new line and places the cursor on new line for edit
* Esc - Switch from insert mode to command mode
* dd - Delete th current line the cursor is on
* yy - yank/copy a line
* p/P - paste yanked or deleted line after cursor
* x - delete one character
* G - Go to end of the file 
* / - To search for a text in the file

### Commands for exiting Vim

* :wq - Save the data/file and exit
* :q! - Exit without warnings
* :q  - Exit with warning if unsaved data

## Sublime
Sublime is one of the editors used heavily by developers.

* Install sublime and move in Applications folder
* open /Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl
* Create symbolic link for sublime ->  `ln -s "/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl" /usr/local/bin/sub`

## Useful commands 
* CMD + d - Select a word
* CMD + l - Select a line
* CMD + a - Select the entire document
* CMD + ↑ - Move cursor to start of the file
* CMD + ↓ - Move cursor to end of the file
* CMD + Shift + P - Open the command Pallete 
* CMD + t - Switching between tabs inside the editor

## Code formatting in Sublime for different languages

### Python PEP8 Autoformat 
* To get list of controls type cmd+shift+P
* Choose "Package Control: Install Package"
* Choose Python PEP8 Autoformat and install
* To format the whole docume type : CTRL + SHIFT + r

### Pretty JSON Formatting 
* To get list of controls type cmd+shift+P
* Choose "Package Control: Install Package"
* Choose Pretty JSON and install
* To format the whole docume type : CTRL + CMD + j


### JS Beautifier  
* To get list of controls type cmd+shift+P
* Choose "Package Control: Install Package"
* Choose Pretty JsFormat and install
* To format the whole docume type : CTRL + ALT + f

### Command Pallete ( Allow to perform many operations)
* Set Syntax : Allows to set certain syntax ( HTML , Javascript, Python )
* Package Control Options
















