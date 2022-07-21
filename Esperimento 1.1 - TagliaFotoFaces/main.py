from PIL import Image
import cv2
import os
import glob

from numpy import save

def cropandsave(img, save_path, img_name):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.4, 4)
    for (x, y, w, h) in faces:
        faces = img[y:y + h, x:x + w]
    try:
        cv2.imwrite(save_path +"\\"+img_name, faces)
    except:
        err_img = cv2.imread("C:\\Users\\Alfonso\\Desktop\\Python\\err.jpg")
        cv2.imwrite(save_path +"\\"+img_name, err_img)

def createFolder(dest_path, newFolder):
    newFolder = os.path.join(dest_path, newFolder)
    os.mkdir(newFolder)

def getImgName(filepath):
    array = filepath.split("\\")
    return array[7]

folders = ["train", "test", "val"]
emotions = ['anger', 'disgust', 'fear', 'happiness', 'neutral', 'sadness']

createFolder("C:\\Users\\Alfonso\\Desktop\\Python\\", "faces")

for folder in folders:
    origin_path = "C:\\Users\\Alfonso\\Desktop\\faces"
    dest_path = "C:\\Users\\Alfonso\\Desktop\\Python\\faces"
    currentPath = origin_path + "\\" + folder
    createFolder(dest_path, folder)
    tvt_path = "C:\\Users\\Alfonso\\Desktop\\Python\\faces" + "\\" + folder
    for emote in emotions:
        createFolder(tvt_path, emote)
        analyze_path = currentPath + "\\" + emote + "\\*.jpg"
        save_path = tvt_path + "\\" + emote
        for filepath in glob.glob(analyze_path):
            print(filepath)
            img_name = getImgName(filepath)
            img = cv2.imread(filepath)
            cropandsave(img, save_path, img_name)