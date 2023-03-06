
# 導入所需要的函式庫
import speech_recognition as sr 

# 建立語音辨識器
r = sr.Recognizer()

# 讀取檔案
# audio_file = sr.AudioFile('tt.wav')

# 讀取音檔
# with audio_file as source:
#     audio = r.record(source)

# 開啓麥克風，開始監聽
with sr.Microphone() as source:
    print("請開始說話：")

    audio = r.listen(source)



# 語音辨識
try:
    print("您說的是：" + r.recognize_google(audio, language="zh-TW"))
except sr.UnknownValueError:
    print("Google Speech Recognition 無法辨識")
except sr.RequestError as e:
    print("無法連接到 Google Speech Recognition 伺服器： {0}".format(e))