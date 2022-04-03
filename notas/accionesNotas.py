import notas.nota as modeloNota




class Acciones:
    
    
    def crear(self, usuario):
        
        print(f"Ok, {usuario[1]}, Crearemos una nueva nota ")
        #sacar los datos para guardar
        
        titulo = input("\nIntroduce el título de tu nota: ")
        descripcion = input("\nIntroduce el contenido de tu nota: ")
        
        nota = modeloNota.Nota(usuario[0], titulo, descripcion)# se crea la nota con el id del usuario identificado
        guardar = nota.guardar()
        
        if guardar[0] >= 1:
            print(f"\nSe ha guardado con exito la nota {nota.titulo}")
             
        else:
            print("No se ha podido guardar la nota") 
            
    def mostrar(self, usuario):
        print(f"\nOk, {usuario[1]}, Se mostrarán todas tus notas...\n")
        
        nota = modeloNota.Nota(usuario[0])
        notas = nota.listar()
        
        for lista in notas:#devuelve la lista de notas 
            print("***********************************************")
            print(lista[2])
            print(lista[3])    
            print("***********************************************")
            
    def borrar(self, usuario):
        print(f"Ok, {usuario[1]} vamos a borrar notas...")
        
        titulo = input("Introduce el titulo de la nota a borrar: ")
        nota = modeloNota.Nota(usuario[0], titulo)
        
        eliminar = nota.eliminar()
        
        
        if eliminar[0] >= 1: # eliminar [0] devuelve el número de la rowcount
            print(f"Se ha borrado {nota.titulo}")
        else:
            print("No se ha borrado la nota")
            
            