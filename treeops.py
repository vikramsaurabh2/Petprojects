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
    #value=50
    
    def __init__(self,key):
        self.value=key
        self.right=None
        self.left=None
        
class treeops:
    
    def __init__(self,root):
        self.root=root
        
 
    def insert(self,root,node):
        if root is None:
            root= node
        else:
            if root.value < node.value:
                if (root.right is None):
                    root.right = node
                else:
                    self.insert(root.right,node)
            else:    
                if (root.left is None):
                    root.left = node
                else:
                    self.insert(root.left,node)
                    
    def inorder(self,root): 
     if root: 
        self.inorder(root.left) 
        print(root.value) 
        self.inorder(root.right)                 
    
               
    
        