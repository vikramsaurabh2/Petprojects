'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
#!/usr/bin/env Python
import os
import sys
import math

class SubS:
    strn="zplababz"
    k=3
    
    
    def __init__(self,string,k):
        self.strn=string
        self.k=k 
    
    
    def subtrLong(self):
        start=0
        ln=len(self.strn)
        Final_Str=""
        
        for k in range(0, ln):
           temp=self.strn[start:k+1]
           #print(temp)
           uni= self.unique(temp)
           #print(uni)
           if uni >= self.k:
               Final_Str=temp
               start=start+1
        return Final_Str
        
    def unique(self,string):
        List=[]
        for j in range(0,len(string)):
            List.append(string[j])
        
        uniset=set(List)
        return(len(uniset))
        
            
def main():
    S = SubS("ccaedfggd",4)
    print(S.subtrLong())
    #print St.subtrLong()
    
if __name__=='__main__':
  main()
            
            
            
            