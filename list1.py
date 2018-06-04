weekday=['Monday','Tuesday','Wednesday','Thursday','Friday']
print(weekday[0])
all_in_list=[
    1, #整数
    1.0, #浮点数
    'a word', #字符串
    print(1),#函数
    True,#布尔值
    [1,2],#列表中套列表
    (1,2),#元组
    {'key':'value'} #字典 
]

fruit=['pineapple','pear']
fruit.insert(1,'grape')  #列表增加，insert方法必须指定在列表中要插入心得元素位置，插入元素的实际位置是在指定位置元素之前的位置，如果指定的位置在列表不存在，实际上也就是超出指定列表长度，那么这个元素一定会被放在列表的最后位置
print(fruit)

fruit[0:0]=['Orange']
print(fruit)

#删除列表中元素的方式使用remove()
fruit=['pinapple','pear','grape']
fruit.remove('grape')
print(fruit)

#如果要替换修改其中的元素
fruit[0]='Grapefruit'
print(fruit)

#删除还有一种方法，那就是使用del关键字来声明
del fruit[0:2]
print(fruit)

print('--------------------------------------')
periodic_table=['H','He','Li','Be','B','C','N','O','F','Ne']
print(periodic_table[0])
print(periodic_table[-2])
print(periodic_table[0:3])
print(periodic_table[-10:-7])
print(periodic_table[-10:])
print(periodic_table[:9])