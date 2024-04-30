# BEST FIRST SEARCH ALGORITHM

s=[[2,0,3],[1,8,4],[7,6,5]]
g=[[1,2,3],[8,0,4],[7,6,5]]
open=[s]
closed=[]
finish=False

def left(i,j, current):
  if j>0:
    current[i][j]=current[i][j-1]
    current[i][j-1]=0
    return current
  else:
    return -1

def right(i,j, current):
  if j<len(current)-1:
    current[i][j]=current[i][j+1]
    current[i][j+1]=0
    return current
  else:
    return -1

def up(i,j, current):
  if i>0:
    current[i][j]=current[i][j+1]
    current[i][j+1]=0
    return current
  else:
    return -1

def down(i,j, current):
  if i<len(current)-1:
    current[i][j]=current[i][j+1]
    current[i][j+1]=0
    return current
  else:
    return -1


def heuristic(current):
  val=0
  global g
  for i in range(len(s)):
    for j in range(len(s)):
      if s[i][j]!=g[i][j] and s[i][j]!=0:
        val=val+1
  return val

while finish==False and len(open)!=0:
  location=[0,0]
  current=open.pop(0)
  closed.append(current)
  if current==g:
    finish=True
  else:
    current_heur=heuristic(current)
    for i in range (len(current)):
      for j in range (len(current)):
        if(current[i][j]==0):
          location=[i,j]
          break;
    left_cur=left(location[0],location[1],current)
    right_cur=right(location[0],location[1],current)
    up_cur=up(location[0],location[1],current)
    down_cur=down(location[0],location[1],current)
    heuristic_val=[1000,1000,1000,1000]
    if(left_cur!=-1):
      heuristic_val[0]=int(heuristic(left_cur))
      print(heuristic_val[0])
    if(right_cur!=-1):
      heuristic_val[1]=int(heuristic(right_cur))
    if(up_cur!=-1):
      heuristic_val[2]=int(heuristic(up_cur))
    if(down_cur!=-1):
      heuristic_val[3]=int(heuristic(down_cur))
    min_val=min(heuristic_val)
    min_index=heuristic_val.index(min_val)
    if min_val>=current_heur:
      break;
    else:
      if min_index==0:
        open.append(left_cur)
      elif min_index==1:
        open.append(right_cur)
      elif min_index==2:
        open.append(up_cur)
      elif(min_index==3):
        open.append(down_cur)
if finish==True:
  print("FOUND. Path Followed:")
else:
  print("NOT FOUND. Path Followed:")
print(closed)
