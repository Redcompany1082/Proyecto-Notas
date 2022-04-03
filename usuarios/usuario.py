

import usuarios.conexionbdd as conexion# se importa del paquete usuarios el modulo conexion
import datetime #módulo para sacar fechas y tiempo en general
import hashlib #módulo para cifrar las contraseñas



connect = conexion.conectar()# se espera el return de la función conectar
database = connect[0] #el primer índice del return de la función conectar()
cursor = connect[1]#el segundo índice del return de la función conectar()

class Usuario:
    
    def __init__(self, nombre, apellido, email, password): # declarar el constructor de cuando se invoque la clase se tiene que poner los parámetros
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password
        
    def registrar(self):
        fecha = datetime.datetime.now()
        
        #cifrar contraseña 
        cifrado = hashlib.sha256()# algoritmo de cifrado
        cifrado.update(self.password.encode('utf8'))# permite pasarle un darto para cifrarlo, pero necesita recibir byts
        
        
        sql = "INSERT INTO usuarios VALUES(null, %s,%s,%s,%s,%s ) "#insertar en la tabla usuarios los valores de este objeto
        usuario = (self.nombre, self.apellido, self.email, cifrado.hexdigest(), fecha )#hexdigest pasa el cifrado de la contraseña
        
        try: # como el código es suceptible a errores aquí se prueba el registro correcto del usuario, la actualización de la base de datos y la devolución de los parametros
            cursor.execute(sql, usuario) # se ejecuta el comando sql y se reemplazan los %s por los datos de la tupla de usuario
            database.commit()#ingresa los cambios a la base de datos real
            result = [cursor.rowcount, self]# devuelve la cantidad de datos ingresados y el este mismo objeto con los datos

        except: # si el registro falla devuelve un 0 y el objeto y esto en acciones está conectado con el if en el método registro()
            result = [0, self]
            
        return result
        
    def identificar(self):
        #consulta para comprobar si existe el usuario
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"# de la base de usuarios seleccionar el email y la contraseña que le pase mos a ver si es igual
        
        #cifrar contraseña 
        cifrado = hashlib.sha256()# algoritmo de cifrado
        cifrado.update(self.password.encode('utf8'))# permite pasarle un darto para cifrarlo, pero necesita recibir byts
        
        #Datos para la consulta
        usuario = (self.email, cifrado.hexdigest())
        
        cursor.execute(sql, usuario)
        result = cursor.fetchone()# para obtener solo un resultado de la busqueda
        
        return result 