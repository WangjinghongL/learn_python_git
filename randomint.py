
#一个简单的程序
import random

print("...进入猜数字游戏，您有20次机会...")
chance=0
randint=random.randint(0,10000)
boo=False
while chance<=20:
    instr=input("请输入您猜的数字：")
    innum=int(instr)
    if innum>randint:
        print("您猜的数字有点大。")
    elif innum<randint:
        print("您猜的数字有点小。")
    else:
        print("恭喜您，猜对了！！！")
        boo=True
        break
    chance=chance+1
    print(">>>>>>>>>>>>")
    print("您还有",20-chance,"次机会")
if boo:
    print("✿✿ヽ(°▽°)ノ✿")
else:
    print("很遗憾，没有机会了。。。。。正确答案为：",randint)
    