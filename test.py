# import os
# files = os.listdir(os.path.join("Static","Save_Resume"))
# for file in files:
#     os.remove(os.path.join("Static","Save_Resume" , file))
from bs4 import BeautifulSoup
import requests
url_html = "http://127.0.0.1:8000/"
req = requests.get(url_html)
soup = BeautifulSoup(req.text, 'html.parser')
print(soup)

# import email
# import os
# import spacy
# from PyPDF2 import PdfFileReader

# paths = os.listdir(os.path.join("Static","Save_Resume"))
# print(os.path.join("Static","Save_Resume",paths[0]))

# nlp = spacy.load("en_core_web_sm")
# pdf = pdfplumber.open('C:/Person.pdf')
# page = pdf.pages[0]
# doc = nlp(page.extract_text())
# print([(X.text, X.label_) for X in doc.ents if X.label_ == 'PERSON'])
# paths = 'C:/Users/IMR/Desktop/NLP_Resume/static/Save_Resume/Resume_อิศมัต.pdf'
# pdf = PdfFileReader(paths)
# print(pdf.pages[0].extract_text())
# pdf_read = PDF_read.decode('UTF-8')  
# print(pdf_read)

# import re
# # Make a regular expression
# # for validating an Email

# from tika import parser  
# print(parser.from_file(".\static\Save_Resume\Resume_อิศมัต.pdf")['content'].lower())