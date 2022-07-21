import requests
import json
import csv
import glob
from tkinter import Tk, filedialog


def choosePath():
    print("Inserire percorso del dataset")
    root = Tk() 
    root.withdraw() 
    root.attributes('-topmost', True) 
    return filedialog.askdirectory() 

def sendRequest(path):
    newp = path.replace("\\", "/")
    my_img = {'image': open(newp, 'rb')}
    url = 'https://www.intintlab.uniba.it/face-analyzer'
    my_data = {"emotion": "yes", "gender": "no", "age": "no", "detect_face": "no"} 
    r = requests.post(url, data=my_data, files=my_img, verify=False)
    data = r.json()
    return data

def inserireNomeFile():
    print("Inserire nome file csv da salvare (senza estensione)")
    return input()

def checkCorrispondenza(filename, emotion):
    temp = str(filename)
    faces_emote = temp[8]
    flag = 0
    if(flag == 0 and emotion == "Anger" and faces_emote == "a"):
        flag = 1
    if(flag == 0 and emotion == "Disgust" and faces_emote == "d"):
        flag = 1
    if(flag == 0 and emotion == "Fear" and faces_emote == "f"):
        flag = 1
    if(flag == 0 and emotion == "Happiness" and faces_emote == "h"):
        flag = 1
    if(flag == 0 and emotion == "Neutral" and faces_emote == "n"):
        flag = 1
    if(flag == 0 and emotion == "Sadness" and faces_emote == "s"):
        flag = 1
    if(flag == 0 and emotion == "Surprise"):
        flag = 2
    return flag


nomefile = inserireNomeFile()
temp_path = str(choosePath())
temp_path += "/*.jpg"

header = ['nome', 'emozione', 'prob', 'corrispondenza']

with open(nomefile+'.csv', 'w') as fcsv:
    writer = csv.writer(fcsv, delimiter=',')
    writer.writerow(header)
i = 1
for fname in glob.glob(temp_path):
    with open(nomefile+'.csv', 'a') as fcsv:
        writer = csv.writer(fcsv, delimiter=',')
        filename = fname.rsplit("\\")
        name = filename[1]
        print(i,") ", name)
        if name[4] == "o":
            data = sendRequest(str(fname))
            if "error" in str(data):
                print("Faccia non trovata")
                writer.writerow([filename[1]]+["Faccia non trovata"])
                i+=1    
            else:
                emotion = json.dumps(data["emotion"])
                emotion_CUT = emotion.replace('\"', '')
                probabilities = json.dumps(data["probabilities"])
                probabilities_CUT = probabilities.replace('\"', '')
                writer.writerow([filename[1]]+[emotion_CUT]+[probabilities_CUT]+[checkCorrispondenza(filename[1], emotion_CUT)])
                i+=1 
print("Analisi Terminata. Premere un tasto per continuare...")
input()