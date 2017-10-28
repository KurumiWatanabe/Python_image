import numpy as np
import cv2

img = cv2.imread('mell2.jpg') #画像の読み込み

cv2.imshow('mell', img) #画像を開いて
cv2.waitKey(0) #何かしらのkey入力を待つ
cv2.destroyAllWindows() #画像を閉じる
