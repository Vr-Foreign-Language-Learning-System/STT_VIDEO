
import requests
from mutagen.mp4 import MP4
import librosa
import soundfile as sf

# clova

client_id = "id 값 넣기"
client_secret = "secret 키 값 넣기"
lang = "Kor" # 언어코드{Kor, Jpn, Eng, Chn}
url = "https://naveropenapi.apigw.ntruss.com/recog/v1/stt?lang=" + lang

headers = {
    "X-NCP-APIGW-API-KEY-ID": client_id,
    "X-NCP-APIGW-API-KEY": client_secret,
    "Content-Type" : "application/octet-stream"
}


def open_file(file_name, origin_rate):
    data, rate = librosa.load(file_name, sr = origin_rate)
    return data, rate


def split_wav(data, sample_rate, start, end):
  start *= sample_rate
  if end >= length: end = length
  end *= sample_rate
  return data[start:end]

# 원본 mp4 파일
dir = '../[레전드] 겁나웃긴 자매의 장난전화 (욕설 주의).mp4'

# 길이 확인
length = int(MP4(dir).info.length)
print(length)

# mp4 파일 오픈 -> wav
wav_data, sample_rate = open_file(dir, 48000)

# 60초 만큼 잘라서 저장
j = 0
for i in range(0, length, 60):
    j+=1
    edited_data = split_wav(wav_data, 48000, i, i+60)
    edited_dir = "./[레전드] 겁나웃긴 자매의 장난전화 (욕설 주의)"+str(j)+".wav"
    sf.write(edited_dir, edited_data, 48000, subtype='PCM_16')


data_dir = "./[레전드] 겁나웃긴 자매의 장난전화 (욕설 주의)"

# 60초 wav 파일 -> stt
for n in range(1,j+1,1):
    data = open(data_dir+str(n)+".wav", 'rb')
    response = requests.post(url, data=data, headers=headers)
    rescode = response.status_code
    if(rescode == 200):
        print(response.text)
    else :
        print("Error : " + response.text)

