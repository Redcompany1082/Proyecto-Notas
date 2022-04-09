
import usuarios.usuario as user# se importa el paquete usuarios y el módulo usuario
import notas.accionesNotas as note # se importa 

class Acciones:
    
    def registro(self):
        print("\nOk!! Vamos a registrarte en el sistema... ")
        nombre = input("¿Cuál es tu nombre?: ")
        apellido = input("¿Cuál es tu apellido?: ")
        email = input("Introduce tu email:  ")
        password = input("Introduce tu contraseña: ") 

        usuario = user.Usuario(nombre, apellido, email, password)# se importó el objetos Usuario y se le pasan como argumentos las variables de este mismo método registrar
        registro = usuario.registrar()# no se le pasa ningún valor porque el constructor, recibe los datos de aquí arriba
        
        if registro[0] >= 1:# si se completa el registro
            print(f"\nPerfecto!! {registro[1].nombre} te has registrado con el email {registro[1].email}") #registro se crea la lista en el modulo usuario con el return de la función registrar
        else:
            print("\nNo te has registrado correctamente!!!")
        
    def login(self):
        print("\nOk!! Identificate en el sistema... ")
        
        try: 
            email = input("Introduce tu email:  ")
            password = input("Introduce tu contraseña: ")
            
            usuario = user.Usuario("","",email, password)# se crea al objeto con solo los datos de email y la contraseña
            login = usuario.identificar()# se llama a la función identificar y por defecto se le pasan los datos de arriba
            
            if email == login[3]:
                print(f"\nBienvenido {login[1]}!! te has registrado en el sistema {login[5]}")
                self.proximasAcciones(login)# proximasAcciones recibe como parametro el usuario identificado, devuelto en el fetchone 
                    
        except Exception as e:
            print(type(e))
            print("Nombre de usuario o contraseña incorrecta")  

    
    def proximasAcciones(self, usuario):
        
        print("""
         Acciones disponibles:
            -Crear notas    (crear)
            -Mostar notas   (mostrar)
            -Modificar nota (modificar)
            -Eliminar notas (eliminar)
            -Salir          (salir)             
              
              """)
        
        
        accion = input("\n¿Qué quieres hacer?: ")
        hazEl = note.Acciones()
        
        
        if accion == "crear":
            hazEl.crear(usuario)# se le pasa el usuario ya identificado
            self.proximasAcciones(usuario)
               
        
        elif accion == "mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == "modificar":
            hazEl.modificar(usuario)
            self.proximasAcciones(usuario)    
        
        
        elif accion == "eliminar":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)
            
        elif accion == "salir":
            print(f"Hasta pronto {usuario[1]}!!!")
            exit()
        
        