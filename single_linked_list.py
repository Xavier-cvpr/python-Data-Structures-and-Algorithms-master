# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 20:21:32 2018
######################单链表    
p13 4-06  18/12/4
@author: xuhaohao
"""
#单链表的结点


class Node(object):
    #节点
    def __init__(self,elem):
        self.elem=elem#存放数据元素
        self.next=None#下一个节点的标识
        
        
class SingleLinkList(object):
    #单链表
    def __init__(self,node=None):
       
        self.__head = node                 #起始节点 私有属性,外部无法访问
    
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
            node=Node(item)
            pre=self.__head
            count=0
            while count<(pos-1):
                count=count+1
                pre=pre.next
                #当循环退出后，pre指向pos-1
            node.next=pre.next
            pre.next=node
    


    def remove(self,item): 
        #删除节点
        cur=self.__head
        pre=None
        while cur!=None:
            if cur.elem==item:
                #判断此节点是否是头结点
                if cur==self.__head:
                    self.__head=cur.next
                else:
                    pre.next=cur.next
                break
            else:
                pre=cur
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
    ll=  SingleLinkList()
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
    
    
    
       
     
    
        
    
        






'''
def rev(link):
    pre = link
    cur = link.next
    pre.next = None
    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return pre

root = rev(link)
while root:
    print (root.data)
    root = root.next
'''