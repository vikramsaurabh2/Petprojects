'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
from linklist import Node
from linklist import linklistops



def main():
 print ("This is main function")
 list = linklistops(Node(5))
 list.insert(Node(10))
 list.insert(Node(1))
 list.printList()
 
 

if __name__=='__main__':
  main()
