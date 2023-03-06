import openai
import pyttsx3
import speech_recognition as sr 
from tkinter import*

def text_to_speech():
    # 建立語音辨識器
    r = sr.Recognizer()

    # 開啓麥克風，開始監聽
    with sr.Microphone() as source:
        #print("請開始說話：")

        audio = r.listen(source)

    # 語音辨識
    try:
        text=r.recognize_google(audio, language="zh-TW")
        #print("您說的是：" + text)
    except sr.UnknownValueError:
        text="Google Speech Recognition 無法辨識"
    except sr.RequestError as e:
        text="無法連接到 Google Speech Recognition 伺服器： {0}".format(e)

    openai.api_key = "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"
    # https://platform.openai.com/account/api-keys

    response = openai.Completion.create( # Completion 是指生成完整內容，其他的請參考官方文件
    model = "text-davinci-003", # 要使用的模型 https://platform.openai.com/docs/models
    max_tokens = 1000, # 生成文字的最長長度
    temperature = 0.8, # 生成的文字溫度、風格
    prompt = text # 問題
    # 還有其他參數可使用，請參考官方文件
    )
    #print(response)
    # 完整的回應json
    print(response["choices"][0]["text"])
    # 取出回應內容的文字部分

    # 初始化設定
    engine = pyttsx3.init()
    # 讀取文字
    text = response["choices"][0]["text"]
    # 語音輸出
    engine.say(text)
    engine.runAndWait()

# 創建一個tkinter窗口
window=Tk()
window.title("聊天")
window.geometry('400x150')

# 創建按鈕
btn=Button(window,text="開始",command=lambda:text_to_speech())
btn.pack()

window.mainloop()