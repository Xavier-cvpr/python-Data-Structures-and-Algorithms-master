# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 15:42:25 2018

@author: Xavier
双向链表

#可以继承单链表
"""
class Node(object):
    
    """结点"""
    def __init__(self,item):    
        self.elem=item
        self.next=None
        self.prev=None
        
class Doublelinklist(object):
    """双链表"""
    def __init__(self,node=None):
        self.__head=node
        
    def is_empty(self):#对象方法
        return self.__head == None
        #链表是否为空  
    def length(self):  
        #cur 游标，用来移动遍历节点
        cur=self.__head
        #count记录数量
        count=0
        while  cur!=None:
            count+=1
            cur =cur.next
        return count
        #链表长度
 
    def travel(self):
        
        #遍历整个链表
        cur=self.__head
        while cur!=None:
            print(cur.elem,end=" ")
            cur=cur.next
        
    def add(self,item):
        #链表头部添加元素 "头插法"
        node=Node(item)
        node.next=self.__head
        self.__head=node
        node.next.prev=node  #与单链表不一样的
        
    def append(self,item):#item是元素
        
        #链表尾部添加元素   -----尾插法
        node=Node(item)#元素变为节点
        if self.is_empty():
            self.__head=node
        else:    
            cur=self.__head
            while cur.next!=None:
                cur=cur.next
            cur.next=node
            node.prev=cur
                
    def insert(self,pos,item):
        #指定位置添加元素
        """
        :param pos:从0开始
        """
        if pos<0:
            self.add(item)
        elif pos>(self.length()-1):
            self.append(item)
        else:
            cur = self.__head
            count=0
            node=Node(item)

            while count<pos:
                count=count+1
                cur=cur.next
                #当循环退出后，pre指向pos的位置
            node=Node(item)  
            node.next=cur
            node.prev=cur.prev
            cur.prev.next=node
            cur.prev=node
            
    def remove(self,item): 
        #删除节点
        cur=self.__head
       
        while cur!=None:
            if cur.elem==item:
                #判断此节点是否是头结点
                #头结点
                if cur==self.__head:
                    self.__head=cur.next
                    if cur.next:
                        #判断链表是否只要一个节点
                        cur.next.prev=None
                else:
                    cur.prev.next=cur.next
                    if cur.next:
                        cur.next.prev=cur.prev               
                break
            else:
                cur=cur.next
        
    def search(self,item):
        
        cur=self.__head
        while cur !=None:
            if cur.elem == item:
                return True
            else:
                cur=cur.next
        return False
      
if __name__=="__main__":
    ll= Doublelinklist()
    print(ll.is_empty())
    print(ll.length())
    
    ll.append(1)
    print(ll.is_empty())
    print(ll.length())
    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.insert(-1,9)
    ll.insert(3,100)
    ll.insert(10,200)
    ll.travel()
    ll.remove(1)
    print("")
    ll.travel()
    
    
    
       
     
    
        
    
        





    

