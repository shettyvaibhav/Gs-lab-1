import cv2

img=cv2.imread('movietalk-despicableme630-jpg_002144.jpg')

(h,w) = img.shape[:2]

H = int(h/2)
W = int(w/2)

for i in range(h):
    for j in range(w):
        if j == W or i == H or j == W-1 or i == H-1:
            img[i,j] = (0,0,0)

name='Split'
cv2.imshow(name,img)
cv2.waitKey(0)
cv2.destroyAllWindows()