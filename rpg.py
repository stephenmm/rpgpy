#!/usr/bin/python3
import random, time, math

class Item(object):
  def __init__(self,name):
    self.name = name
    self.val = 0.0

class Weapon(Item):
  def __init__(self,name,atk_pts,val):
    Item.__init__(self,name)
    self.type = ''
    self.atk_pts = atk_pts
    self.val = val

class Char(object):
  def __init__(self,name,create="random"):
    self.name = name
    self.max_hp = 0.0
    self.hp = 0.0
    self.str = 0.0
    #self.agi = 0.0
    #self.dex = 0.0
    self.armor = 0.0
    self.xp = 0.0
    self.melee = Weapon( 'hands', 1.0, 0.0 )
    if( create == "random" ):
      self.max_hp = random.uniform(80.0,120.0)
      self.hp = self.max_hp
      self.str = random.uniform(8.0,12.0)
      #self.agi = random.uniform(8.0,12.0)
      #self.dex = random.uniform(8.0,12.0)
  def __repr__(self):
    return "%s(%r)" % (self.__class__, self.__dict__)
  def attack(self,opp,type='melee'):
    hp_dmg = 0
    if( type == 'melee' ):
      hp_dmg = ( self.melee.atk_pts * random.uniform(0.8,1.2) ) - opp.armor
    self.xp += hp_dmg
    opp.hp = opp.hp - hp_dmg
    print("%s strikes %s with %s for %f dmg and %s has %f HP left" % ( self.name, opp.name, self.melee.name, hp_dmg, opp.name, opp.hp ))

p = Char( "Jack" )
npc = Char( "Luci" )

for x in range(10):
  p.attack(npc)
  npc.attack(p)


print(p)
print(npc)





