class Action:
    def __init__(self):
        pass

    def eat(self):
        print('用嘴吃东西')

    def tell(self):
        print('用嘴说')

    def grab(self):
        print('用手抓')

    def perform(self):
        print('表演')


ac = Action()
ac.perform()
