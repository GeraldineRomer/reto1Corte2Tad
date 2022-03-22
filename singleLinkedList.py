from optparse import Option
from platform import node
import io

class nodesList:
    
    class node:
        #inicializar estructura nodo
        def __init__(self, value):
            self.value=value
            self.next_node=None
            
    #inicializar estructura de la lista simplemente enlazada
    def __init__(self):
        self.head=None
        self.tail=None
        self.lenght=0
        self.list_nodes=[]
        
    #mostrar lista
    def show_nodes_list(self):
        node_list=[]
        current_node=self.head
        while(current_node!=None):
            node_list.append(current_node.value)
            current_node=current_node.next_node 
        print(f"{node_list} Cantidad de nodos -> {self.lenght}")  
        
    def show_nodes_list_v2(self):
        node_list=[]
        current_node=self.head
        while(current_node!=None):
            node_list.append(current_node.value)
            current_node=current_node.next_node 
        #print(f"{node_list} Cantidad de nodos -> {self.lenght}")
        return node_list
    
    
    
    #añadir nodo al inicio de la lista    
    def prepend_node(self,value):
        new_node=self.node(value)
        if self.head==None and self.tail==None:
            self.head=new_node
            self.tail=new_node
            
        else:
            new_node.next_node=self.head
            self.head=new_node
        self.lenght+=1
            
    #añadir nodo al final de la lista
    def append_node(self,value):
        new_node=self.node(value)
        if self.head==None and self.tail==None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next_node=new_node
            self.tail=new_node
        self.lenght+=1
            
    #eliminar primer nodo de la lista
    def shift_node(self):
        if self.lenght==0:
            self.head=None
            self.tail=None
        else:
            current_node=self.head
            self.head=current_node.next_node
            current_node.next_node=None
            self.lenght-=1
            print(f"El valor del nodo eliminado es: {current_node.value}")
            
    #eliminar ultimo nodo de la lista
    def pop_node(self):
        if self.lenght==0:
            self.head=None
            self.tail=None
        else:
            current_node=self.head
            new_tail=current_node
            while(current_node.next_node!=None):
                new_tail=current_node
                current_node=current_node.next_node
            self.tail=new_tail
            self.tail.next_node=None
            self.lenght-=1
            print(f"El valor del nodo eliminado es: {current_node.value}")
            
    #consultar el valor de determinado nodo por el indice
    def get(self,index):
        #indice por cabeza -> user
        if index==0:
            print(self.head.value)
            return self.head
        #indice por cola -> user
        elif index==self.lenght-1:
            print(self.tail.value)
            return self.tail
        elif not (index<0 or index>=self.lenght):
             
            current_node=self.head
            contador=0
            while(contador!=index):
                current_node=current_node.next_node
                contador+=1
            print(current_node.value)
            return current_node
        else:
            return None
    
    #actualizar el valor del nodo
    def update_node(self,index,value):
        current_node=self.get(index)
        if current_node!= None:
            current_node.value=value
        else:
            return None
         
     
    #agregar un elemento en cualquier lugar de la linkedList
    def insert(self,index,value):
        #añadir el nodo al principio de la lista -> prepend
        if index==1:
            return self.prepend_node(value)
        #añadir el nodo al final de la lista -> append
        elif index==self.lenght+1:
            return self.append_node(value)
        elif not(index<=0 or index>=self.lenght+1):
            new_node=self.node(value)
            pre_node=self.get(index-2)
            sig_node=pre_node.next_node
            pre_node.next_node=new_node
            new_node.next_node=sig_node
            self.lenght+=1
        else:
            return None
        
    #eliminar un elemento de cualquier lugar de la linkedList
    def remove(self,index):
        #eliminar el primer nodo de la lista -> shift
        if index==1:
            return self.shift_node()
        #eliminar el ultimo nodo de la lista -> pop
        elif index==self.lenght:
            return self.pop_node()
        elif not(index<=0 or index>self.lenght):
            pre_node=self.get(index-2)
            current_node=pre_node.next_node
            pre_node.next_node=current_node.next_node
            current_node.next_node=None
            self.lenght-=1
            return current_node
        else:
            return None
        
    #revertir la lista 
    def reverse (self):
        reverse_node=None
        current_node=self.head
        self.tail=current_node
        while current_node!=None:
            next_node=current_node.next_node
            current_node.next_node=reverse_node
            reverse_node=current_node
            current_node=next_node
        self.head=reverse_node
        return self.head
            
    #vaciar la lista 
    def delete_list(self,node_list):
        for i in range(len(node_list)):
            node_list.pop()
        #print(node_list)
     
    def delete_list_v2(self):
        self.head=None
        self.tail=None