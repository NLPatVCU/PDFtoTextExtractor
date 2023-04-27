install.sh is for Debian Linux
Prerequisites: apt and python above 3.8

The project includes 3 main parts:<br>
PDF Text Extractor - extracts text from PDF</br>
Image Extractor from PDF - extracts images and saves it to a folder 
Text Visualizer - Visualize the text to see what the computer recognizes

If on debian linux do <h5>Sudo bash install.sh</h5>
Steps:
1. Install tesseract-ocr and libtesseract-dev using your os package installed
2. Create a virual env python3 -m venv venv
3. source venv/bin/activate
4. Install all libraries required pip install -r requirments.txt

Depending on your work load either use **main.py** if you want a graphical interface or **maincli.py** to use command line argumets

For __mainCLI.py__ you can use either syntax
<br>
`python3 main.py PDFfile`   
or 
<br>
`python3 main.py PDFfile -o outputFileName`

For __visualizer.py__ the syntax is
<br>
`python3 visualizer.py PDFfile`
