#coding:utf-8
SX=40;SY=23
S=6
CLIST=["  ","::","::","::"]
import sys,math,time

class Cube:
 def __init__(self):
  self.p=[[-1,-1,-1],[-1,1,-1],[1,1,-1],[1,-1,-1],[-1,-1,1],[-1,1,1],[1,1,1],[1,-1,1]]
  self.graph=[[0 for i in range(SX)] for j in range(SY)]
  sys.stdout.write("\x1b[2J")
  
 def rot(self):
  for i in range(SY):
   for j in range(SX):
    self.graph[i][j]=0
  self.graphpos=[]
  for i in range (len(self.p)):
   x=self.p[i][0];y=self.p[i][1];z=self.p[i][2]
   self.p[i][0]=x*math.cos(self.rad_z)-y*math.sin(self.rad_z)
   self.p[i][1]=x*math.sin(self.rad_z)+y*math.cos(self.rad_z)
   x=self.p[i][0];y=self.p[i][1];z=self.p[i][2]
   self.p[i][1]=y*math.cos(self.rad_x)-z*math.sin(self.rad_x)
   self.p[i][2]=y*math.sin(self.rad_x)+z*math.cos(self.rad_x)
   x=self.p[i][0];y=self.p[i][1];z=self.p[i][2]
   self.p[i][2]=z*math.cos(self.rad_y)-x*math.sin(self.rad_y)
   self.p[i][0]=z*math.sin(self.rad_y)+x*math.cos(self.rad_y)
   self.graph [round(((SY/2)+S*self.p[i][1]))][round(((SX/2)+S*self.p[i][0]))]=1
   self.graphpos.append([round(((SX/2)+S*self.p[i][0])),round(((SY/2)+S*self.p[i][1]))])

  self.draw_line()
   
 def draw_line(self):
  for i in range(12):
   p1=i;p2=i+1
   if p1==3:
    p2=0
   elif p1==7:
    p2=4
   elif p1>=8:
    p1-=8
    p2=p1+4
    
   j=1
   
   p1x=self.graphpos[p1][0];p2x=self.graphpos[p2][0]
   p1y=self.graphpos[p1][1];p2y=self.graphpos[p2][1]
   
   if p1x!=p2x:
    m=(p1y-p2y)/(p1x-p2x)
    if -1<m<1:
     if p1x<p2x:
      while p1x+j!=p2x:
       if self.graph[round(p1y+m*j)][p1x+j]!=1:
        self.graph[round(p1y+m*j)][p1x+j]=2
       j+=1
     else:
      while p2x+j!=p1x:
       if self.graph[round(p2y+m*j)][p2x+j]!=1:
        self.graph[round(p2y+m*j)][p2x+j]=2
       j+=1
       
    else:
     if p1y<p2y:
      while p1y+j!=p2y:
       if self.graph[p1y+j][round(p1x+j/m)]!=1:
        self.graph[p1y+j][round(p1x+j/m)]=2
       j+=1
     else:
      while p2y+j!=p1y:
       if self.graph[p2y+j][round(p2x+j/m)]!=1:
        self.graph[p2y+j][round(p2x+j/m)]=2
       j+=1
   else:
    if p1y>p2y:
     while p2y+j!=p1y:
      self.graph[p2y+j][p2x]=3
      j+=1
    elif p1y<p2y:
     while p1y+j!=p2y:
      self.graph[p1y+j][p1x]=3
      j+=1
      
 def output (self):
  sys.stdout.write("\x1b[H")
  for i in range(SY):
   for j in range(SX):
    sys.stdout.write(CLIST[self.graph[i][j]])
   sys.stdout.write("\n")
   