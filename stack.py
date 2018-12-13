# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 15:54:54 2018

@author: Xavier
栈的实现
代码使用顺序表来实现的,python中的list
"""
class Stack(object):
    def __init__(self):#把容器保存的地方生成出来
        self.__list=[]
               
    def push(self,item):
        """添加一个新的元素item到栈顶,顺序表使用尾部，时间复杂度o(1),链表的话
        使用头部，时间复杂度o(1)"""
        self.__list.append(item)
        
    def pop(self):
        """弹出栈顶元素"""
        return self.__list.pop()
              
    def peek(self):
        #返回栈顶元素
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
        #判断栈是否为空
        return self.__list==[]
        #return not self.__list  #和上面的效果是一样的
    
    def size(self):
        #返回栈的元素个数
        return len(self.__list)

if __name__=="__main__":
    s=Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    
        
        
