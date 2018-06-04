album=[]
album=['Black Star','David Bowie',25,True]
album.append('new song')
print(album[0],album[-1]) #打印列表中的第一个和最后一个元素
print('Black Star' in album) #用in判断元素是否在列表里存在

the_Eddie='Eddie'
name='Eddie'
print(the_Eddie==name)
print(the_Eddie is name)
print('-----------------------------')
print(bool(0))
print(bool([]))
print(bool(''))
print(bool(False))
print(bool(None))
print('-----------------------------')
print('1<3 and 2<5 is {}'.format(1<3 and 2<5))
print('1<3 and 2>5 is {}'.format(1<3 and 2>5))
print('1<3 or 2>5 is {}'.format(1<3 or 2>5))
print('1>3 or 2>5 is {}'.format(1>3 or 2>5))