# 2024/05/01 AI프로그래밍및실습 해양학전공

# 개인프로젝트

"""
#
from gtts import gTTS
import playsound

news = '안녕하쇼'
tts=gTTS(text=news, lang='ko')
tts.save("news_Son.mp3")
playsound.playsound("news_Son.mp3", True)

#
from gtts import gTTS
import playsound

tts = gTTS("Hi, good to see u", lang='en')
tts.save("news2_Son.mp3")
playsound.playsound("news2_Son.mp3", True)
"""
### 과제: SVM(support_vector_machine) 개념 알아오기 ###

#
from sklearn import datasets

d=datasets.load_iris()  # iris 데이터셋을 읽고
#print(d.DESCR)          # 내용은 출력

#for i in range(0, len(d.data)):         # 샘플을 순서대로 출력
    #print(i+1, d.data[i], d.target[i])

from sklearn import svm

s = svm.SVC(gamma=0.1, C=10)                        # svm 분류 모델 SVC 객체 생성하고
s.fit(d.data, d.target)                             # iris 데이토러 학습

new_d=[[3.4, 1.2, 1.0, 1.5], [7.1, 3.1, 4.7, 1.35]] # 101번째와 51번째 샘플을 변형하여 새로운 데이터 생성

res=s.predict(new_d)
print("새로운 2개 샘플의 부류는", res)