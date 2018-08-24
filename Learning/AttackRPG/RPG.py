'''
RPG Attack 
class + initializing objects 
'''
import random

class Enemy:
    hp = 200 #static var
    def __init__(self, atk_low, atk_high):
        self.atk_low = atk_low
        self.atk_high = atk_high


    def getAtk(self):
        print("atk is", self.atk_low) #similiar to this in JS

    def getHp(self):
        print("HP is", self.hp)

enemy1 = Enemy(40,49)
enemy1.getAtk()
enemy1.getHp()

enemy2 = Enemy(75,90)
enemy2.getAtk()
enemy2.getHp()



playerhp = 260
enemyatk_low = 60
enemyatk_high = 80

while playerhp > 0 : 
    dmg = random.randrange(enemyatk_low, enemyatk_high)
    playerhp = playerhp - dmg 

    if playerhp <= 30:
        playerhp = 30

    print('enemy strikes for', dmg, 'points of dmg.  Current HP is', playerhp)
    
    if playerhp > 30:
            continue
    print("You have low health so you were sent to the inn to get more health")
    break
