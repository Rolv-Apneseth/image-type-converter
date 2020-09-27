# image-type-converter
 Converts files between different image file types e.g. png, jpg, pdf etc. One of my first ever projects. This is a very simple program and only converts .jpg or .png files into .jpg, .png or .pdf.

## What I learned
* Building GUI's using tkinter
* Handling and filtering different file types
* Use of the Pillow module

## Installation
1. Requires python 3.6+ to run. Python can be installed from [here](https://www.python.org/downloads/).
2. Clone the repository by opening your command line/terminal and run: git clone https://github.com/Rolv-Apneseth/hacker-news-webscraper.git
    * Note: if you don't have git, it can be downloaded from [here](https://git-scm.com/downloads).
3. Install the requirements for the program.
    * In your terminal, navigate to the cloned directory and run: pip install -r requirements.txt
4. To run the actual program, navigate further into the file-sorter folder and run: python3 main.py

## Usage
1. Place any .jpg or .png files you wish to connvert into the Images folder.
2. On the left side of the gui, click the image type of the images you want converted.
3. On the right side of the gui, click on the image type you want to convert them into.
4. Click on the convert button. Your converted images can be found inside the Converted_Images folder.

Alternatively, run convert_script.py and give the file type you want to convert from and to as the first two arguments
    * i.e. Run: python3 convert_script.py  "jpg" "png" to convert .jpg files to .png.


