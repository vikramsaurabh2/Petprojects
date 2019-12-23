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

class Node:
    value=10
    
    
    def __init__(self,data):
        self.value=data
        self.next=None
        
class linklistops:
    
    def __init__(self,node):
        self.head=node
        
    def insert(self,new_node):
        
        if self.head is None:
            new_node.next=self.head
            self.head=new_node
        
        elif self.head.value > new_node.value:
            new_node.next=self.head
            self.head=new_node
            
        else:
            tmp = self.head
            while tmp.next is not None and tmp.next.value < new_node.value:
                tmp = tmp.next
            new_node.next = tmp.next
            tmp.next = new_node
            
    def printList(self): 
        temp = self.head 
        while(temp): 
            print (temp.value) 
            temp = temp.next