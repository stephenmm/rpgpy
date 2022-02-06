#!/usr/bin/python3
import random, time, math, pynput, curses
import curses.panel

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
    self.x = 10
    self.y = 10
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

class Game(object):
  def __init__(self):
    
    self.stdscr = curses.initscr()
    curses.start_color()
    curses.use_default_colors()
    curses.noecho()
    curses.curs_set( False )

    curses.init_pair( 1, curses.COLOR_YELLOW, curses.COLOR_GREEN )
    curses.init_pair( 2, curses.COLOR_RED,    curses.COLOR_GREEN )

    self.bgWin = curses.newwin(10,50,1,1)
    self.bgWin.bkgd( '.', curses.color_pair( 1 ) )
    self.bgPnl = curses.panel.new_panel(self.bgWin)

    self.chrWin = curses.newwin(1,1,5,5)
    self.chrWin.bkgd( "@", curses.color_pair( 2 ) )
    self.chrPnl = curses.panel.new_panel( self.chrWin )

    #self.bgWin.addstr(0, 0, "Hello World")
    #self.bgWin.getch()
    #self.
    #self.bgPnl.move(y+1, x)

    curses.panel.update_panels()
    curses.doupdate()

    self.p = Char( "Jack" )
    self.npc = Char( "Luci" )

  #print('Commands: esc-quit a-attack d-defend')
  def on_press(self,key):
     x = self.p.x
     y = self.p.y
     if key == pynput.keyboard.Key.esc:
         return False  # stop listener
     try:
         k = key.char  # single-char keys
     except:
         k = key.name  # other keys
     if k == ' ':
       self.p.attack(self.npc)
       #print(npc)
     if k == 'a': y-=1; self.chrPnl.move(x,y);
     if k == 'd': y+=1; self.chrPnl.move(x,y);
     if k == 's': x+=1; self.chrPnl.move(x,y);
     if k == 'w': x-=1; self.chrPnl.move(x,y);
     self.p.x  =  x
     self.p.y  =  y
     curses.panel.update_panels()
     curses.doupdate()


  def run(self):
    listener = pynput.keyboard.Listener(on_press=self.on_press)
    listener.start()  # start to listen on a separate thread
    listener.join()  # remove if main thread is polling self.keys
    while True:
      time.sleep(1)


#for x in range(10):
#  p.attack(npc)
#  npc.attack(p)

# print('Press s or n to continue:')
# 
# with pynput.keyboard.Events() as events:
#   # Block for as much as possible
#   event = events.get(1e6)
#   if event.key == pynput.keyboard.KeyCode.from_char('s'):
#     print("YES")
#print(p)
#print(npc)




## Run the game
game = Game()
game.run()
