import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys

#キーボード入力
args = sys.argv
#イメージの読み込み
img = cv2.imread(args[1])

#色の定義
color = ('b','g','r')

#三色に対して行う
for i,col in enumerate(color):
    #ヒストグラム取得
    chist = cv2.calcHist([img],[i],None,[256],[0,256])
    #基準化(サイズを合わせる）
    cv2.normalize(chist,chist,0,100,cv2.NORM_MINMAX)
    #ヒストグラムの表を表示
    plt.plot(chist,color = col)
    plt.xlim([0,256])
plt.show()
