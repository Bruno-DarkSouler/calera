from sistema import *


def aplicar_interfaz(accion):
    print(accion)

class Usuario:
    def __init__(self):
        self.boton_iniciar_se = TK.Button(ventana, text="IniciarSesion", command=self.ventanaInicioSesion)
        self.boton_registrarse = TK.Button(ventana, text="Registrarse", command=self.ventanaRegistro)
        ultimos_proyectos = consultaSelect("SELECT 1 FROM `usuarios` LIMIT 3", ())
        self.botones_ultimos_proyectos = [
            # TK.Button(ventana, text=ultimos_proyectos[0]["nombre"]),
            # TK.Button(ventana, text=ultimos_proyectos[1]["nombre"]),
            # TK.Button(ventana, text=ultimos_proyectos[2]["nombre"])
            TK.Button(ventana, text="Proyecto 1"),
            TK.Button(ventana, text="Proyecto 2"),
            TK.Button(ventana, text="Proyecto 3")
        ]
        self.boton_buscador_proyectos = TK.Button(ventana, text="Ver más")
        self.boton_iniciar_se.grid(row=0, column=0)
        self.boton_registrarse.grid(row=0, column=1)
        for i in range(len(self.botones_ultimos_proyectos)):
            self.botones_ultimos_proyectos[i].grid(row=2, column=i + 2)
        self.boton_buscador_proyectos.grid(row=len(self.botones_ultimos_proyectos) + 2, column=0)
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
        # ventana_inicio_se = Inicio_se(lambda: self.iniciar_ses("", ""))
        ventana_inicio_se = Inicio_se(self.iniciar_ses)

    def ventanaRegistro(self):
        ventana_inicio_se = Resgistro(self.registrarse)

    def ventanaProyecto(self):
        ventana_proyecto = Presentacion()

#----------------------------------------------------------Metodos-------------------------------------------------------------------

    def iniciar_ses(self, contra, email):    #Debe cambiar los valores de los atributos del objeto para que coincidan con los datos del inicio de sesion
        resultado = consultaSelectUnica("SELECT * FROM `usuarios` WHERE email = %s and contra = %s", (contra, email))
        if resultado == None:
            return 1
        else:
            self.id = resultado["id"]
            self.email = resultado["email"]
            self.nombre = resultado["nombre"]
            self.permiso = resultado["permiso"]
            return 0


    def registrarse(self, nombre, email, contra):    #Debe ingresar en la base de datos los valores ingresados en el formulario de registro
        resultado = consultaInsert("INSERT INTO `usuarios`(`nombre`, `contra`, `email`) VALUES (%s,%s,%s)", (nombre, email, contra))

    def crear_proyecto(self, nombre, descripcion, tema, grupo):    #Debe crear un nuevo proyecto en la base de datos si tiene los permisos necesarios
        resultado = consultaInsert("INSERT INTO `usuarios`(`nombre`, `contra`, `email`) VALUES (%s,%s,%s)", (nombre, descripcion, grupo, tema))
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

class Interfaz:
    def __init__(self):
        self.boton_iniciar_se 

class Proyecto(Interfaz):
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



class Evento(Interfaz):
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



class Buscador(Interfaz):
    def __init__(self):
        self.ventana = TK.Toplevel(ventana)
        self.encabezado = TK.Label(self.ventana, text="Proyectos")
        self.contenedor_lista = TK.Frame(self.ventana, borderwidth=3, relief="solid", bg="light blue")
        self.contenedor_lista.config(height=400, width=300)
        self.contenedor_lista.grid_propagate(False)
        self.lienzo_buscador = TK.Canvas(self.contenedor_lista)
        self.lista_proyectos = TK.Frame(self.lienzo_buscador)
        self.barra_deslizadora = TK.Scrollbar(self.contenedor_lista)
        self.lienzo_buscador.config(yscrollcommand=self.barra_deslizadora.set)

        self.proyectos = [
            TK.Label(self.contenedor_lista, text="CONSULTAR NOMBRES"),
            TK.Label(self.contenedor_lista, text="CONSULTAR NOMBRES"),
            TK.Label(self.contenedor_lista, text="CONSULTAR NOMBRES"),
            TK.Label(self.contenedor_lista, text="CONSULTAR NOMBRES"),
            TK.Label(self.contenedor_lista, text="CONSULTAR NOMBRES"),
            TK.Label(self.contenedor_lista, text="CONSULTAR NOMBRES"),
            TK.Label(self.contenedor_lista, text="CONSULTAR NOMBRES"),
            TK.Label(self.contenedor_lista, text="CONSULTAR NOMBRES"),
            TK.Label(self.contenedor_lista, text="CONSULTAR NOMBRES"),
            TK.Label(self.contenedor_lista, text="CONSULTAR NOMBRES")
            ]
        self.botones_acceso = [
            TK.Button(self.lista_proyectos),
            TK.Button(self.lista_proyectos),
            TK.Button(self.lista_proyectos),
            TK.Button(self.lista_proyectos),
            TK.Button(self.lista_proyectos),
            TK.Button(self.lista_proyectos),
            TK.Button(self.lista_proyectos),
            TK.Button(self.lista_proyectos),
            TK.Button(self.lista_proyectos),
            TK.Button(self.lista_proyectos)
            ]
        self.botones_solicitar = [
            TK.Button(self.lista_proyectos),
            TK.Button(self.lista_proyectos),
            TK.Button(self.lista_proyectos),
            TK.Button(self.lista_proyectos),
            TK.Button(self.lista_proyectos),
            TK.Button(self.lista_proyectos),
            TK.Button(self.lista_proyectos),
            TK.Button(self.lista_proyectos),
            TK.Button(self.lista_proyectos),
            TK.Button(self.lista_proyectos)
            ]
        
        for i in range(len(self.proyectos)):
            self.proyectos[i].grid(row=i, column=0)
            self.botones_acceso[i].grid(row=i, column=1)
            self.botones_solicitar[i].grid(row=i, column=2)
        self.lienzo_buscador.grid(row=0, column=0)
        self.barra_deslizadora.grid(row=0, column=1)
        self.contenedor_lista.grid(row=0, column=0)



