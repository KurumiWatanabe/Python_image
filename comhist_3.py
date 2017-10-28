import cv2
#RGB三つの観点において、ヒストグラムの比較を行い、一つの値を求める

#画像ファイルの読み込み
im1 = cv2.imread('mell5.jpg')
im2 = cv2.imread('mell4.jpg')
d=0

#rgb　三色分の比較
for i in range(3):
    hist1 = cv2.calcHist([im1],[i],None,[256],[0,256])
    hist2 = cv2.calcHist([im2],[i],None,[256],[0,256])
    #比較値を保管
    d = d + cv2.compareHist(hist1,hist2,0)
#平均値を取る
d = d/3
print(d)
