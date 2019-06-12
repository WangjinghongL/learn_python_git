h=input('请输入身高')
h=float(h)**2
w=input('请输入体重')
w=float(w)
hzs=w/h

if hzs>32:
    print('严重肥胖')
elif hzs>28:
    print('肥胖')
elif hzs>25:
    print('过重')
elif hzs>18.5:
    print('正常')
else:
    print('过轻')