# pip install py-pdf-parser will fix your issue
# This is not everything that tesseract is reading but it helps to visualize which texts general ocrs recognize from the pdf
from py_pdf_parser.loaders import load_file
from py_pdf_parser.visualise import visualise
import argparse

def visualizer(inputFile):
    document = load_file(inputFile)
    visualise(document)

if __name__ == "__main__":
    # Tkinter for gui file selector
    parser = argparse.ArgumentParser(
        description='Visualizes what OCR program recognizes')
    # parser. .ArgumentParser(description='python3 mainCLI.py inputFile.pdf')

    parser.add_argument('inputFile', metavar='input', type=str, help='an input file')
    args = parser.parse_args()

    visualizer(args.inputFile)