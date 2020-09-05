class Animal:
    def __init__(self, weight, age, name):
        self.weight = weight
        self.age = age
        self.name = name

    def infomation(self):
        print(f'这是一只{self.name},重{self.weight}斤,{self.age}岁')

    def eat(self):
        print(f'{self.name}吃东西')

    def play(self):
        print(f'{self.name}玩耍')


cat = Animal(10, 1, '小猫')
cat.eat()
cat.play()
dog =Animal(20,1,'小狗')
dog.play()