
"""
题目：
一个多回合制游戏，每个角色都有hp 和power，
hp代表血量，power代表攻击力，hp的初始值为1000，
power的初始值为200。打斗多个回合
定义一个fight方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
谁的hp先为0，那么谁就输了
"""


my_hp = 1000                 #初始化自己血量
enemy_hp = 1000               #初始化敌人血量
my_power = 200                 #初始化自己攻击力
enemy_power = 200               #初始化敌人攻击力

def fight(my_hp,enemy_hp,my_power,enemy_power):
    while True:                                 #开始攻击
        my_hp = my_hp - enemy_power             # 敌方攻击
        enemy_hp = enemy_hp - my_power          # 我放攻击
        if my_hp<=0:                            # 判断我方血量是否小于等于0，
            print("我输了")                     # 我方血量小于等于0，则判断为输
            break
        elif enemy_hp<=0:                       # 判断敌方血量是否小于等于0
            print('我赢了')                     # 敌方血量小于等于0 ，则判断为赢
            break

fight(my_hp,enemy_hp,my_power,enemy_power)      #执行攻击