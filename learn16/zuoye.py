
# 课后作业二进制函数
def dsbs(num):
    res=''
    while num>0:
        yu=num%2
        num=int(num/2)
        res=str(yu)+res
    return str(res)

print(dsbs(111))
