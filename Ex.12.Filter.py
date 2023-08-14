import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
path="C:Downloads\srees\Programs\Sample3.jpg"
image=cv.imread(path)
kernel1=np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
filter1=cv.filter2D(src=image,ddepth=-1,kernel=kernel1)
cv.imwrite('Output12(filter).jpg',filter1)
cv.destroyAllWindows()
