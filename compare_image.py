##二つのjpgをヒストグラムで比較する
import cv2

#二つ目の引数　０＝グレースケール
#            なし＝カラーで比較
#im1 = cv2.imread('mell2.jpg',0)
im1 = cv2.imread('mell2.jpg')
#im2 = cv2.imread('mell5.jpg',0)
im2 = cv2.imread('mell5.jpg',0)

hist1 = cv2.calcHist([im1],[0],None,[256],[0,256])
hist2 = cv2.calcHist([im2],[0],None,[256],[0,256])

d = cv2.compareHist(hist1,hist2,0)
print(d)

#１に近いと類似している
#値が小さいほど似ていない
