#include headers
import cv2 as cv
import numpy as np
from lot_xml_to_json import xmltojson  # function to convert from xml to json
from json import loads
 
def getLotData(jsonFileName):
    file = open(jsonFileName,'r') #open file for reading
    lotData = loads(file.read()) # load json data as a python object
    
    
    return lotData

def getSpaceCoordinates(lotData):
    spaceCoordinates=[] # contains coordinates for each space
    
    for space in lotData: #loop through all spaces
        #get width and height of each space
        w = int(space['rotatedRect']['size']['w'])
        h = int(space['rotatedRect']['size']['h'])
        spaceCoordinates.append((w,h))
        #get four edges of each lot
        for i in range(4):
            x = int(space['contour']['point'][i]['x'])
            y = int(space['contour']['point'][i]['y'])
            
            spaceCoordinates.append((x,y))
 
    return spaceCoordinates


    

if __name__ == '__main__':
     #xmlFile = '2012-12-16_12_05_07.xml' #get the xml file
     xmlFile = '2012-09-13_10_20_17.xml'
     
     imageFile = '2012-12-16_12_05_07.jpg'
     
     #print(xmlFile[:-3])
     #convert to json
     jsonName= xmlFile[:-3] +"json" #use xml format to name json file
     xmltojson(xmlFile,jsonName )
     
     lotData = getLotData(jsonName)
     spaceCoordinates = getSpaceCoordinates(lotData)
     
     img = cv.imread(imageFile) #read image as cv object
     
     
     
     
     #loop through all the coordinates gotten
     # steps of 4 because each space has five tuples
     for i in range(0,len(spaceCoordinates),5):
         #get edges for the rectangle
         w= spaceCoordinates[i][0]
         h = spaceCoordinates[i][1]
         x1 = spaceCoordinates[i+1][0]
         y1 = spaceCoordinates[i+1][1]
         x2 = spaceCoordinates[i+2][0]
         y2 = spaceCoordinates[i+2][1]
         x3 = spaceCoordinates[i+3][0]
         y3 = spaceCoordinates[i+3][1]
         x4 = spaceCoordinates[i+4][0]
         y4 = spaceCoordinates[i+4][1]
         
         #draw rectangles at locations
         #rectangle = cv.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 1)
         
         
         cropped = img[y2:y2+h, x2:x2+int(w/2)]
         currentSpace = str(int((i+5)/5))
         cv.imwrite("spaces/space"+ currentSpace +".png", cropped)
         
         hist = cv.calcHist([cropped], [0, 1], None, [180, 256], [0, 180, 0, 256])
         np.savetxt('histograms/histogram'+currentSpace+".csv", hist, delimiter=',')
         
        
         
     