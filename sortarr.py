#!/usr/bin/env python

############################################
# Imports
###########################################
import sys
import os
import math
#import urllib
#import urllib2
#import time
#import httplib2
#from httplib import responses
#import json
#from urllib2 import Request, build_opener, HTTPCookieProcessor, HTTPHandler

__author__ = 'vikram_saurabh vikram.saurabh@gmail.com>'

class sortarr:
  arr = [21,23,34,45,56,57,59,60,0]

  def __init__(self):
    self.arr = [3,7,9,11,18,0]
    self.element = 5

  def insert(self):
    print (self.arr[0])
    self.arr[len(self.arr)-1] = self.element
    print (self.arr[len(self.arr)-1])
    return self.arr
    
  def sort(self,array):
    self.showarr(array)
    if len(array) >1:
        mid = int (math.ceil((len(array)/2)))
        print (mid)
        L = array[:mid]
        R = array[mid:]
        self.sort(L)
        self.sort(R)
        i=j=k=0
        while i < len(L) and j < len(R):
         if L[i]<R[j]:
          array[k]=L[i]
          i=i+1
         else:
          array[k]=R[j]
          j=j+1
         k=k+1
        
        while  i < len(L):
          array[k]=L[i]
          k=k+1
          i=i+1
        
        while  j < len(R):
          array[k]=R[j]
          k=k+1
          j=j+1
    return array
     
  def showarr(self, array):
   print ("---")
   for i in range(len(array)):
     print (array[i])
   print ("---")
     
    


