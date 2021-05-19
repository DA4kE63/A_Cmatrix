import random as r


import sys
import os  

import time




print("\033[1;92m")




type = ["Happy Anonymous Cyber Army", " Love You All ", "400 Member Thanks All "]


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
    








            
            
            
            
            
            
            
            
#time.sleep(0.10)

if time.sleep(0.10):
    os.system("clear")




#os.system("clear")
   



