#12個のイメージファイルのヒストグラムの比較を行い、表形式で表示
import cv2

#関数の定義
def compare_hist():
  #リストの初期化
    img = [0 for i in range(12)]
    hist = [0 for i in range(12)]
    d = [[0 for i in range(12)] for j in range(12)]
    
    #画像の読み込み
    for i in range(0,11):
        if i<=3:
            img[i] = cv2.imread('food'+str(i+1)+'.jpg')
        else:
            img[i] = cv2.imread('vegetable'+str(i-3)+'.jpg')
    #それぞれのヒストグラムの計算
    for i in range(0,11):
        hist[i] = cv2.calcHist([img[i]],[0],None,[256],[0,256])

    #ヒストグラムの比較
    for i in range(0,11):
        for j in range(0,11):
            d[i][j] = cv2.compareHist(hist[i],hist[j],0)
            print(str(round(d[i][j],4)),end ='  ')
        print('vegetable'+str(i-3)+'.jpg')
#表示
compare_hist()
