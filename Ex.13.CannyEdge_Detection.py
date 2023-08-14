import cv2
path = "C:Downloads\srees\Programs\Sample8.jpg"
img =cv2.imread(path)
t_upper=50
t_lower=150
imgCanny = cv2.Canny(img,t_upper,t_lower)
cv2.imwrite("Output13(CannyEdge).jpg",imgCanny)
cv2.waitKey(0)
cv2.destroyAllWindows()
