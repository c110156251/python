a=int(input("請輸入西元年:"))
b=("鼠牛虎兔龍蛇馬羊猴雞狗豬")
c=(a-3)%12
if c == 1:
    print(b[0],"年")
elif c == 2:
    print(b[1],"年")
elif c == 3:
    print(b[2],"年")
elif c == 4:
    print(b[3],"年")
elif c == 5:
    print(b[4],"年")
elif c == 6:
    print(b[5],"年")
elif c == 7:
    print(b[6],"年")
elif c == 8:
    print(b[7],"年")
elif c == 9:
    print(b[8],"年")
elif c == 10:
    print(b[9],"年")
elif c == 11:
    print(b[10],"年")
else:
    print(b[11],"年")