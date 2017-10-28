import cv2

def compare_hist(f1,f2):
    #画像をフレイスケールで取得
    im1 = cv2.imread(f1,0)
    im2 = cv2.imread(f2,0)
    #ヒストグラムの計算
    #二つ目の引数　RGB [0][1][2]
    #三つ目の引数　RGB 256階調
    #四つ目の引数　RGB 0から256
    hist1 = cv2.calcHist([im1],[0],None,[256],[0,256])
    hist2 = cv2.calcHist([im2],[0],None,[256],[0,256])
    
    #ヒストグラムの類似度を計算
    d = cv2.compareHist(hist1,hist2,0)
    #print(d)
    return d

if __name__ == "__main__":
    #f1="mell2.jpg"
    #f2="mell3.jpg"
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
            d=compare_hist(f1,f2)
            #print(f1+"  "+f2 +" : "+format(d))
            print(str(round(d,3))+'\t',end='')
        print()
