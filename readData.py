import io
from singleLinkedList import nodesList


class read:
    ''' r: read
    w: write
    a: añadir contenido a un fichero ya existente '''
    def __init__(self):
        self.archivo=str("Challenge1.txt")
        self.list_nodes=nodesList()
        self.menu_read_data()
        self.menu_single_linked_list()
        
    def show_file_content(self,archivo):
        with io.open(archivo,'r+',encoding='utf-8') as data_file:
            file_line= data_file.readline()
            while file_line!='':
                print(file_line, end='')
                file_line=data_file.readline()
        data_file.close()
        
    def show_file_content_v2(self,archivo):
        with io.open(archivo,'r+',encoding='utf-8') as data_file:
            for line in data_file.readlines():
                print(line, end='')
        self.converter_text_in_node(archivo)
        data_file.close()
       
    #añadir texto 
    def write_in_file(self,archivo):
        line_write=input("\n << Texto a añadir: \n    >>>>> ")
        with io.open(archivo,'a+',encoding='utf-8') as data_file:
            data_file.write('\n'+line_write)
        data_file.close()
        self.show_file_content(archivo)
        
    #cuando actulice la lista, actualice el archivo de texto
    def replace_file(self,archivo,node_list):
        new_data= ''.join(node_list)
        list=new_data.split(" ")
        with io.open(archivo,"w",encoding="utf-8") as data_file:
            for item in range (len(list)):
                data_file.write(list[item].strip()+"\n")
        data_file.close()
        
    def replace_file_v2(self,archivo):
        current_node=self.list_nodes.head
        with io.open(archivo,'w',encoding='utf-8') as data_file:
            while current_node!=None:
                data_file.write('\n'+current_node.value.strip())
                current_node=current_node.next_node
        data_file.close() 
        
    #sobreescribir el texto
    def write_text_again(self,archivo):
        new_data= input("\n << Ingrese el nuevo texto a sobreescribir: \n     >>>>> ")
        list=new_data.split(" ")
        with io.open(archivo,"w",encoding="utf-8") as data_file:
            for item in range (len(list)):
                data_file.write(list[item]+"\n")
        self.show_file_content(archivo)
        data_file.close()    
        
    #convertir linea de texto en nodo 
    def converter_text_in_node(self,archivo):
        with io.open(archivo,'r+',encoding='utf-8') as data_file:
            for line in data_file.readlines():
                new_node=nodesList.node(line)
                self.list_nodes.append_node(new_node.value)
        data_file.close()
        
    #vaciar lista
    def delete(self,archivo):
        with io.open(archivo,'a',encoding='utf-8') as data_file:
            data_file.truncate(0)
        
    #primer menu
    def menu_read_data(self):
        print("  \n<< Seleccione la opción correspondiente \n      1. Hacer lectura del archivo actual\n      2. Editar el archivo actual\n      3. Sobreescribir el archivo actual")
        while True:
            try:
                option=int(input("     >>>>> "))
                if option==1:
                    self.show_file_content(self.archivo)
                    self.converter_text_in_node(self.archivo)
                elif option==2:
                    self.write_in_file(self.archivo)
                    self.converter_text_in_node(self.archivo)
                elif option==3:
                    self.write_text_again(self.archivo)
                    self.converter_text_in_node(self.archivo)
                else:
                    print(" <<<<< ¡Opción inválida! >>>>> ")
                break
            except ValueError:
                print(" <<<<< ¡Se esperaba un valor numérico! >>>>> ")
                
    #segundo menu
    def menu_single_linked_list(self):
        Option=0
        while Option!=7:
            print("<< Elija la opción con la que desea continuar: \n     1. Insertar un nuevo nodo\n     2. Eliminar un nodo\n     3. Consultar por el valor de un nodo especificado\n     4. Editar el valor de un nodo existente en la lista\n     5. Invertir el contenido de la lista\n     6. Vaciar la lista\n     7. Salir del sistema")
            while True:
                try:
                    Option=int(input("     >>>>> "))
                    if Option==1:
                        print("<< Elija donde desea insertar el nodo: \n     1. Al inicio de la lista\n     2. Al final de la lista\n     3. En una posición específica de la lista")
                        while True:
                            try:
                                option_insert=int(input("     >>>>> "))
                                if option_insert==1:
                                    value_node=input("<< Ingrese el valor del nodo\n     >>>>> ")
                                    self.list_nodes.prepend_node(value_node)
                                    self.list_nodes.show_nodes_list()
                                    self.replace_file_v2(self.archivo)
                                    #aux_list=self.list_nodes.show_nodes_list_v2()
                                    #self.replace_file(self.archivo,aux_list)
                                elif option_insert==2:
                                    value_node=input("<< Ingrese el valor del nodo\n     >>>>> ")
                                    self.list_nodes.append_node(value_node)
                                    self.list_nodes.show_nodes_list()
                                    self.replace_file_v2(self.archivo)
                                    #aux_list=self.list_nodes.show_nodes_list_v2()
                                    #self.replace_file(self.archivo,aux_list)
                                elif option_insert==3:
                                    value_node=input("<< Ingrese el valor del nodo\n     >>>>> ")
                                    index_node=int(input("<< Ingrese la posición del nuevo valor del nodo\n     >>>>> "))
                                    self.list_nodes.insert(index_node,value_node)
                                    self.list_nodes.show_nodes_list()
                                    self.replace_file_v2(self.archivo)
                                    #aux_list=self.list_nodes.show_nodes_list_v2()
                                    #self.replace_file(self.archivo,aux_list)
                                else:
                                    print("<< Opción inválida >>")
                                break
                            except ValueError:
                                print(" <<<<< ¡Se esperaba un valor numérico! >>>>>") 
                    elif Option==2:
                        print("<< Elija donde desea eliminar el nodo: \n     1. Al inicio de la lista\n     2. Al final de la lista\n     3. En una posición específica de la lista")
                        while True:
                            try:
                                option_delete=int(input("     >>>>> "))
                                if option_delete==1:
                                    self.list_nodes.shift_node()
                                    self.list_nodes.show_nodes_list()
                                    self.replace_file_v2(self.archivo)
                                    #aux_list=self.list_nodes.show_nodes_list_v2()
                                    #self.replace_file(self.archivo,aux_list)
                                elif option_delete==2:
                                    self.list_nodes.pop_node()
                                    self.list_nodes.show_nodes_list()
                                    self.replace_file_v2(self.archivo)
                                    #aux_list=self.list_nodes.show_nodes_list_v2()
                                    #self.replace_file(self.archivo,aux_list)
                                elif option_delete==3:
                                    index_node=int(input("<< Ingrese la posición del nodo a eliminar\n     >>>>> "))
                                    self.list_nodes.remove(index_node)
                                    self.list_nodes.show_nodes_list()
                                    self.replace_file_v2(self.archivo)
                                    #aux_list=self.list_nodes.show_nodes_list_v2()
                                    #self.replace_file(self.archivo,aux_list)
                                else:
                                    print("<< Opción inválida >>")
                                break
                            except ValueError:
                                print(" <<<<< ¡Se esperaba un valor numérico! >>>>>")    
                    elif Option==3:
                        consult_node=int(input("<< Ingrese la posicion del valor del nodo a consultar \n     >>>>> "))
                        return_get=self.list_nodes.get(consult_node)
                        print(f"El valor de la posición consultada es :{return_get.value}")
                        self.list_nodes.show_nodes_list()
                        self.replace_file_v2(self.archivo)
                        #aux_list=self.list_nodes.show_nodes_list_v2()
                        #self.replace_file(self.archivo,aux_list)
                    elif Option==4:
                        value_node=input("<< Ingrese el valor del nodo a editar \n     >>>>> ")
                        index_node=int(input("<< Ingrese la posición del nodo a editar\n     >>>>> "))
                        self.list_nodes.update_node(index_node,value_node)
                        self.list_nodes.show_nodes_list()
                        self.replace_file_v2(self.archivo)
                        #aux_list=self.list_nodes.show_nodes_list_v2()
                        #self.replace_file(self.archivo,aux_list)
                    elif Option==5:
                        self.list_nodes.reverse()
                        self.list_nodes.show_nodes_list()
                        self.replace_file_v2(self.archivo)
                        #aux_list=self.list_nodes.show_nodes_list_v2()
                        #self.replace_file(self.archivo,aux_list)
                    elif Option==6:
                        aux_list=self.list_nodes.show_nodes_list_v2()
                        self.list_nodes.delete_list(aux_list)
                        #self.delete(self.archivo)
                        #self.replace_file_v2(self.archivo)
                        self.replace_file(self.archivo,aux_list)
                    elif Option==7:
                        print("*********** Un gusto en servirle ***********")
                    else:
                        print("<< Opción inválida >>")
                    break
                except ValueError:
                    print(" <<<<< ¡Se esperaba un valor numérico! >>>>>") 
        