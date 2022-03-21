import io
from singleLinkedList import nodesList
inst_operation_node=nodesList()

class read:
    ''' r: read
    w: write
    a: añadir contenido a un fichero ya existente '''
    def __init__(self):
        self.archivo=open("Challenge1.txt")
        self.list_nodes=[]
        self.menu_read_data()
        
    def show_file_content(self):
        with io.open("Challenge1.txt",'r+',encoding='utf-8') as data_file:
            file_line= data_file.readline()
            while file_line!='':
                print(file_line, end='')
                file_line=data_file.readline()
        #inst_operation_node.converter_text_in_node()
        self.converter_text_in_node()
        data_file.close()
        
    def show_file_content_v2(self):
        with io.open("Challenge1.txt",'r+',encoding='utf-8') as data_file:
            for line in data_file.readlines():
                print(line, end='')
        #inst_operation_node.converter_text_in_node()
        self.converter_text_in_node()
        data_file.close()
       
    #añadir texto 
    def write_in_file(self):
        line_write=input("\n << Texto a añadir \n    >>>>> ")
        with io.open("Challenge1.txt",'a+',encoding='utf-8') as data_file:
            data_file.write('\n'+line_write)
        #inst_operation_node.converter_text_in_node()
        self.converter_text_in_node()
        data_file.close()
        self.show_file_content()
        
    #reemplazar todo el texto
    def replace_file(self):
        line_write=input("\n << Nuevo texto \n    >>>>> ")
        with io.open("Challenge1.txt",'w+',encoding='utf-8') as data_file:
            data_file.write(line_write)
        #inst_operation_node.converter_text_in_node()
        self.converter_text_in_node()
        data_file.close()
        self.show_file_content()
        
    def converter_text_in_node(self):
        print("\n Lista con cada dato de archivo en nodo")
        with io.open('Challenge1.txt','r+',encoding='utf-8') as data_file:
            for line in data_file.readlines():
                new_node=inst_operation_node.node(line)
                self.list_nodes.append(new_node.value)
        print(self.list_nodes)
        data_file.close()
        
    def menu_read_data(self):
        print("  \n<< Seleccione la opción correspondiente \n      1. Hacer lectura del archivo actual\n      2. Editar el archivo actual\n      3. Sobreescribir el archivo actual\n")
        while True:
            try:
                option=int(input("     >>>>> "))
                if option==1:
                    self.show_file_content()
                elif option==2:
                    self.write_in_file()
                elif option==3:
                    self.replace_file()
                else:
                    print(" <<<<< ¡Opción inválida! >>>>> ")
                break
            except ValueError:
                print(" <<<<< ¡Se esperaba un valor numérico! >>>>> ")
        