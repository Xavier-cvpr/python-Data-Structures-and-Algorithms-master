# -*- coding: utf-8 -*-
"""

######################单向循环链表    
p13 4-06  18/12/7
@author: xuhaohao
"""



class Node(object):
    #节点
    def __init__(self,elem):
        self.elem=elem#存放数据元素
        self.next=None#下一个节点的标识
        
        
class SingleCycleLinkList(object):
    #单向循环链表
    def __init__(self,node=None):
       
        self.__head = node
        if node:                 #起始节点 私有属性,外部无法访问
            node.next=node            #循环链表，指向自身
    def is_empty(self):#对象方法
        return self.__head == None
        #链表是否为空
      
    
    def length(self):
        if self.is_empty():
            return 0
        
        #cur 游标，用来移动遍历节点
        cur=self.__head
        #count记录数量
        count=1
        while  cur.next!=self.__head:
            count+=1
            cur =cur.next
        return count
        #链表长度
    
    
    def travel(self):
        
        #遍历整个链表
        if self.is_empty():
            return 
        cur=self.__head
        while cur.next!=self.__head:
            print(cur.elem,end=" ")
            cur=cur.next
        #退出循环，cur指向尾节点，但是尾节点，没有打印出来
        print(cur.elem)
        
    def add(self,item):
        #链表头部添加元素 "头插法"
        node=Node(item)
        if self.is_empty():
            self.__head=node
            node.next=node
        else:
            cur=self.__head
            while cur.next!=self.__head:
                cur=cur.next
            #退出循环，cur指向尾节点
            node.next=self.__head
            self.__head=node
            cur.next=node#或者 cur.next=self.__head
        
        
        
        

     
    def append(self,item):#item是元素
        
        #链表尾部添加元素   -----尾插法
        node=Node(item)#元素变为节点
        if self.is_empty():
            self.__head=node
            node.next=node
        else:    
            cur=self.__head
            while cur.next!=self.__head:
                cur=cur.next    
            cur.next=node
            node.next=self.__head
            
        
          
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
        if self.is_empty():
            return
        
        cur=self.__head
        pre=None
        while cur.next!=self.__head:
            if cur.elem==item:
                #判断此节点是否是头结点
                if cur==self.__head:
                    #头结点
                    #找尾节点
                    rear=self.__head
                    while rear.next!=self.__head:
                        rear=rear.next
                    self.__head=cur.next
                    rear.next=self.__head 
                    #self.__head=cur.next
                else:
                    #中间节点
                    pre.next=cur.next
                return
            else:
                pre=cur
                cur=cur.next
        
        #退出循环，代表的是尾节点
        if cur.elem==item:
            if cur==self.__head:
                #链表只要一个节点
                self.__head=None
            else:
                pre.next=cur.next
        
    def search(self,item):
        
        if self.is_empty():
            return False
        cur=self.__head
        while cur.next!=self.__head:
            if cur.elem == item:
                return True
            else:
                cur=cur.next
        if cur.elem==item:
            return True
        return False
    
            
        
        
    
    
if __name__=="__main__":
    ll=  SingleCycleLinkList()
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
    '''
    ll.remove(1)
    print("")
    ll.travel()
    '''
    
    
       
     
    
        
    
        






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