import re


#metodo para verificar si un archivo es formato .xlsx retornado true

def MesXlsx(archivo):
    
    resultado = re.search(r".xlsx", archivo) # retorna la uicacion del string buscado
    print(resultado.group)
    
    return False
            

archivo = input("introduce archivo ")
MesXlsx(archivo)

