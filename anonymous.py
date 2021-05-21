






import random as r


import sys
import os  

import time


#sorry for my bad english

#print("\033[1;92m")


im = input("enter your choice /red/blue/green/white/")



if im =="red":
    print("\033[1;91m")
elif im == "green":
    print("\033[1;92m")
elif im == "blue":
    print("\033[1;94m")
elif im == "white":
    print("\033[1;97m")

i1 = input("please enter your cmatrix efect name ")

ih = input("if you want more name add yes enter [ bro please yes and its requird for cmatrix ]")

if ih == "yes":
    
    i2 = input("enter your cmatrix 2nd Cmatrix  efects name ")

    i3 = input("please enter your cmatrix  efects name ")
else :
    
    print("no problem start cmatrix efects ")
    

type = [i1, i2, i3]







counter =0
line=[]

for i in range(110):
    x = r.randint(0,2)
    line.append(type[x])






counter +=1


for i in range(10000):
    




    if counter % 5==0:
        r_type=[ r.randint(0,117) for i in range(10)]
        
        for i in r_type :
            line[1]= type[r.randint(0,2)]
    print(*line)
    counter+=1
    time.sleep(0.02)
    








            
            
            
            
            
"""           
            
            
#time.sleep(0.10)

if time.sleep(0.10):
    os.system("clear")




#os.system("clear")
   

"""

