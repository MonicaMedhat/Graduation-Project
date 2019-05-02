# import the necessary packages
import glob

from imutils import contours
from skimage import measure
import numpy as np
import imutils
import cv2
import mysql.connector
from mysql.connector import Error
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


# from database
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
       num = 0
       num2=0

       for row in records:
           # Load image from database
           img = row[0]
           image = np.asarray(bytearray(img), dtype="uint8")
           image2 = cv2.imdecode(image, cv2.IMREAD_COLOR)


           ##############################################################
           #######################Detetcting the light#######################################
           # image = cv2.imread(image2)
           gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
           blurred = cv2.GaussianBlur(gray, (11, 11), 0)

           # el 140 dih kol m texawediha haydetect 7agat 2a2al w kol m tewatiha bhay detect aktar
           _, thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)

           # perform a series of erosions and dilations to remove
           # any small blobs of noise from the thresholded image
           thresh = cv2.erode(thresh, None,iterations=2)  # bet scan kol el pixels 3ashan tetala3 white only decrease white region
           thresh = cv2.dilate(thresh, None, iterations=4)  # increase the white region
           labels = measure.label(thresh, neighbors=8, background=0)
           mask = np.zeros(thresh.shape, dtype="uint8")
           # loop over the unique components

           for label in np.unique(labels):
               # if this is the background label, ignore it
               if label == 0:
                   continue

               # otherwise, construct the label mask and count the
               # number of pixels
               labelMask = np.zeros(thresh.shape, dtype="uint8")
               labelMask[labels == label] = 255
               numPixels = cv2.countNonZero(labelMask)

               # if the number of pixels in the component is sufficiently
               # large, then add it to our mask of "large blobs"

               if numPixels > 300:
                   mask = cv2.add(mask, labelMask)

           cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
           cnts = imutils.grab_contours(cnts)
           cnts = contours.sort_contours(cnts)[0]
           # loop over the contours

           for (i, c) in enumerate(cnts):
               # draw the bright spot on the image
               (x, y, w, h) = cv2.boundingRect(c)
               ((cX, cY), radius) = cv2.minEnclosingCircle(c)


               cv2.circle(image, (int(cX), int(cY)), int(radius),
                          (0, 0, 255), 3)
               cv2.putText(image, "#{}".format(i + 1), (x, y - 15),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

           # img_id = 'select id from dataset where u_id=1'
           #
           # cursor2 = connection.cursor()
           # cursor2.execute(img_id)
           # records = cursor2.fetchall()
           # y = ''.join(map(str, records))
           # z = int(y)
           # print(z)


           # y=row in records
           # x = y[0]
           # print(x)

           # img_id = 'select id from dataset where u_id=1'
           #
           # cursor2 = connection.cursor()
           # cursor2.execute(img_id)
           # records = cursor2.fetchall()
           # # y = ''.join(map(str, records))
           # # z = int(y)
           # # print(z)
           # for row in records:
           #     n = row[0]
           #     print(n)

           img_id = 'SELECT id FROM dataset ORDER BY ID DESC LIMIT 1'
           #
           cursor2 = connection.cursor(prepared=True)
           cursor2.execute(img_id)
           records = cursor2.fetchall()

           for row in records:
               x = row[0]
               print(x)


           lighted=True
           if (i <= 4):
               print('Not Lighted ')

               cursor = connection.cursor(prepared=True)
               sql_select_Query = """UPDATE `dataset` SET `result_id`=%s where id= %s """

               result_id=2
               id=x
               input =(result_id,id)
               cursor.execute(sql_select_Query,input)

               connection.commit()

               num += 1

           else:
               print('Lighted')

               cursor = connection.cursor(prepared=True)
               sql_select_Query = """UPDATE `dataset` SET `result_id`=%s where id= %s """
               result_id = 1
               id = x
               input = (result_id, id)

               cursor.execute(sql_select_Query, input)

               connection.commit()
               num2 += 1

           ################################################################

           cv2.imshow('from database',image)
           cv2.waitKey(0)
           cv2.destroyAllWindows()




       cursor.close()
except Error as e :
    print ("Error while connecting to MySQL", e)
finally:
    #closing database connection.
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")






# files = glob.glob ("D:/Gradiuation/dataset/nightSequence1/min/nightSequence1*.jpg")
# num_samples = len(files)
# print("number of images ", num_samples)
# num = 0
# for myFile in files:

    # image = cv2.imread(myFile)
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # blurred = cv2.GaussianBlur(gray, (11, 11), 0)
    # # cv2.imshow(' blurred',blurred)
    # # el 140 dih kol m texawediha haydetect 7agat 2a2al w kol m tewatiha bhay detect aktar
    # _ ,thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)
    # # cv2.imshow('thresh',thresh)
    # # perform a series of erosions and dilations to remove
    # # any small blobs of noise from the thresholded image
    # thresh = cv2.erode(thresh, None,iterations=2)  # bet scan kol el pixels 3ashan tetala3 white only decrease white region
    # thresh = cv2.dilate(thresh, None, iterations=4)  # increase the white region
    # labels = measure.label(thresh, neighbors=8, background=0)
    # mask = np.zeros(thresh.shape, dtype="uint8")
    # # loop over the unique components
    # for label in np.unique(labels):
    #     # if this is the background label, ignore it
    #     if label == 0:
    #         continue
    #
    #     # otherwise, construct the label mask and count the
    #     # number of pixels
    #     labelMask = np.zeros(thresh.shape, dtype="uint8")
    #     labelMask[labels == label] = 255
    #     numPixels = cv2.countNonZero(labelMask)
    #
    #     # if the number of pixels in the component is sufficiently
    #     # large, then add it to our mask of "large blobs"
    #     if numPixels > 300:
    #         mask = cv2.add(mask, labelMask)
    #
    # cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
    #                         cv2.CHAIN_APPROX_SIMPLE)
    # cnts = imutils.grab_contours(cnts)
    # cnts = contours.sort_contours(cnts)[0]
    # # loop over the contours
    # for (i, c) in enumerate(cnts):
    #     # draw the bright spot on the image
    #     (x, y, w, h) = cv2.boundingRect(c)
    #     ((cX, cY), radius) = cv2.minEnclosingCircle(c)
    #     cv2.circle(image, (int(cX), int(cY)), int(radius),
    #                (0, 0, 255), 3)
    #     cv2.putText(image, "#{}".format(i + 1), (x, y - 15),
    #                 cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
    #
    #
    #
    # if(i<=4):
    #     print('Not Lighted ')
    #     num+=1
    # else:
    #     print('Lighted')
    #     num+=1

#results = len(num)

print("labels array size NL ",num)
print("labels array size L ",num2)

# show the output image

