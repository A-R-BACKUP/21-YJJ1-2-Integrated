pcl = 3000
pen = 4000
numPencil = input('연필 개수 입력: ')
numPen = input('펜 개수 입력: ')
wari = (((pcl * numPencil) + (pen * numPen)) * 0.3)
totalPrice = (((pcl * numPencil) + (pen * numPen)) - wari)
print('총 가격은' + totalPrice + '원입니다.')