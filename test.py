import pyttsx3

# 初始化設定
engine = pyttsx3.init()

# 讀取文字
text = input('請輸入要轉成語音的文字: ')

# 語音輸出
engine.say(text)
engine.runAndWait()