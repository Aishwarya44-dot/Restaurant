# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 11:05:53 2020

@author: AISHWARYA
"""

import matplotlib.pyplot as plt


print("*** MENU CARD OF GREEN RESTAUARANT ***")

class Food(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def getprice(self):
        return self.price
    
    def __str__(self):
        return self.name + ' : ' + str(self.getprice())
  
def buildmenu(names, costs):
    menu = []
    for i in range(len(names)):
        menu.append(Food(names[i], costs[i]))
    return menu

names = ['Coffee', 'Tea', 'Pizza', 'Burger', 'Fries']

# prices
costs = [250, 150, 180, 70, 65]

# building food menu
Foods = buildmenu(names, costs)

n = 1
for el in Foods:
    print(n,'. ', el)
    n = n + 1

names = ['Coffee', 'Tea', 'Pizza', 'Chapathi', 'Fries']
height=[5,7,2,10,6]
plt.bar(names,height)
plt.xlabel("ITEMS")
plt.ylabel("RATINGS")

plt.title("GREEN RESTAURANT")
plt.show()



