import cv2
import numpy as np

def GUC():
    img = cv2.imread('GUC.png', cv2.IMREAD_COLOR)
    cv2.imshow('GUC image',img)

    img1 = (img//2)

    cv2.imwrite('GUCDim.png',img1)
    cv2.imshow('GUC image after dimming',img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def calculator():
    img = cv2.imread('calculator.png', cv2.IMREAD_COLOR)
    cv2.imshow('calculator image',img)

    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            if np.any(img[i,j] >= [180,180,180]):
                img[i,j] = [180,180,180]

    cv2.imwrite('calcAfterModification.png',img)
    cv2.imshow('Calculator image after modification' , img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def cameraman():
    img = cv2.imread('cameraman.png',cv2.IMREAD_COLOR)
    cv2.imshow('cameraman',img)

    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            if np.any(img[i,j] <= [20,20,20]):
                img[i,j] = img[i,j]*4

    cv2.imwrite('cameramanModified.png',img)
    cv2.imshow('cameraman image after modification', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def lake():
    img = cv2.imread('lake.png',cv2.IMREAD_COLOR)
    cv2.imshow('lake',img)

    kernel = np.ones((5,5),np.uint8)
    edges = cv2.Canny(img,150,100)
    dilation = cv2.dilate(edges,kernel,iterations = 1)

    for i in range(0,dilation.shape[0]):
        for j in range(0,dilation.shape[1]):
            if np.any(dilation[i,j] >= 220):
                dilation[i,j] = img[i,j,0]

    cv2.imwrite('lakeModification.png',dilation)
    cv2.imshow('lake image after modification',dilation)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def jamesShifted():
    img = cv2.imread('james.png',cv2.IMREAD_COLOR)
    img1 = cv2.imread('london1.png',cv2.IMREAD_COLOR)

    M = np.float32([[1,0,-200],[0,1,0]])
    img2 = cv2.warpAffine(img,M,(img.shape[1],img.shape[0]))

    for i in range(0,img2.shape[0]):
        for j in range(1000,img2.shape[1]):
            if np.any(img2[i,j] == [0,0,0]):
                img2[i,j] = [255,255,255]

    for i in range(0,img2.shape[0]):
        for j in range(0,img2.shape[1]):
            if np.any(img2[i,j] >= [235,235,235]):
                img2[i,j] = img1[i,j]

    cv2.imwrite('jamesAndLondonShifted.png',img2)
    cv2.imshow('James and London shifted image after modification', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def jamesFlipped():
    img = cv2.imread('james.png',cv2.IMREAD_COLOR)
    img1 = cv2.imread('london2.png',cv2.IMREAD_COLOR)

    img2 = cv2.flip(img,1)
    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            if np.any(img2[i,j] >= [235,235,235]):
                img2[i,j] = img1[i,j]

    cv2.imwrite('jamesAndLondonFlipped.png',img2)
    cv2.imshow('James and London flipped image after modification',img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



# GUC()
# calculator()
# cameraman()
# lake()
# jamesShifted()
jamesFlipped()