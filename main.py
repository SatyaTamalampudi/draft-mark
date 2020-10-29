import cv2
import pytesseract
#from imutils.object_detection import non_max_suppression

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
cv2.namedWindow("output", cv2.WINDOW_NORMAL)
img = cv2.imread('frame11.jpg')
#img = cv2.imread('example_01.jpg')
#img = cv2.imread('Capture.png')
#img = cv2.imread('Still_watersurface_imag.JPG')
#img = cv2.imread('Resized_opening.jpg')
#img = cv2.imread('Resized_closing.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#print(pytesseract.image_to_string(img))

#Returns bounding box information
#print(pytesseract.image_to_boxes(img))
# Detecting Characters
# hImg, wImg,_ = img.shape
# conf = r'--oem 1 --psm 6 outputbase digits'
# boxes = pytesseract.image_to_boxes(img,config = conf)
# for b in boxes.splitlines():
#     print(b)
#     b = b.split(' ')
#     print(b)
#     x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
#     cv2.rectangle(img, (x,hImg- y), (w,hImg- h), (50, 50, 255), 2)
#     cv2.putText(img,b[0],(x,hImg- y+25),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)



# # ### Detecting Words
# hImg, wImg,_ = img.shape
# boxes = pytesseract.image_to_data(img)
# #print(boxes)
# for x,b in enumerate(boxes.splitlines()):
#     if x!=0:
#         b = b.split()
#         print(b)
#         if len(b)==12:
#             x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
#             cv2.rectangle(img, (x,y), (x+w, y+h), (50, 50, 255), 2)
#             cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)


# ### Detecting Words
hImg, wImg,_ = img.shape
cong = r'--oem 1 --psm 6 outputbase digits'
boxes = pytesseract.image_to_data(img,config=cong)
#int minHeight
#print(boxes)
for x,b in enumerate(boxes.splitlines()):
    if x!=0:
        b = b.split()
        print(b)
        if len(b)==12:
            #x is the distance from upper-left corner of the bounding box to the left border of the image.
            # y is the distance from the upper -left corner of the bounding box, to the top border of the image.
            # width and height are the width and height of the bounding box.
            # conf is the model's confidence for the prediction for the word within that bounding box.
            # If conf is -1, that means that the corresponding bounding box contains a block of text, rather than just a single word.
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])

            cv2.rectangle(img, (x,y), (x+w, y+h), (50, 50, 255), 2)
            cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)

#             cv2.imwrite('C:/Users/SatyaTamalampudi/Tymor Marine Ltd/Tymor Marine - Tymor Marine/R&D Development Projects/Draft Marks/Python code/Morphological Operations/Resized Image/Negative1.jpg', img);
##############################################
##### Detecting Words  ######
##############################################



cv2.imshow('output', img)
cv2.waitKey(0)

