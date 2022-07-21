import os
import shutil
import csv
import glob
from tkinter import Tk, filedialog

emotions = ['anger', 'disgust', 'fear', 'happiness', 'neutral', 'sadness']
letter_emotions = ['a', 'd', 'f', 'h', 'n', 's']
folders = ['train' , 'val', 'test']

train = [0, 0, 0, 0, 0, 0]
val = [0, 0, 0, 0, 0, 0]
test = [0, 0, 0, 0, 0, 0]

header = ["nome file", "emozione"]

def choosePath():
    root = Tk() 
    root.withdraw() 
    root.attributes('-topmost', True) 
    return filedialog.askdirectory() 

def createFolders(dest_path):
    folder2 = os.path.join(dest_path, "dest")
    os.mkdir(folder2)
    dest_path+="/dest"
    for folder in folders:
        newF = os.path.join(dest_path, folder)
        os.mkdir(newF)
        for emote in emotions:
            temp_dest_f = dest_path + "/" + folder
            folder_path = os.path.join(temp_dest_f, emote)
            os.mkdir(folder_path)
    return dest_path

print("Inserire cartella di origine")
origin_path = "C:/Users/Alfonso/Desktop/SistemaAgenti/Datasets/FACES Filtrato" +  "/*.jpg"
print("Inserire cartella di destinazione")
dest_path = "C:/Users/Alfonso/Desktop/SistemaAgenti/Script/servizioNicola/DivisioneDatasetPerEmozione"
dest_path = createFolders(dest_path)

for folder in folders:
    with open(dest_path +'/'+ folder +'.csv', 'w', newline='') as fcsv:
        writer = csv.writer(fcsv, delimiter=',')
        writer.writerow(header)

for filepath in glob.glob(origin_path):
    indexEmotion = 0
    temp_filename = filepath.rsplit("\\")
    filename = temp_filename[1]
    print(filename)
    for firstLetter in letter_emotions:
        if(filename[8] == firstLetter):
            for folder in folders:
                if folder == "train":
                    if train[indexEmotion] < 80:
                        dst_path = dest_path+"/train/"+emotions[indexEmotion]
                        shutil.move(filepath, dst_path)
                        train[indexEmotion] += 1
                        with open(dest_path +'/'+folder+'.csv', 'a', newline='') as fcsv:
                            writer = csv.writer(fcsv, delimiter=',')
                            writer.writerow([emotions[indexEmotion]+'/'+filename]+[indexEmotion])
                        break
                elif folder == "val":
                    if val[indexEmotion] < 23:
                        dst_path = dest_path+"/val/"+emotions[indexEmotion]
                        shutil.move(filepath, dst_path)
                        val[indexEmotion] += 1
                        with open(dest_path +'/'+folder+'.csv', 'a', newline='') as fcsv:
                            writer = csv.writer(fcsv, delimiter=',')
                            writer.writerow([emotions[indexEmotion]+'/'+filename]+[indexEmotion])
                        break
                elif folder == "test":
                    if test[indexEmotion] < 11:
                        dst_path = dest_path+"/test/"+emotions[indexEmotion]
                        shutil.move(filepath, dst_path)
                        test[indexEmotion] += 1
                        with open(dest_path +'/'+ folder +'.csv', 'a', newline='') as fcsv:
                            writer = csv.writer(fcsv, delimiter=',')
                            writer.writerow([emotions[indexEmotion]+'/'+filename]+[indexEmotion])
                        break
        indexEmotion+=1