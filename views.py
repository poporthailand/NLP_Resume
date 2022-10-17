import textract
import numpy as np
import math
import re
import pandas as pd
from docx import Document
from pyresparser import ResumeParser
import nltk
from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from flask import Flask
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)
views = Blueprint(__name__, "views")

library = []
program = []
programming_languages = []
university = []


@views.route("/", methods=["GET", "POST"])
def index():
    skills = []
    Library()
    Program()
    Programming_Languages()
    University()
    skills = library + program + programming_languages
    
    return render_template("page_resume.html", skills=skills)


def Library():
    global library
    Library = pd.read_excel('./static/Library/Library.xlsx')
    library = []
    for i in Library.keys():
        for j in range(len(Library[i])):
            if (pd.isna(Library[i][j])):
                pass
            else:
                tmp = re.sub(r"\(.*\)", "", Library[i][j].lower())
                tmp = re.sub(r"by.*", "", tmp)
                tmp = re.sub(r"\xa0", " ", tmp)
                tmp = re.sub(r"^\s+|\s+$", "", tmp)
                library.append(tmp)


def Program():
    global program
    Program = pd.read_excel('./static/Program/Program.xlsx')
    program = []
    for i in Program.keys():
        for j in range(len(Program[i])):
            if (pd.isna(Program[i][j])):
                pass
            else:
                tmp = re.sub(r"\(.*\)", "", Program[i][j].lower())
                tmp = re.sub(r"by.*", "", tmp)
                tmp = re.sub(r"\xa0", " ", tmp)
                tmp = re.sub(r"\[\d+\]", "", tmp)
                tmp = re.sub(r"^\s+|\s+$", "", tmp)
                program.append(tmp)


def Programming_Languages():
    global programming_languages
    Programming_Languages = pd.read_excel(
        './static/Programming_Languages/Programming_Languages.xlsx')
    programming_languages = []
    for i in Programming_Languages.keys():
        for j in range(len(Programming_Languages[i])):
            if (pd.isna(Programming_Languages[i][j])):
                pass
            else:
                tmp = re.sub(
                    r"\(.*\)", "", Programming_Languages[i][j].lower())
                tmp = re.sub(r"by.*", "", tmp)
                tmp = re.sub(r"\xa0.*", "", tmp)
                tmp = re.sub(r"^\s+|\s+$", "", tmp)
                programming_languages.append(tmp)


def University():
    global university
    University = pd.read_excel('./static/University/University.xlsx')
    university = []
    for i in University.keys():
        for j in range(len(University[i])):
            if (pd.isna(University[i][j])):
                pass
            else:
                tmp = re.sub(r"\(.*\)", "", University[i][j].lower())
                tmp = re.sub(r"\[\d+\]", "", tmp)
                tmp = re.sub(r"^\s+|\s+$", "", tmp)
                university.append(tmp)
