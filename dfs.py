import copy
blocks=int(input('Total no. of Blocks = '))
s=[['A','B'],['C'],[]]
g=[['C'],['A'],['B']]
# #--------------------------------------------
# print("\n INITIAL STATE\n")

# for i in range(blocks):
#   a=[]
#   print('Elements in Stack',i+1,sep="-", end=" = ")
#   jaadu=int(input())
#   for j in range(jaadu):
#     print('Value for Element',j+1,sep="-", end=" = ")
#     value=input()
#     a.append(value)
#   print("\n ------------ \n")
#   s.append(a)
# #--------------------------------------------
# print("\n GOAL STATE\n")

# for i in range(blocks):
#   a=[]
#   print('Elements in Stack',i+1,sep="-", end=" = ")
#   jaadu=int(input())
#   for j in range(jaadu):
#     print('Value for Element',j+1,sep="-", end=" = ")
#     value=input()
#     a.append(value)
#   print("\n ------------ \n")
#   g.append(a)
# #--------------------------------------------
print("\n =============== \n")
print("INITAIL STATE =",s)
print("GOAL STATE =",g)
print("\n =============== \n")
open=[s]
closed=[]
success=False
#--------------------------------------------
def findStates(current):
    states=[]
    for i in range(len(s)):
      if(len(s[i])!=0):
        for j in range(len(s)):
          if j!=i:
            s1=copy.deepcopy(s)
            x=s1[i].pop(0)
            s1[j].insert(0,x)
            states.append(s1)
          else:
            continue
    return states



if s==g:
  print("Initial State is Goal State itself.")
else:
  while success==False and len(open)!=0:
    current=open.pop(len(open)-1)
    closed.append(current)
    if g==current:
      success=True
    else:
      states=findStates(current)
      print("\nSTATES\n",states)
      for state in states:
        if state not in open and state not in closed:
          open.append(state)
          #print("\nOPEN\n",open)
    if success:
      print('Found')
    else:
      print('Not Found')

