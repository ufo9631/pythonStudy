NASDAQ_code={
    'BIDU':'Baidu',
    'SINA':'Sina'
}
#字典的增删改查
NASDAQ_code['Youku']='youku'
print(NASDAQ_code)

#添加多个元素update
NASDAQ_code.update({'FB':'facebook','TSLA':'Tesla'})
print(NASDAQ_code)
#删除元素
del NASDAQ_code['FB']
print(NASDAQ_code)
#索引
print(NASDAQ_code['Youku'])
