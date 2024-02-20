'''
welcome to game
input name
tells you how to access inv and stats
you first enter a shop and choose an item
sword, armor, ...
leave shop, choose path
each path requires specific item from shop
be able to retreat back to shop
restores health
and able to pick another item and path
must complete all 3 paths to beat game
'''
import sys

SWORD_DAMAGE = 3
    
class character():
    name = "player's name"
    health = 5
    lvl = 1
    inv = []
    gold = 0
    def __init__(self, newName):
        self.name = newName
    def lvlUp(self,):
        self.lvl = self.lvl + 1
    def takeDamage(self, points):
        self.health = self.health - points
        if self.health < 1:
            print("You died, Game Over.")
            sys.exit()
    def takeItem(self, addItem):
        self.inv.append(addItem)
        print(f"{addItem} was added to your inventory.")
    def changeGold(self, addGold, loseGold):
        self.gold = self.gold + addGold
        if addGold > 0:
            print(f"You found {addGold} gold!")
        self.gold = self.gold - loseGold
        if loseGold > 0:
            print(f"You used {loseGold} gold.")
    def attack(self):
        if "sword" in self.inv:
            return SWORD_DAMAGE
        else:
            return 1

class shop():
    shopInv = ["sword", "armor"]
    def talkShop(self):
        print("You enter the shop.")
        if "sword" in self.shopInv and "armor" in self.shopInv:
            print('The shop owner says, "Welcome to my shop."')
            print('"The sword is 100 gold and the armor is 1 gold."')
            print("You may leave the shop at any time by typing 'leave shop'.")
            shopPurchase = shop()
            shopPurchase.purchase()
        elif "armor" in self.shopInv:
            print('The shop owner says, "Welcome to my shop."')
            print(f'"I have {self.shopInv}"')
            print('"It is 1 gold."')
            print("You may leave the shop at any time by typing 'leave shop'.")
            shopPurchase = shop()
            shopPurchase.purchase()
        elif "armor" not in self.shopInv and "sword" not in self.shopInv:
            print('The shop owner screams, "I dont have anything left!" and kicks you out.')
            print("You leave the shop.")
    def purchase(self):
        buyItem = input('"What would you like to buy?"  ')
        if buyItem in self.shopInv and player.gold < 1:
            print("Sorry you don't have enough for that.")
            enterShop.purchase()
        elif buyItem == "armor" and player.gold > 0:
            self.shopInv.remove(buyItem)
            print(f"{player.name} took the {buyItem}.")
            player.takeItem(buyItem)
            player.changeGold(0,1)
        elif buyItem in self.shopInv:
            self.shopInv.remove(buyItem)
            print(f"{player.name} took the {buyItem}.")
            player.takeItem(buyItem)
        
        elif buyItem == "leave shop":
            if "sword" in self.shopInv:
                print("You go to leave and the shop owner stops you.")
                print('He says, "Its dangerous to go alone! Take this."')
                self.shopInv.remove("sword") #not sure if there's a better way to do this
                player.takeItem("sword")
                print("You leave the shop.")
            else:
                print("You leave the shop.")
        else:
            print('"Sorry we dont have that."')
            enterShop.purchase()


class enemy():
    
    def __init__(self, enemyMaxHealth, enemyName):
        self.enemyHealth = enemyMaxHealth
        self.enemyName = enemyName
    def attackEnemy(self, points):
        self.enemyHealth = self.enemyHealth - points
            
class imp(enemy):
    def __init__(self):
        self.enemyHealth = 5
        self.enemyName = "imp"
        self.damage = 2
                    
class troll(enemy):
    def __init__(self):
        self.enemyHealth = 10
        self.enemyName = "troll"
        self.damage = 4
        

class cave():
    def __init__(self, character):
        self.player = character
    def encounterEnemy(self):
        mob = imp()
        print(f"You encounter a {mob.enemyName}.")
        print(f"The {mob.enemyName}'s hp is at {mob.enemyHealth}.")
        while mob.enemyHealth > 0:
            action = input("Do you fight or run?  ")
            if action == "fight":
                damage = self.player.attack()
                mob.attackEnemy(damage)
                self.player.takeDamage(mob.damage)
                print(f"You deal {damage} damage to the {mob.enemyName} and it deals {mob.damage} to you.")
                print(f"The {mob.enemyName}'s is at {mob.enemyHealth}.")
                
            elif action == "run":
                print("You flee the cave.")
                outside(player)
            elif action == "open menu":
                menu(player)
        self.player.lvlUp()
        print(f"You've defeated the {mob.enemyName}.")
        print("You leveled up!")
        self.player.changeGold(1,0)
        while action != "leave cave":
            action = input("What do you do?  ")
            if action == "leave cave":
                break

def menu(player):
    action = input("check stats or check inventory?  ")
    if action == "check stats":
        print(f"{player.name}'s hp and level are at {player.health} and {player.lvl}.")
    if action == "check inventory":
        print(f"You have {player.inv} and {player.gold} gold.")
    
def outside(player):
    while True:
        print("There is a shop and cave, you may open menu to check inventory or stats.")
        action = input("What do you do?  ")
        if action == "open menu":
            menu(player)
        elif action == "enter shop":
            player.health = 5
            print(player.name + "'s hp is now 5.")
            enterShop = shop()
            enterShop.talkShop()
        elif action == "enter cave":
            enterCave = cave(player)
            print("You enter the cave and can go left or right.")
            dir = input("Which way do you go?  ")
            if dir == "left":
                enterCave.encounterEnemy()
            elif dir == "right":
                pass

def startGame():
    print("Welcome to the game.")
    name = input("What's your name?  ")
    player = character(name)
    print(player.name)
    outside(player)