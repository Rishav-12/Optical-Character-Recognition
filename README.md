# findthosewords
A program to detect text in images

### Requirements
* opencv
* pytesseract

There are three test images in the assets folder

This project is inspired by a [video](https://youtu.be/6DjFscX4l_c) from Murtaza's Workshop YouTube channel

### Installation & Usage
1. Install dependencies with `pip install -r requirements.txt`
	* If this doesn't work, try installing the libraries `pillow`, `pytesseract`, and `opencv-python` manually one-by-one
2. Use the command `python main.py [path_to_image_file]` to get the image alongwith the identified text

Make sure you have tesseract installed.

- On Linux, do `apt install tesseract-ocr`
- On Windows, download the binary from https://github.com/UB-Mannheim/tesseract/wiki

Refer the pytesseract docs for more information
