#coding=utf-8
import io
import sys
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
#定义一个类
class CocaCola:
    formula=['caffeine','sugar','water','soda']
    def __init__(self): #魔术方法  实例化的时候会被自动调用，类似构造函数
        self.local_chinalogo='可口可乐'
    def drink(self):  #self这个参数其实就是被创建的实例本身
        print('Energy!')

    def dring(self,how_much):
        if how_much=='a sip':
            print('Cool~')
        elif how_much=='whole bottle':
            print('Headache!')   
coke_for_me=CocaCola()  #类的实例化
coke_for_you=CocaCola()
print(CocaCola.formula)
print(coke_for_me.formula)
print(coke_for_you.formula)

for num, element in enumerate(coke_for_me.formula):
    print(num,'=',element)

coke_for_china=CocaCola()
coke_for_china.local_logo='中国地方的叫法可口可乐' #创建实例属性
print(coke_for_china.local_logo)
coke_for_china.drink()

self=CocaCola
CocaCola.drink(self)

ice_coke=CocaCola()
ice_coke.dring('a sip')

coke=CocaCola()
print(coke.local_chinalogo)

class CocaCola1:
    formula=['caffeine','sugar','water','soda']
    calories=140
    sodium=45
    total_carb=39
    caffeine=34
    ingredients=[
        'High Fructose Corn Syrup',
        'Carbonated Water',
        'Phosphoric Acid',
        'Caramel Color',
        'Caffeine'
    ]
    def __init__(self,logo_name):#类似于构造函数
        self.local_logo=logo_name
    def drink(self):
        print('You got{} cal energy!'.format(self.calories))
coke1=CocaCola1('七喜可乐')
print(coke1.local_logo)
coke1.drink()

class CaffeineFree(CocaCola1): #类的继承
    caffeine=0
    ingredients=[
        'High Fructose Corn Syrup',
        'Carbonated Water',
        'Phosphoric Acid',
        'Natural Flavors',
        'Caramel Color'
    ]
coke_a=CaffeineFree('Cocacola-FREE')
print(coke_a.local_logo)
coke_a.drink()