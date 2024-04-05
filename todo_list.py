
# Usuario
class Usuario:
    def __init__(self, id_usuario, nombre_usuario, email_usuario):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.email_usuario = email_usuario
 


# Redordatorio
class Recordatorio:    
    def __init__( self, usuario, id_actividad, nombre_actividad, estado_actividad ):
        self.usuario  = usuario
        self.id_actividad = id_actividad
        self.nombre_actividad = nombre_actividad
        self.estado_actividad = estado_actividad


# Administrador
class Administrador:
    def __init__ (self):
        self.recordatorios = []

    def crear_actividad (self, info_usuario, info_actividad) :    
        usuario = Usuario(info_usuario['id_usuario'], 
            info_usuario['nombre_usuario'], 
            info_usuario['email_usuario']
            )
        recordatorio = Recordatorio(usuario,info_actividad['id_actividad'],
            info_actividad['nombre_actividad'],
            info_actividad['estado_actividad']
            )
        self.recordatorios.append(recordatorio)


# Valores

info_usuario_1 = {
    'id_usuario': 1,
    'nombre_usuario': "Juan",
    'email_usuario': "juan@uan.edu.co"  
}
info_usuario_2 = {
    'id_usuario': 2,
    'nombre_usuario': "John",
    'email_usuario': "john@uan.edu.co"  
}
info_actividad = {
    'id_actividad': 1,
    'nombre_actividad': 'Hacer tarea Ing SW',
    'estado_actividad': 'pendiente'
}

if __name__ == "__main__":
    
    adm = Administrador()

    adm.crear_actividad(info_usuario_1,info_actividad)
    adm.crear_actividad(info_usuario_2,info_actividad)

    for rec in adm.recordatorios:
        print("Usuario: ",rec.usuario.nombre_usuario)