class Formulario(Interfaz):
    def __init__(self):
        self.ventana = 0
        self.accion = ""
        self.etiquetas = [
            TK.Label(ventana, text="Correo electrónico"),
            TK.Label(ventana, text="Contraseña")
        ]
        self.entradas = [
            TK.Entry(ventana),
            TK.Entry(ventana)
        ]
        self.boton =  TK.Button(ventana, command=self.accion)

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


    def abrir_ventana(self):
        for i in range(len(self.etiquetas)):
            self.etiquetas[i].grid(row=i, column=0)
            self.entradas[i].grid(row=i, column=1)
        self.boton.grid(row=len(self.etiquetas), column=1, columnspan=2)



class Inicio_se(Formulario):
    def __init__(self, accion):
        self.ventana = TK.Toplevel(ventana)
        self.colores = ""
        self.accion = accion
        self.etiquetas = [
            TK.Label(self.ventana, text="Correo electrónico"),
            TK.Label(self.ventana, text="Contraseña")
        ]
        self.entradas = [
            TK.Entry(self.ventana),
            TK.Entry(self.ventana)
        ]
        self.boton =  TK.Button(self.ventana, command=lambda: self.accion(self.entradas[0].get(), self.entradas[1].get()))

        self.abrir_ventana()



class Resgistro(Formulario):
    def __init__(self, accion):
        self.ventana = TK.Toplevel(ventana)
        self.colores = ""
        self.accion = accion
        self.etiquetas = [
            TK.Label(self.ventana, text="Nombre"),
            TK.Label(self.ventana, text="Correo electrónico"),
            TK.Label(self.ventana, text="Contraseña")
        ]
        self.entradas = [
            TK.Entry(self.ventana),
            TK.Entry(self.ventana),
            TK.Entry(self.ventana)
        ]
        self.boton =  TK.Button(self.ventana, command=lambda: self.accion(self.entradas[0].get(), self.entradas[1].get(), self.entradas[2].get()))

        self.abrir_ventana()



class Crear_proyecto(Formulario):
    def __init__(self, accion):
        self.ventana = 0
        self.colores = ""
        self.accion = accion
        self.etiquetas = [
            TK.Label(self.ventana, text="Nombre proyecto"),
            TK.Label(self.ventana, text="Descripcion proyecto")
        ]
        self.entradas = [
            TK.Entry(self.ventana),
            TK.Entry(self.ventana)
        ]
        self.boton =  TK.Button(self.ventana, command=self.accion)
        


class Presentacion(Interfaz):
    def __init__(self, id_grupo, id_presentacion, permiso):
        self.ventana = TK.Toplevel(ventana)
        self.etapas = consultaSelect("SELECT * FROM `presentaciones` WHERE id_solicitud = %s AND tipo = 'etapa' ORDER BY id DESC", (id_presentacion))
        for i in range(len(self.id_etapas)):
            self.botones_etapas.append(TK.Button(self.ventana, text=self.nombre_etapas[i], command= lambda: self.abrir_etapa(self.id_etapas[i])))
        encabezado = ""
        contenido = []
        imagen = ""
        self.id = id_presentacion
        self.imagen = TK.PhotoImage(file= "../img/" + imagen)
        self.etiqueta_imagen = TK.Label(image=self.imagen)
        self.encabezado = TK.Label(self.ventana, text=encabezado)
        self.contenido = []
        for i in contenido:
            self.contenido.append(TK.Label(self.ventana, text=i))

        self.abrir_ventana()

    def get_id(self):
        return self.id

    def set_id(self, id_presentacion):
        self.id = id_presentacion

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def abrir_ventana(self):
        self.encabezado.grid(row=0, column=0)
        self.etiqueta_imagen.grid(row=1, column=0)
        for i in range(len(self.contenido)):
            self.contenido[i].grid(row=i+2, column=0)

    def abrir_etapa(self, id_presentacion):
        self.nueva_etapa = Etapa(id)


class Etapa(Interfaz):
    def __init__(self, id):
        self.ventana = TK.Toplevel(ventana)
        self.id_etapas = []
        self.nombre_etapas = []
        self.id = id
        encabezado = ""
        contenido = []
        self.encabezado = TK.Label(self.ventana, text=encabezado)
        self.contenido = []
        for i in contenido:
            self.contenido.append(TK.Label(self.ventana, text=i))
        
        self.abrir_ventana()

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

    def abrir_ventana(self):
        self.encabezado.grid(row=0, column=0)
        for i in range(len(self.contenido)):
            self.contenido[i].grid(row=i+1, column=0)
