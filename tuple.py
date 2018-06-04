#Tuple元组
letters=('a','b','c','d','e','f','g')
print(letters[0])

#集合 Set
a_set={1,2,3,4}
a_set.add(5) #增加
print(a_set) 
a_set.discard(5)#删除
print(a_set)

mun_list=[6,8,1,5,9,7]
print(sorted(mun_list))  #排序
print(sorted(mun_list,reverse=True))

#循环两个集合zip
str=['six','eight','one','five','nine','seleven']
for a,b in zip(mun_list,str):
    print(a,'is',b)

#10个元素装进列表
a=[]
for i in range(1,11):
    a.append(i)
print(a)
#list的推导式
b=[i for i in range(1,11)]
print(b)

a=[i**2 for i in range(1,10)]
print(a)
b=[j+1 for j in range(1,10)]
print(b)
c=[n for n in range(1,10) if n%2==0]
print(c)
d=[letter.lower() for letter in 'ABCDEFGHIJKLMN']
print(d)

#字典推导式，字典必须满足key唯一
e={i:i+1 for i in range(4)}
print(e)
f={i:j for i,j in zip(range(1,6),'abcde')}
print(f)
g={i:j.upper() for i,j in zip(range(1,6),'abcde')}
print(g)

#循环列表获取元素的索引\
letters=['a','b','c','d','e','f','g']
for num,letter in enumerate(letters):
    print(letter,'is',num+1)

