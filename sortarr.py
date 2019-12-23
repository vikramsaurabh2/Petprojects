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
    self.arr = [3,7,9,11,18,24]
    self.element = 2

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
    
  def sort_sorted(self,array):
        i=0 
        j=-1
        k=0
        while i < len(array):
            if self.element < array[i]:
                j=i
                break
            i=i+1
        if j ==0:
            array = [self.element] + array[0:(len(array)-1)]
            L = [array[j]]
        elif j==-1:
            array = array[1:(len(array))] + [self.element]
        else:
            k=j+1
            while k < len(array):
             array[len(array)-1-(k-j-1)]=array[len(array)-2-(k-j-1)]
             k=k+1
            array[j]=self.element
        
        return array
        
  def bubble_sort(self,array):
      i=0
      while i < len(array):
        j=0
        print (i)
        print ("-----")
        while j < len(array)-1-i:
            if array[j] > array[j+1]:
               array[j] = array[j+1]+array[j]
               array[j+1] = array[j]-array[j+1]
               array[j] = array[j]-array[j+1]
            print (j) 
            print ("====")
            j=j+1
        i=i+1
      return array

  def reverse(self,array):
      i=0
      while i < len(array):
        j=0
        tmp=array[j]
        while j < len(array)-i-1:
            array[j]=array[j+1]
            j=j+1
        array[len(array)-i-1]=tmp
        i=i+1
      return array
     
  def showarr(self, array):
   print ("---")
   for i in range(len(array)):
     print (array[i])
   print ("---")
     
    


