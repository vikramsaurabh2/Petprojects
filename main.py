'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
from sortarr import sortarr
def main():
 print ("This is main function")
 global_arr = sortarr()
 #global_arr.arr = [21,23,34,45,56,57,59,60,0]
 global_arr.insert()
 final_array=global_arr.sort(global_arr.arr)
 global_arr.showarr(final_array)

if __name__=='__main__':
  main()
