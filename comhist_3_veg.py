import cv2
import numpy as np
from matplotlib import pyplot as plt

def compare_hist(f1,f2):
    #画像をフレイスケールで取得
    im1 = cv2.imread(f1)
    im2 = cv2.imread(f2)
    d = 0.0
    
    #ヒストグラムの計算と基準化(サイズをあわせる) rgb三色分
    for i in range(3):
        hist1 = cv2.calcHist([im1],[i],None,[256],[0,256])
        cv2.normalize(hist1,hist1,0,100,cv2.NORM_MINMAX)
        hist2 = cv2.calcHist([im2],[i],None,[256],[0,256])
        cv2.normalize(hist2,hist2,0,100,cv2.NORM_MINMAX)
        #ヒストグラムの比較を三色分ためる
        d = d + cv2.compareHist(hist1,hist2,0)
    #ヒストグラムの比較の平均値を取る
    d = d/3.0
    return d

if __name__ == "__main__":
    #f1="mell2.jpg"
    #f2="mell3.jpg"
    
    #読み込む画像ファイルの定義
    files=["food1.jpg","food2.jpg","food3.jpg","food4.jpg",
        "vegetable1.jpg","vegetable2.jpg","vegetable3.jpg",
        "vegetable4.jpg","vegetable5.jpg","vegetable6.jpg",
        "vegetable7.jpg","vegetable8.jpg"]

    #print(files)
    #compare_hist(f1,f2)
    #一行目（ラベルの表示）
    for f1 in files:
        print(f1+'\t',end='')
    print()

    #二行目以降
    for f1 in files:
        #print(f)
        print(f1+'\t', end='')
        #結果の表示
        for f2 in files:
            #print(f1+" "+f2)
            #各ヒストグラムの比較の表示
            d=compare_hist(f1,f2)
            #print(f1+"  "+f2 +" : "+format(d))
            print(str(round(d,3))+'\t',end='')
        print()
