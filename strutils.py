name='My name is Mik'
print(name[0])
print(name[-4])
print(name[11:14]) #截取的编号从第11个字符开始，到位置14但不包含14
print(name[11:15])
print(name[5:]) #从编号为5的字符到结束
print(name[:5]) #从0的字符开始到编号为5但不包含第5个字符

word='friends'
find_the_evil_in_your_friends=word[0]+word[2:4]+word[-3:-1]
print(find_the_evil_in_your_friends)