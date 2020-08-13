# pyprog4iot
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

This repo serves as a documentation for the codes that i tried to do for the End-Of-Term assignment for Elective Code EP0401.


## Usage
This entire code is meant to work with a raspberry pi and a USB WebCam connect to it. All of the workplace should be in a raspbian linux environment.

Before using the code, please make sure the following points are fulfilled.
- Webcam is enabled in settings.
- `OpenCV` has been installed to the system. 
- `imutils` has been installed to the system.

If any of the above is not fulfilled, refer to the step on how to execute.

## Setup
### Installing `imutils`.
1. Install it via pip by running this in terminal:
    ```bash
    pip install imutils
    ```
### Installing `OpenCV`
1. Install it via pip by running this in terminal:
    > Attention: **This is not the official built version**
    ```bash
    pip install opencv-contrib-python
    ```
### Installing `DropBox`
1. Install it via pip by running this in terminal:
    ```bash
    pip install --upgrade dropbox
    ```

## Usage
### Running the script(Please run it from terminal)
1. Running a python script
    1. Open terminal.
    1. Run the following command:
        ```bash
        python <python file name>
        e.g.: 
        python videostream_demo.py
        ```