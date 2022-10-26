
import re
import pandas as pd
from docx import Document
from pyresparser import ResumeParser
import nltk
from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from flask import Flask
import warnings
warnings.filterwarnings('ignore')
import os
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from tika import parser  
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
views = Blueprint(__name__, "views")

library = []
program = []
programming_languages = []
university = []
vocabulary = []
Data = []
data_resume = []
number_resume = 0
skills = []
text_skills = ""

first_open = True

@views.route("/", methods=["GET", "POST"])
def index():
    global number_resume
    global first_open
    global skills
    
    
    if first_open:
        skills = []
        Library()
        Program()
        Programming_Languages()
        University()
        Vocabulary()
        first_open = False
    
    number_resume = 0
    skills = library + program + programming_languages
    return render_template("page_resume.html", skills=skills , number_resume = number_resume)

@views.route("/upload_files", methods=["GET", "POST"])
def upload_files():
    global number_resume
    global skills
    status_file = True
    try:
        #delete_file
        files_delete = os.listdir(os.path.join("Static","Save_Resume"))
        for file in files_delete:
            os.remove(os.path.join("Static","Save_Resume" , file))
        if request.method == 'POST':    
            files = request.files.getlist('files')  
            for file in files:
                if "pdf" != file.filename.split('.').pop():
                    status_file = False
                    return redirect('/')
                    
            if(status_file):
                #save_file
                for file in files:
                    file.save(os.path.join("Static","Save_Resume" , file.filename))
                #number_file
                number_resume = len(files)
    except :
        print("Something")

    return render_template("page_resume.html" , skills=skills , number_resume=number_resume)

@views.route("/submit_files", methods=["GET", "POST"])
def submit_files():
    global text_skills
    global number_resume
    global skills
    text_skills = ""
    text_skills = request.form['input_skills']
    
    if number_resume != 0 and text_skills != "" :   
        return redirect('/result_resume')
    else:
        return render_template("page_resume.html", skills=skills , number_resume=number_resume)
        

@views.route("/result_resume", methods=["GET", "POST"])
def result_resume():
    global Data
    global data_resume 
    global text_skills
    Data = [] 
    file_resume = os.listdir(os.path.join("Static","Save_Resume"))
    for i in range(len(file_resume)):
        data_resume = []
        file_resume[i] = os.path.join("Static","Save_Resume", file_resume[i])
        Data.append({"name" : "" , "email" : "" , "skills" : [] , "college_name" : "" , "score" : 0 , "range" : 0} )
        Check_Name(file_resume[i],i)
        Data_resume(file_resume[i])
        Check_Email(file_resume[i],i)
        Check_University(i)
        Check_Skill(i)
        Count_Score(i)
    #Sort Data
    Sort_Data()
    Range_Data()

    return render_template("page_result_resume.html" , Data = Data , text_skills = text_skills)


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

def Vocabulary():
    global vocabulary
    Vocabulary = pd.read_excel('./static/Vocabulary/Vocabulary.xlsx')
    vocabulary = []
    for i in Vocabulary.keys():
        for j in range(len(Vocabulary[i])):
            if (pd.isna(Vocabulary[i][j])):
                pass
            else:
                tmp = re.sub(r"^\s+|\s+$","", str(Vocabulary[i][j]).lower())
                vocabulary.append(tmp)

def Check_Name(path,num):
    tmp_data_name = []
    special_characters = r'[!@#$%^&*()-+?_=,<>/"]'
    for i in parser.from_file(path)['content'].lower().split("\n"):
        tmp_name = ''
        if re.match(r"\b[A-z]", i) and not re.search(r"\d+" , i) and not re.search(r"\.$" , i.strip()) and not re.search(special_characters , i):
            tmp_data_name.append(i.strip())

    data_name = []
    lemmatizer = WordNetLemmatizer()
    for i in tmp_data_name:
        status = True
        for j  in re.split("\s", i):
            j = lemmatizer.lemmatize(j)
            for k in stopwords.words('english'):
                if j == k:
                    status = False
            for k in library:
                if j == k:
                    status = False
            for k in program:
                if j == k:
                    status = False
            for k in programming_languages:
                if j == k:
                    status = False
            for k in vocabulary:
                if j == k:
                    status = False
        if status:
            data_name.append(i)

    data_name_final = ""
    for i in range(len((" ").join(data_name).split(' '))):
        status = True
        if re.search(r"\." , (" ").join(data_name).split(' ')[i]):
            status = False
        if (" ").join(data_name).split(' ')[i] in data_name_final:
            status = False
        if status:
            if len(data_name_final) == 0:
                data_name_final = (" ").join(data_name).split(' ')[i].capitalize()
            else:  
                data_name_final += " " + (" ").join(data_name).split(' ')[i].capitalize()
    Data[num]['name']= data_name_final

