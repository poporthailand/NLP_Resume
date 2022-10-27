
import webbrowser
import os

c = webbrowser.Chrome(r'C:\Program Files\Google\Chrome\Application\chrome.exe')
# c.open()
file_name = os.listdir(os.path.join("Static","Save_Resume"))
for i in file_name:
    c.open(os.path.abspath(os.path.join("Static","Save_Resume" , i)))