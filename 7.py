a=int(input("請輸入月租費型式:"))
b=int(input("請輸入通話時間:"))

if a ==186:
    c=b*0.09
    if c<=186:
        print("通話費為:186")
    elif c>186:
        if c>186*2:
            print("通話費為:",round(c*0.9))
        elif c<386*2:
            print("通話費為:",round(c*0.8))
elif a==386:
    c=b*0.08
    if c<=386:
        print("通話費為:386")
    elif c>386:
        if c>386*2:
            print("通話費為:",round(c*0.7))
        elif c<386*2:
            print("通話費為:",round(c*0.8))
elif a==586:
    c=b*0.07
    if c<=586:
        print("通話費為:386")
    elif c>586:
        if c>386*2:
            print("通話費為:",round(c*0.7))
        elif c<386*2:
            print("通話費為:",round(c*0.8))