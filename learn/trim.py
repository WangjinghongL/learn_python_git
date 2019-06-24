def trim(s):
    if(len(s)!=0):
       while s[:1]==' ':
           s=s[1:]
       while s[-1:]==' ':
           s=s[:-1]
    else:
        print("不可能!")
    return s




print(trim("    Hello,begin00"))

print(trim('Hello ,end  !     '))