"""
Proyecto Python Mysqpl
-Abrir un asistente 
-Login o registro
-Si elegimos registro, se registrará un usuario em la bdd
-Si elegimos login, identificará al usuario  
-Crear notas, Mostrar notas, Borrar notas


"""

from usuarios import acciones #importamos el módulo de acciones desde el paquete usuarios




print("""

NOTAS      

Acciones disponibles:      
    -registro
    -login 
    -salir 
      
""")#""" triple comilla para un print multilínea

accion = input("¿Qué quieres hacer?: ")
hacerEL = acciones.Acciones()

if accion == "registro":
    
    hacerEL.registro()# importamos del módulo acciones el objeto Acciones y el método para registrar un usuario
    
    
elif accion == "login":
   
    hacerEL.login()# importamos del módulo acciones el objeto Acciones y el método para logear un usuario
    
elif accion == "salir":
     
    exit()
    
