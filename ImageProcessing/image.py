import cv2
import numpy as np

img = cv2.imread('sample.jpg')
rows, cols = img.shape[:2]
print "enter pivot point and scale:"
x = int(raw_input())
y = int(raw_input())
scale = float(raw_input())

#problem statement 1

src_points = np.float32([[0,0], [cols-1,0], [0,rows-1]])
dst_points = np.float32([[0,0], [int(0.6*(cols-1)),0], [int(0.4*(cols-1)),rows-1]])
affine_matrix = cv2.getAffineTransform(src_points, dst_points)
img_output = cv2.warpAffine(img, affine_matrix, (cols,rows))



#problem statement 2

if(x-(rows/2*scale)) < 0:
	x = rows/2
elif (x + rows/(2*scale)) > rows:
	x = rows/2
if (y-cols/(2*scale)) < 0:
	y = cols/2
elif (y + cols/(2*scale)) > cols:
	y = cols/2


new_img = np.ones((rows,cols,3))
for k in range(3):
	for i in range((-1*rows/2),rows/2):
		for j in range((-1*cols/2), cols/2):
			#print k,i,j,y+j,int(round(y+j/scale)),x+i,int(round(x+i/scale)),np.shape(img)
			new_img[(rows/2)+i][(cols/2)+j][k] = float(img[int(round(x+i/scale))][int(round(y+j/scale))][k])/256;

cv2.imshow('Input', img)
cv2.imshow('Output', img_output)
cv2.imshow("out",new_img)

cv2.waitKey()