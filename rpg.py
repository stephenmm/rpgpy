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


# curses windows and panel setup
x=5
y=5

stdscr = curses.initscr()
curses.start_color()
curses.use_default_colors()
curses.noecho()
curses.curs_set( False )

curses.init_pair( 1, curses.COLOR_YELLOW, curses.COLOR_GREEN )
curses.init_pair( 2, curses.COLOR_RED,    curses.COLOR_GREEN )

bgWin = curses.newwin(10,50,1,1)
bgWin.bkgd( '.', curses.color_pair( 1 ) )
bgPnl = curses.panel.new_panel(bgWin)

chrWin = curses.newwin(1,1,5,5)
chrWin.bkgd( "@", curses.color_pair( 2 ) )
chrPnl = curses.panel.new_panel( chrWin )

#bgWin.addstr(0, 0, "Hello World")
#bgWin.getch()
#
#bgPnl.move(y+1, x)

curses.panel.update_panels()
curses.doupdate()


p = Char( "Jack" )
npc = Char( "Luci" )

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

#print('Commands: esc-quit a-attack d-defend')
def on_press(key):
   global x, y
   if key == pynput.keyboard.Key.esc:
       return False  # stop listener
   try:
       k = key.char  # single-char keys
   except:
       k = key.name  # other keys
   if k == ' ':
     p.attack(npc)
     #print(npc)
   if k == 'a': y-=1; chrPnl.move(x,y);
   if k == 'd': y+=1; chrPnl.move(x,y);
   if k == 's': x+=1; chrPnl.move(x,y);
   if k == 'w': x-=1; chrPnl.move(x,y);
   curses.panel.update_panels()
   curses.doupdate()

listener = pynput.keyboard.Listener(on_press=on_press)
listener.start()  # start to listen on a separate thread
listener.join()  # remove if main thread is polling self.keys

#print(p)
#print(npc)




## Run the game
#game = Game(board_num_rows=16, board_num_columns=10)
#game.main_loop()
