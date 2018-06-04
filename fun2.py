file=open('G://PythonTs/text.txt','w')
file.write('Hello world')

def text_create(name,msg):
    file_path="G://PythonTs/"
    full_path=file_path+name+'.txt'
    file=open(full_path,'w') #w参数代表作为写入模式，意思是：如果没有就在该路径创建一个该名称文本，有则追加覆盖文本内容
    file.write(msg)
    file.close()
    print('Done')

text_create('hello','Hello world') #调用函数

def text_filter(word,censored_word='Lame',changed_word='Awesome'):
    return word.replace(censored_word,changed_word)
print(text_filter("Python is Lame!"))

def censored_text_create(name,msg):
    clean_msg=text_filter(msg)
    text_create(name,clean_msg)
censored_text_create('Try','Lame!Lame!Lame') #调用函数
