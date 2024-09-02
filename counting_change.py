bills =[5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]
count5 = 0
count10 = 0
count20 = 0
for item in bills:
    if item == 5:
        count5 += 1
    elif item == 10:
        count10 += 1
        count5 -= 1
    elif item == 20:
        count20 += 1
        if count10 == 0:
            count5 -= 3
        else:
            count10 -= 1
            count5 -= 1
    if any([count5<0,count10<0,count20<0]):
        print(False)
        print(count5,count10,count20)
        break
else:
    print(True)
    print(count5,count10,count20)