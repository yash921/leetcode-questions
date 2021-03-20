#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 20:17:09 2020

@author: yash
"""

class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None
    def viewList(self):
        if self.start == None:
            print("List is empty!!")
        else:
            temp = self.start
            while temp != None:
                print(temp.data, end=" ")
                temp = temp.next
    def deleteFirstNode(self):
        if self.start == None:
            print("Linkedlist is Empty!!!")
        else:
            self.start = self.start.next
    def insertLast(self, value):
        newNode = node(value)
        if self.start == None:
            self.start = newNode
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = newNode
            
mylist = LinkedList()
mylist.insertLast(10)
mylist.insertLast(20)
mylist.insertLast(30)
mylist.insertLast(40)
mylist.insertLast(50)
mylist.viewList()
print()
mylist.deleteFirstNode()
mylist.viewList()

    
                