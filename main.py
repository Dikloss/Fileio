from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
import requests



def upload():
    filepath = fd.askopenfilename()# путь к файлу, который будем получать
    if filepath:
        files = {"file": open(filepath, "rb")}# открываем файл в пкжиме чтения
        response = requests.post("https://file.io", files=files)# ответ, кот. получим на направленный запрос
        if response.status_code == 200:
            link = response.json()["link"]
            entry.insert(0, link)



window = Tk()
window.title("Сохранение файлов в облаке")
window.geometry("400x200")

button = ttk.Button(text="Загрузить файл", command=upload)
button.pack()

entry = ttk.Entry()
entry.pack()

window.maimloop()

