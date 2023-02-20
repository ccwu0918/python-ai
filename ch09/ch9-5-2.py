import win32com
from win32com.client import Dispatch
import os

app = win32com.client.Dispatch("Word.Application")
app.Visible = 1
app.DisplayAlerts = 0
docx = app.Documents.Open(os.getcwd()+"\\test.docx")
