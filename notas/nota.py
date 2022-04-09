import usuarios.conexionbdd as conexion # se importa del paquete usarios el módulo conexion para poder conectarse a la base de datos

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]





class Nota:
    
    def __init__(self, usuario_id, titulo = "", descripcion =""):
         self.usuario_id = usuario_id
         self.titulo = titulo
         self.descripcion = descripcion
         
         
    def guardar(self):
        sql = "INSERT INTO notas VALUES(null, %s,%s,%s, NOW())" # now() función de sql para crear fechas actuales
        nota = (self.usuario_id, self.titulo, self.descripcion)
        
        cursor.execute(sql, nota)
        database.commit()
        
        return [cursor.rowcount, self]
    
   
    def modificar(self):
        sql = f"UPDATE notas SET descripcion = \"{self.descripcion}\" WHERE usuario_id = {self.usuario_id} AND titulo LIKE \"%{self.titulo}%\" "
        cursor.execute(sql)
        database.commit()
        
        return [cursor.rowcount, self]
    
    
    
    def listar(self):
        sql = f"SELECT * FROM notas WHERE usuario_id = {self.usuario_id}" # selecciona todas las notas de el usario identificado
        cursor.execute(sql)
        result = cursor.fetchall()#saca dentro de una lista todos los datos que se seleccionaron 
        
        return result
    
    def eliminar(self):#dentro de clase ya está el titulo 
        sql = f"DELETE FROM notas WHERE  usuario_id = {self.usuario_id} AND titulo LIKE '%{self.titulo}%' " #borrar del usuario identificado  la nota con el titulo contenido en el titulo guardado en la base de datos
        cursor.execute(sql)
        database.commit()
        
        return [cursor.rowcount, self]
    
    
    
    