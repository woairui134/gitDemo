# -*- coding: utf-8 -*-
import random
class timo:
    myhp1 = 100
    enemy_power = 0

    def my_hp(self,myhp1,enemy_power):
        self.myhp1 = myhp1
        self.enemy_power = enemy_power
        myhp = self.myhp1 - self.enemy_power
        return myhp

class police:
    enemy_hp1 = 100
    my_power = 20

    def enemy_hp(self,enemy_hp1,my_power):
        self.enemy_hp1 = enemy_hp1
        self.my_power = my_power
        enemy_hp = self.enemy_hp1 - self.my_power
        return enemy_hp

c = random.randint(1,99)
d = random.randint(1,99)

a = timo()
my_fight=a.my_hp(100,c)

b = police()
enemy_fight = b.enemy_hp(100,d)


if my_fight > enemy_fight:
    my_fight = str(my_fight)
    enemy_fight = str(enemy_fight)
    print("英雄血量：" +my_fight+";"+"敌人血量：" +enemy_fight+";"+" 英雄获胜!")

elif my_fight == enemy_fight:
    print("同归于尽")

else:
    my_fight = str(my_fight)
    enemy_fight = str(enemy_fight)
    print("英雄血量：" +my_fight+";"+"敌人血量：" +enemy_fight+";"+" 敌人获胜!")
