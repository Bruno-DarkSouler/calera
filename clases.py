from sistema import *


def aplicar_interfaz(accion):
    print(accion)

class Usuario:
    def __init__(self):
        self.id = 0
        self.nombre = ""
        self.email = ""
        self.permiso = "UE"

#----------------------------------------------------------Getters y Setters--------------------------------------------------------

    def get_id(self):
        return self.id
    
    def set_id(self, valor):
        self.id = valor

    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, valor):
        self.nombre = valor

    def get_email(self):
        return self.email
    
    def set_email(self, valor):
        self.email = valor

#----------------------------------------------------------Interfaz-------------------------------------------------------------------

    def ventanaInicioSesion(self):
        self.ventana = TK.Toplevel()

    def venatanaRegistro(self):
        self.ventana = TK.Toplevel()

#----------------------------------------------------------Metodos-------------------------------------------------------------------

    def iniciar_ses(self, contra, email):    #Debe cambiar los valores de los atributos del objeto para que coincidan con los datos del inicio de sesion
        resultado = consultaSelect("SELECT", (contra, email))
        if resultado == 1:
            aplicar_interfaz("mensaje de error")
        else:
            self.permiso = "Nuevo permiso"
            self.nombre = "Nombre"
            self.email = "Email"
            aplicar_interfaz("cerrar ventana")

    def registrarse(self, nombre, email, contra):    #Debe ingresar en la base de datos los valores ingresados en el formulario de registro
        resultado = consultaInsert("CONSULTA", ())
        if resultado == 1:
            aplicar_interfaz("Mensaje de error")
        else:
            aplicar_interfaz("cerrar ventana")
            aplicar_interfaz("Abrir inicio de sesion")

    def crear_proyecto(self, nombre, descripcion, tema, grupo):    #Debe crear un nuevo proyecto en la base de datos si tiene los permisos necesarios
        resultado = consultaInsert("CONSULTA", (nombre, descripcion, grupo, tema))
        if resultado == 1:
            aplicar_interfaz("Mensaje de error")
        else:
            aplicar_interfaz("cerrar ventana")
            aplicar_interfaz("Abrir inicio de sesion")


    def enviar_form(self, id_form, respuestas):    #Debe enviar a la tabla "respuestas" de la base de datos los valores con los que se completo el formulario
        if self.permiso == "D" or self.permiso == "AE" or self.permiso == "AS":
            consultaInsert("Insert", ())

    def crear_form(self):    #Debe crear un nuevo formulario en la base de datos
        print("hola")

    def crear_proyecto(self):    #Debe crear un nuevo proyecto en la base de datos
        print("hola")

    def crear_evento(self):    #Debe crear un nuevo evento en la base de datos
        print("hola")

    def ver_proyectos(self, permiso_requerido):    #Devolvera un "true" si tiene el permiso requerido, por el contrario, un "false"
        print("hola")

    def subir_etapa(self):    #Debera subir la informacion ingresada en el formulario a la base de datos en la tabla "etapas"
        print("hola")

    def subir_presentacion(self):    #Debera subir la informacion ingresada en el formulario a la base de datos en la tabla "presentacion"
        print("hola")

    def crear_grupo(self):    #Debera ingresar la cantidad de registros correspondientes en base a los usuarios asignados al grupo en cuestion
        print("hola")

    def crear_grupo(self):    #Debera ingresar la cantidad de registros correspondientes en base a los usuarios asignados al grupo en cuestion
        print("hola")

    def crear_grupo(self):    #Debera ingresar la cantidad de registros correspondientes en base a los usuarios asignados al grupo en cuestion
        print("hola")

    def crear_grupo(self):    #Debera ingresar la cantidad de registros correspondientes en base a los usuarios asignados al grupo en cuestion
        print("hola")

    def crear_grupo(self):    #Debera ingresar la cantidad de registros correspondientes en base a los usuarios asignados al grupo en cuestion
        print("hola")

    def crear_grupo(self):    #Debera ingresar la cantidad de registros correspondientes en base a los usuarios asignados al grupo en cuestion
        print("hola")

    def crear_grupo(self):    #Debera ingresar la cantidad de registros correspondientes en base a los usuarios asignados al grupo en cuestion
        print("hola")

    

class Proyecto():
    def __init__(self, id, nombre, desc):
        self.id = id
        self.nombre = nombre
        self.desc = desc

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_desc(self):
        return self.desc

    def set_desc(self, desc):
        self.desc = desc



class Evento():
    def __init__(self, id, nombre, desc):
        self.id = id
        self.nombre = nombre
        self.desc = desc

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_desc(self):
        return self.desc

    def set_desc(self, desc):
        self.desc = desc


class Formulario():
    def __init__(self, id, nombre, desc):
        self.id = id
        self.nombre = nombre
        self.desc = desc

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_desc(self):
        return self.desc

    def set_desc(self, desc):
        self.desc = desc



class Etapa():
    def __init__(self, id, nombre, email):
        self.id = id
        self.nombre = nombre
        self.email = email

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email


class Presentacion(Etapa):
    def __init__(self, id, nombre, email, imagen):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.imagen = imagen
