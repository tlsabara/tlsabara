# -*- coding: utf-8 -*-
"""
by Tlsabará
"""
class Human:
    def __init__(self, name):
        self.alive = True
        self.name = name
        self.hungry = 100
        self.energy = 50
        self.drams = False
        self.intelligence = 120
        self.to_do = 'eat, sleep, code, repeat'
        
    def eat(self):
        self.hungry = 0
        self.energy = 100
        return 'Done'
    
    def sleep(self):
        self.dreams = True
        self.energy = 100
        return 'Awake'
    
    def code(self):
        self.intelligence += 10
        self.energy = 10
        self.hungry = 100
        
    def repeat(self):
        self.to_do = 'new tasks'
    


me = Human('tlsabara')

while me.alive == True:
    me.code()
    me.eat()
    me.sleep()
    me.repeat()
