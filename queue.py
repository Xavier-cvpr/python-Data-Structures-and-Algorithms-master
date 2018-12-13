# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 16:45:47 2018

@author: Xavier
"""

class Queue(object):
    #取的那一端是队头，插入的那一端是队尾
    #队列
    def __init__(self):
        #构造函数胡
        self.__list=[]
            
    def enqueue(self,item):
        #往队列中添加一个item元素
        self.__list.append(item)
        #self.__list.insert(0,item)
               
    def dequeue(self):
        #从队列头部删除一个元素
        return self.__list.pop(0)
        #return self.__list.pop()
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
    