def Check_Email(path, num):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    for i in parser.from_file(path)['content'].split():
        if re.match(regex, i):
            Data[num]['email'] = i

def Check_University(num):
    for i in range(len(data_resume)):
        tmp = data_resume[i]
        for j in range((i+1),len(data_resume)):
            tmp += " " + data_resume[j]
            for k in university:
                if tmp == k:
                    a = ""
                    for l in tmp.split():
                        if not l in stopwords.words('english'):
                            if len(a) == 0:
                                a = l.capitalize()
                            else:
                                a += " "+ l.capitalize() 
                        else:
                            if len(a) == 0:
                                a = l.capitalize()
                            else:
                                a += " "+ l
                    Data[num]['college_name'] = a

def Check_Skill(num):
    tmp_skill = []
    # กรณีชื่อสกิลอยู่คนละบรรทัด
    for i in range(len(data_resume)):
        tmp = data_resume[i]
        for j in range(i+1, len(data_resume)):
            tmp+= " " + data_resume[j]
            for k in library:
                if tmp == k:
                    tmp_skill.append(k)
            for k in program:
                if tmp == k:
                    tmp_skill.append(k)
            for k in programming_languages:
                if tmp == k:
                    tmp_skill.append(k)

    #เช็คคำซ้ำ
    for i in tmp_skill:
        if len(Data[num]['skills']) == 0:
            Data[num]['skills'].append(i)
        check = True
        for j in Data[num]['skills']:
            if i == j:
                check = False
        if check:
            Data[num]['skills'].append(i)

    # กรณีชื่อสกิลอยู่บรรทัดเดียวกัน
    tmp_skill = []
    for i in range(len(data_resume)):
        tmp = data_resume[i] 
        for k in library:
            if tmp == k:
                tmp_skill.append(k)
        for k in program:
            if tmp == k:
                tmp_skill.append(k)
        for k in programming_languages:
            if tmp == k:
                tmp_skill.append(k)

    #เช็คคำซ้ำ
    for i in tmp_skill:
        if len(Data[num]['skills']) == 0:
            Data[num]['skills'].append(i)
        check = True
        for j in Data[num]['skills']:
            if i == j:
                check = False
        if check:
            Data[num]['skills'].append(i)

def Count_Score(num):
    count_score = 0
    for i in text_skills.split(","):
        for j in Data[num]['skills']:
            if i == j:
                count_score += 1
    tmp = round(count_score / len(text_skills.split(",")) * 100)
    Data[num]['score'] = str(tmp) + "%"

def Sort_Data():
    for i in range(len(Data)):
        for j in range((i+1),len(Data)):
            if int(Data[i]['score'].split("%")[0]) < int(Data[j]['score'].split("%")[0]):
                tmp = Data[i]
                Data[i] = Data[j]
                Data[j] = tmp

def Range_Data():
    range_data = 1
    for i in range(len(Data)):
        if i+1 < len(Data):
            if int(Data[i]['score'].split("%")[0]) > int(Data[i+1]['score'].split("%")[0]):
                Data[i]['range'] = range_data
                range_data += 1
            else:
                Data[i]['range'] = range_data
        else:
            Data[i]['range'] = range_data
            

def Data_resume(path):
    for i in parser.from_file(path)['content'].lower().split():
        a = re.sub(r"^\s+" ,"" , i)
        a = re.sub(r"\s+$" ,"" , a)
        a = re.sub(r"[,]" ,"" , a)
        if a != "":
            data_resume.append(a)