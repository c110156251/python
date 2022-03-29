a=int(input("請輸入X軸座標:"))
b=int(input("請輸入Y軸座標:"))
if a==0 and b==0:
    print("該點位於原點")
elif a>0 and b>0:
    print("該點位於一象限，","離原點距離為根號",(a*a+b*b))
elif a==0 and b>0:
    print("該點位於上半平面Y軸，","離原點距離為根號",(b*b))
elif a<0 and b>0:
    print("該點位於二象限，","離原點距離為根號",(a*a+b*b))
elif a<0 and b==0:
    print("該點位於左半平面X軸，","離原點距離為根號",(a*a))
elif a<0 and b<0:
    print("該點位於三象限，","離原點距離為根號",(a*a+b*b))
elif a==0 and b<0:
    print("該點位於下半平面Y軸，","離原點距離為根號",(b*b))
elif a>0 and b<0:
    print("該點位於四象限，","離原點距離為根號",(a*a+b*b))
else:
    print("該點位於右半平面X軸，","離原點距離為根號",(a*a))