# 使用的工具
import pyttsx3
from tkinter import*

# 創建一個engine對象
engine = pyttsx3.init()

# 定義一個函數，用於將文字轉換為語音
def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()

# 創建一個tkinter窗口
window=Tk()
window.title("文字轉語音應用")
window.geometry('400x150')

# 創建文本框
entry=Entry(window,width=50)
entry.pack()

# 創建按鈕
btn=Button(window,text="請按這裡轉換",command=lambda:text_to_speech(entry.get()))
btn.pack()

window.mainloop()