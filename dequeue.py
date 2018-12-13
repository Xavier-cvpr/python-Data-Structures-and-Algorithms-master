# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 18:25:22 2018

@author: Xavier
"""

class Deque(object):
  #双端队列
    def __init__(self):
        #构造函数胡
        self.__list=[]
            
    def add_front(self,item):
        #头部添加一个item元素
        self.__list.insert(0,item)
        #self.__list.insert(0,item)
               
    def add_rear(self,item):
        #从队列尾部添加一个元素
        self.__list.append(item)
 
    def pop_front(self):
        #从队列头部取
        return self.__list.pop(0)

    def pop_rear(self):
        #从队列尾部取
        return self.__list.pop()
    
    def is_empty(self):
        #判断一个队列是否为空
        return self.__list==[]
      
    def size(self):
        #返回队列的大小
        return len(self.__list)

if __name__=="__main__":
    s=Queue()
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    s.enqueue(4)
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
      

