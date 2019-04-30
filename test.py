# import the necessary packages
import glob

from imutils import contours
from skimage import measure
import numpy as np
import argparse
import imutils
import os
import cv2
import mysql.connector
from mysql.connector import Error
try:
    connection = mysql.connector.connect(host='localhost',
                             database='gp',
                             user='root',
                             password='')
    if connection.is_connected():
       db_Info = connection.get_server_info()
       print("Connected to MySQL database... MySQL Server version on ",db_Info)

       cursor = connection.cursor()
       cursor.execute("select database();")
       record = cursor.fetchone()
       print ("Your connected to - ", record)

       sql_select_Query = "SELECT `image` FROM `dataset` WHERE u_id=1"
       cursor = connection.cursor()
       cursor.execute(sql_select_Query)
       records = cursor.fetchall()
       print("Total number of rows in python_developers is : ", cursor.rowcount)
       print("Printing each row's column values i.e.  developer record")
       for row in records:
           # Load image from database
           img = row[0]
           image = np.asarray(bytearray(img), dtype="uint8")
           image2 = cv2.imdecode(image, cv2.IMREAD_COLOR)
           cv2.imshow('from database',image2)
       cursor.close()
except Error as e :
    print ("Error while connecting to MySQL", e)
finally:
    #closing database connection.
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


# construct the argument parse and parse the arguments

# filename='D:/Gradiuation/dataset/img.jpg'


# files = glob.glob ("D:/Gradiuation/dataset/nightSequence1/min/nightSequence1*.jpg")
#
# for myFile in files:
#     # print(myFile)
#     image = cv2.imread (myFile)
#     # print(image)
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     # cv2.imshow(' blurred', gray)
#     blurred = cv2.GaussianBlur(gray, (11, 11), 0)
#     # cv2.imshow(' blurred',blurred)
#     _ ,thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)
#     # cv2.imshow('thresh',thresh)
#     thresh = cv2.erode(thresh, None, iterations=2)
#     thresh = cv2.dilate(thresh, None, iterations=4)
#     labels = measure.label(thresh, neighbors=8, background=0)
#     mask = np.zeros(thresh.shape, dtype="uint8")
#
#
#     # X_data.append (image)
#     # labels.append('Pedestrian')
#
#
#     # loop over the unique components
#     for label in np.unique(labels):
#         # if this is the background label, ignore it
#         if label == 0:
#          continue
#
#         # otherwise, construct the label mask and count the
#         # number of pixels
#     labelMask = np.zeros(thresh.shape, dtype="uint8")
#     labelMask[labels == label] = 255
#     numPixels = cv2.countNonZero(labelMask)
#
#     # if the number of pixels in the component is sufficiently
#     # large, then add it to our mask of "large blobs"
#     if numPixels > 300:
#         mask = cv2.add(mask, labelMask)
#     cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
#                         cv2.CHAIN_APPROX_SIMPLE)
#     cnts = imutils.grab_contours(cnts)
#     # cnts = contours.sort_contours(cnts)[0]
#
#     # loop over the contours
#     for (i, c) in enumerate(cnts):
#         # draw the bright spot on the image
#         print(c)
#         (x, y, w, h) = cv2.boundingRect(c)
#         ((cX, cY), radius) = cv2.minEnclosingCircle(c)
#         cv2.circle(image, (int(cX), int(cY)), int(radius),
#                (0, 0, 255), 3)
#         cv2.putText(image, "#{}".format(i + 1), (x, y - 15),
#                 cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255),2)
#
#         # classes = ['lighted', 'not lighted']
#         print (i)
#
#         blob = cv2.dnn.blobFromImage(image, 1, (224, 224), (104, 117, 123))
#         cv2.imshow("Image", image)
cv2.waitKey(0)