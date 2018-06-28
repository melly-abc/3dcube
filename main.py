#coding:utf-8

WAIT=0.05

import sys,math,time
import tty,termios
import cube

class Main:
 def __init__(self):
  self.cube=cube.Cube()
  self.cube.rad_z=0;self.cube.rad_x=0;self.cube.rad_y=0
  self.mode=1
 def run (self):
  i=0
  while 1 :
   self.cube.rot()
   self.cube.output()
   if len(sys.argv)>1 and sys.argv[1]=="-i" :
    self.input()
   else:
    self.cube.rad_z=0;self.cube.rad_x=0;self.cube.rad_y=0.1
    self.cube.rad_x=0.05*math.cos(i*0.05)
   i+=1
   time.sleep(WAIT)

 def input(self):
  self.getch()
  if self.key==27:
   sys.exit()
  sys.stdout.write(str(self.key))
  self.cube.rad_z=0;self.cube.rad_x=0;self.cube.rad_y=0
  if self.key==97:
   self.cube.rad_y=0.1
  if self.key==100:
   self.cube.rad_y=-0.1
  if self.key==115:
   self.cube.rad_x=0.1
  if self.key==119:
   self.cube.rad_x=-0.1
  if self.key==65:
   self.cube.rad_z=0.1
  if self.key==68:
   self.cube.rad_z=-0.1

 def getch(self):
  f = sys.stdin.fileno()
  save = termios.tcgetattr(f)
  try:
   tty.setraw(f)
   self.key=ord( sys.stdin.read(1))
  finally:
   termios.tcsetattr(f, termios.TCSADRAIN, save)

if __name__ == "__main__":
 Main().run()
