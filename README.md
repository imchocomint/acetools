# acetools [Windows]
GUI tools for Acestream + patched for no ads

## Usage
Download acetools.exe and engine-[platform].zip. Extract the folder inside the zip file to somewhere convenient. Move the acetools executable into one folder above the extracted folder.

Install VLC to C:\Program Files\.

Search for the needed stream, copy the link and paste in the "Link" section. Click the green button and enjoy.

## Patches to the engine
- Removing the problematic GUI (asking for Premium)
- Removing the default browser (ace_web) and patch it with a placeholder

## Build
Inside ./src:

`nuitka --standalone --onefile --enable-plugin=tk-inter --windows-console-mode=disable main.py`
