import tensorflow as tf 
classifierLoad = tf.keras.models.load_model('model.h5') # load the model here
import pandas as pd
import numpy as np
import cv2
from tensorflow.keras.preprocessing import image
test_image1 = cv2.imread('5.jpg',0)
test_image = image.load_img('5.jpg', target_size = (200,200))  # load the sample image here
#test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)
result = classifierLoad.predict(test_image)
if result[0][0] == 1:
    print("apple-apple scab")
    test_image1 = cv2.resize(test_image1, (380,360))                
    cv2.imshow('sampleimage',test_image1)
    cv2.waitKey(0)
    df = pd.read_excel('APPLE SCAB.xlsx')
    print(df.values)
elif result[0][1] == 1:
    print("apple-black rot")
    test_image1 = cv2.resize(test_image1, (380,360))                
    cv2.imshow('sampleimage',test_image1)
    cv2.waitKey(0)
    df = pd.read_excel('apple block rot.xlsx')
    print(df.values)
elif result[0][2] == 1:
    print("apple sedar-apple rust")
    test_image1 = cv2.resize(test_image1, (380,360))                
    cv2.imshow('sampleimage',test_image1)
    cv2.waitKey(0)
    df = pd.read_excel('Apple___Cedar_apple_rust.xlsx')
    print(df.values)
elif result[0][3] == 1:
    print("corn(maiza)-cercospora gray leaf spot")
    test_image1 = cv2.resize(test_image1, (380,360))                
    cv2.imshow('sampleimage',test_image1)
    cv2.waitKey(0)
    df = pd.read_excel('GREY LEAVE SPOT.xlsx')
    print(df.values)
elif result[0][4] == 1:
    print("corn-common rust")
    test_image1 = cv2.resize(test_image1, (380,360))                
    cv2.imshow('sampleimage',test_image1)
    cv2.waitKey(0)
    df = pd.read_excel('CORN RUST.xlsx')
    print(df.values)
elif result[0][5] == 1:
    print("grape-black rot")
    test_image1 = cv2.resize(test_image1, (380,360))                
    cv2.imshow('sampleimage',test_image1)
    cv2.waitKey(0)
    df = pd.read_excel('grape block rot.xlsx')
    print(df.values)
elif result[0][6] == 1:
    print("grape- NORMAL")
    test_image1 = cv2.resize(test_image1, (380,360))                
    cv2.imshow('sampleimage',test_image1)
    cv2.waitKey(0)
    #df = pd.read_excel('grape esca.xlsx')
    #print(df.values)

elif result[0][5] == 1:
    print("potato late blight")
    test_image1 = cv2.resize(test_image1, (380,360))                
    cv2.imshow('sampleimage',test_image1)
    cv2.waitKey(0)
    df = pd.read_excel('pottato late blight.xlsx')
    print(df.values)
elif result[0][6] == 1:
    print("tomato-Bacterial spot")
    test_image1 = cv2.resize(test_image1, (380,360))                
    cv2.imshow('sampleimage',test_image1)
    cv2.waitKey(0)
    df = pd.read_excel('TOMATTO BACTERIAL SPOT.xlsx')
    print(df.values)

elif result[0][5] == 1:
    print("tomato early blight")
    test_image1 = cv2.resize(test_image1, (380,360))                
    cv2.imshow('sampleimage',test_image1)
    cv2.waitKey(0)
    df = pd.read_excel('TOMOTTO EARLY BLIGHT.xlsx')
    print(df.values)
elif result[0][6] == 1:
    print("tomato-leaf-mold")
    test_image1 = cv2.resize(test_image1, (380,360))                
    cv2.imshow('sampleimage',test_image1)
    cv2.waitKey(0)
    df = pd.read_excel('tomato leaf mold.xlsx')
    print(df.values)
  # this are results



