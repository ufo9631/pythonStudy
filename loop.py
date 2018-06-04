import random  #生成随机数的库
for every_letter in 'Hello world':
    print(every_letter)
    ##----------------end---------------#
print('---------------------------------------')
for num in range(1,11): #不包含11，因此实际范围是1~10
    print(str(num)+'+1=',num+1)
    ##----------------end---------------#
print('---------------------------------------')
#嵌套循环
for i in range(1,10):
    for j in range(1,10):
        print('{}x{}={}'.format(i,j,i*j))
        ##----------------end---------------#
print('---------------------------------------')
count=0
while True:
    print('Repeat this line!')
    count=count+1
    if count==5:
        break
        ##----------------end---------------#
print('---------------------------------------')
a_list=[1,2,3]
print(sum(a_list))
print('---------------------------------------')
point1=random.randrange(1,7)
point2=random.randrange(1,7)
point3=random.randrange(1,7)
print(point1,point2,point3)
  ##----------------end---------------#
def roll_dice(numbers=3,points=None):
    print('<<<< ROLL THE DICE! >>>>')
    if points is None:
        points=[]
    while numbers>0:
        point=random.randrange(1,7)
        points.append(point)
        numbers=numbers-1
    return points    

def roll_result(total):
    isBig=11<=total<=18
    isSmall=3<=total<=10
    if isBig:
        return 'Big'
    elif isSmall:
        return 'Small'

def start_game():
    print('<<<< GAME STARTS! >>>>')
    choices=['Big','Small']
    your_choice=input('Big or Small:')
    if your_choice in choices:
        points=roll_dice()
        total=sum(points)
        youWin=your_choice==roll_result(total)
        if youWin:
            print('The points are',points,'You win!')
        else:
            print('The points are',points,'You lose ！')
    else:
        print('Invalid Words')
        start_game()
start_game()
