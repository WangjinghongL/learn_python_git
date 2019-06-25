def trim(s):
    if len(s)!=0:
       while s[:1]==' ':
           s=s[1:]
       while s[-1:]==' ':
           s=s[:-1]
    else:
        print("不可能!")
    return s


def trims(s):
    if len(s) !=0:
        res=''
        for chr in s:
            if chr!=' ':
                res=res+chr
    return res




print(trim("    Hello,begin00"))

print(trim('Hello ,end  !     '))

print(trims("sdfsdf  uohoenx  我活 ！！！     "))