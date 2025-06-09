from sistema import *



def aplicar_interfaz(accion):
    print(accion)

class Usuario:
    def __init__(self):
        self.id = 0
        self.nombre = ""
        self.email = ""
        self.permiso = "UE"

        ultimos_proyectos = consultaSelect("SELECT * FROM `proyectos` ORDER BY id DESC LIMIT 3", ())

        self.cabecera = TK.Frame(ventana)
        self.cuerpo_proyectos = TK.Frame(ventana)
        self.cuerpo_opciones = TK.Frame(ventana)
        self.pie = TK.Frame(ventana)
        self.boton_iniciar_se = TK.Button(self.cabecera, text="Iniciar Sesión", command=self.ventanaInicioSesion)
        self.boton_registrarse = TK.Button(self.cabecera, text="Registrarse", command=self.ventanaRegistro)
        self.boton_perfil = TK.Button(self.cabecera, text="Perfil", command=self.ventanaRegistro)
        self.boton_buscador_proyectos = TK.Button(self.cuerpo_opciones, text="Ver más", command=self.ventanaBuscador)
        self.boton_crear = TK.Button(self.cuerpo_opciones, text="Crear proyecto", command=self.ventanaCrearProyecto)
        self.etiqueta_sin_proyectos = TK.Label(self.cuerpo_proyectos, text="No hay proyectos subidos")
        self.etiqueta_pie = TK.Label(self.pie, text="Desarrollado por Bruno Fornasar González")
        self.botones_ultimos_proyectos = []
        for i in ultimos_proyectos:
            self.botones_ultimos_proyectos.append(TK.Button(self.cuerpo_proyectos, text=i[1], command=lambda: self.ventanaProyecto(i[0])))
        self.btn_test = TK.Button(ventana, text="Testeo", command=self.cerrar_ses)



        # self.btn_test.grid(row=7, column=7)
        self.cabecera.grid(row=0, column=0)
        self.cuerpo_proyectos.grid(row=1, column=0)
        self.cuerpo_opciones.grid(row=2, column=0)
        self.pie.grid(row=3, column=0)
        if self.id == 0:
            self.boton_iniciar_se.grid(row=0, column=0, sticky="e")
            self.boton_registrarse.grid(row=0, column=1, sticky="e")
        else:
            self.boton_perfil.grid(row=0, column=0)
        if ultimos_proyectos == []:
            self.etiqueta_sin_proyectos.grid(row=0, column=0, sticky="ew")
        else:
            for i in range(len(self.botones_ultimos_proyectos)):
                self.botones_ultimos_proyectos[i].grid(row=0, column=i)
        self.boton_buscador_proyectos.grid(row=0, column=0)
        self.etiqueta_pie.grid(row=0, column=0)
        

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

    def ventanaBuscador(self):
        ventana_buscador = Buscador_proyectos(self.permiso, self.id)

    def ventanaCrearProyecto(self):
        ventana_crear = Crear_proyecto(self.crear_proyecto)

    def ventanaProyecto(self, id):
        ventana_proyecto = Presentacion(id, self.permiso)

#----------------------------------------------------------Actualizar interfaz-------------------------------------------------------------------

    def botonCrear(self):
        if self.permiso == "AD":
            self.boton_crear.grid(row=1, column=0, sticky="ew")
        else:
            self.boton_crear.grid_forget()

    def botonesSesion(self):
        if self.id == 0:
            self.boton_perfil.grid_forget()
            self.boton_iniciar_se.grid(row=0, column=0)
            self.boton_registrarse.grid(row=0, column=1)
        else:
            self.boton_registrarse.grid_forget()
            self.boton_iniciar_se.grid_forget()
            self.boton_perfil.grid(row=0, column=0)

#----------------------------------------------------------Metodos-------------------------------------------------------------------

    def iniciar_ses(self, contra, email):    #Debe cambiar los valores de los atributos del objeto para que coincidan con los datos del inicio de sesion
        resultado = consultaSelectUnica("SELECT * FROM `usuarios` WHERE email = %s and contra = %s", (contra, email))
        if resultado == None:
            return 1
        else:
            print(resultado)
            self.id = resultado[0]
            self.email = resultado[3]
            self.nombre = resultado[1]
            self.permiso = resultado[4]
            print(self.permiso)
            self.botonCrear()
            self.botonesSesion()
            return 0

    def cerrar_ses(self):
        if self.id != 0:
            self.id = 0
            self.boton_cerrar_se.grid_forget()
            self.boton_iniciar_se.grid(row=0, column=0)
            self.boton_registrarse.grid(row=0, column=1)
        else:
            self.id = 1
            self.boton_registrarse.grid_forget()
            self.boton_iniciar_se.grid_forget()
            self.boton_cerrar_se.grid(row=0, column=0)

    def registrarse(self, nombre, email, contra):    #Debe ingresar en la base de datos los valores ingresados en el formulario de registro
        resultado = consultaInsert("INSERT INTO `usuarios`(`nombre`, `email`, `contra`) VALUES (%s,%s,%s)", (nombre, email, contra))
        self.iniciar_ses(contra, email)

    def crear_proyecto(self, nombre, desc):    #Debe crear un nuevo proyecto en la base de datos si tiene los permisos necesarios
        consultaInsert("INSERT INTO `proyectos`(`nombre`, `descripcion`, id_creador) VALUES (%s,%s,%s)", (nombre, desc, self.id))

    def enviar_form(self, id_form, respuestas):    #Debe enviar a la tabla "respuestas" de la base de datos los valores con los que se completo el formulario
        if self.permiso == "D" or self.permiso == "AE" or self.permiso == "AS":
            consultaInsert("Insert", ())

    def crear_form(self, nombre, desc):    #Debe crear un nuevo formulario en la base de datos
        consultaInsert("INSERT INTO `proyectos`(`nombre`, `descripcion`) VALUES (%s,%s)", (nombre, desc))

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



class Buscador_proyectos(Interfaz):
    def __init__(self, permiso, id_usuario):
        self.ventana = TK.Toplevel(ventana)
        self.encabezado = TK.Label(self.ventana, text="Proyectos")
        self.contenedor_lista = TK.Frame(self.ventana, borderwidth=3, relief="solid", bg="light blue")
        self.contenedor_lista.configure(height=10, width=10)
        self.contenedor_lista.grid(row=1, column=0, sticky="nsew")
        self.contenedor_lista.grid_rowconfigure(1, weight=1)
        self.contenedor_lista.grid_columnconfigure(0, weight=1)
        # self.contenedor_lista.grid_propagate(False)
        self.lienzo_buscador = TK.Canvas(self.contenedor_lista)
        self.barra_deslizadora = TK.Scrollbar(self.contenedor_lista, orient="vertical", command=self.lienzo_buscador.yview)
        self.lienzo_buscador.configure(yscrollcommand=self.barra_deslizadora.set)
        self.lienzo_buscador.grid(row=0, column=0, sticky="nswe")
        self.barra_deslizadora.grid(row=0, column=1, sticky="ns")
        self.lista_proyectos = TK.Frame(self.lienzo_buscador)

        proyectos = consultaSelect("SELECT `id`, `nombre`, `descripcion`, `tema` FROM `proyectos`", ())


        self.proyectos = []
        self.botones_acceso = []
        self.botones_solicitud = []

        for i in proyectos:
            self.proyectos.append(
                TK.Label(self.lista_proyectos, text=i[1])
            )
            self.botones_acceso.append(
                TK.Button(self.lista_proyectos, text="Ver más", command=lambda: self.ventanaPresentacion(i[0], permiso))
            )
            self.botones_solicitud.append(
                TK.Button(self.lista_proyectos, text="Solicitar", command=lambda: self.ventanaFormulario(1, id_usuario, False))
            )

        self.lista_proyectos.config(bg="lightgreen")
        self.lienzo_buscador.create_window((0, 0), window=self.lista_proyectos, anchor="nw")
        # self.lista_proyectos.bind("<Configure>", lambda e: self.lienzo_buscador.configure(scrollregion=self.lienzo_buscador.bbox("all")))
        for i in range(len(self.proyectos)):
            self.proyectos[i].grid(row=i, column=0, sticky="ew")
            self.botones_acceso[i].grid(row=i, column=1)
            self.botones_solicitud[i].grid(row=i, column=2)
        self.lista_proyectos.update_idletasks()
        self.lienzo_buscador.config(scrollregion=self.lienzo_buscador.bbox("all"))
        self.encabezado.grid(row=0, column=0)
    
    def ventanaFormulario(self, id_proyecto, id_usuario, id_grupo):
        aux = Formulario_solicitar(id_proyecto, id_usuario, id_grupo)

    def ventanaPresentacion(self, id_proyecto):
        aux = Presentacion(id_proyecto, self.permiso)
        



class Formulario(Interfaz):
    def __init__(self, id_proyecto, id_usuario):
        self.ventana = 0
        self.accion = ""
        
        contenido = consultaSelectUnica("SELECT `id`, `nombre`, `descripcion`, `tema` FROM `proyectos` WHERE id = %s", (id_proyecto))

        self.ventana = TK.Toplevel(ventana)
        self.etiquetas = [
            TK.Label(ventana, text="Correo electrónico"),
            TK.Label(ventana, text="Contraseña")
        ]
        self.entradas = [
            TK.Entry(ventana),
            TK.Entry(ventana)
        ]
        self.boton =  TK.Button(ventana, command=self.accion)
        usuarios = []
        self.contenedor_lista = TK.Frame(self.ventana, borderwidth=3, relief="solid", bg="light blue")
        self.contenedor_lista.configure(height=10, width=10)
        self.contenedor_lista.grid(row=1, column=0, sticky="nsew")
        self.contenedor_lista.grid_rowconfigure(1, weight=1)
        self.contenedor_lista.grid_columnconfigure(0, weight=1)
        self.lienzo_buscador = TK.Canvas(self.contenedor_lista)
        self.barra_deslizadora = TK.Scrollbar(self.contenedor_lista, orient="vertical", command=self.lienzo_buscador.yview)
        self.lienzo_buscador.configure(yscrollcommand=self.barra_deslizadora.set)
        self.lienzo_buscador.grid(row=0, column=0, sticky="nswe")
        self.barra_deslizadora.grid(row=0, column=1, sticky="ns")
        self.lista_proyectos = TK.Frame(self.lienzo_buscador)



        self.lista_proyectos.config(bg="lightgreen")
        self.lienzo_buscador.create_window((0, 0), window=self.lista_proyectos, anchor="nw")
        self.lista_proyectos.update_idletasks()
        self.lienzo_buscador.config(scrollregion=self.lienzo_buscador.bbox("all"))

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



class Formulario_solicitar(Interfaz):
    def __init__(self, id_proyecto, id_usuario, id_grupo):
        if id_grupo == False:
            consultaInsert("INSERT INTO `grupos`() VALUES ()", ())
            self.id_grupo = consultaSelectUnica("SELECT MAX(`id`) FROM `grupos`", ())
            consultaInsert("INSERT INTO `usuarios_grupos`(`id_grupo`, `id_usuario`, `rol`) VALUES (%s,%s,%s)", (id_usuario, self.id_grupo, "lider"))
        else:
            self.id_grupo = id_grupo
        usuarios = consultaSelect("SELECT u.`id`, u.`nombre`, u.`contra`, u.`email`, u.`permisos`, EXISTS(SELECT 1 FROM usuarios_grupos ug WHERE u.id = ug.id_usuario AND ug.id_grupo = %s) AS yaEnGrupo FROM `usuarios` u", (self.id_grupo))
        
        self.ventana = TK.Toplevel(ventana)
        
        self.usuarios = []
        self.contenedor_lista = TK.Frame(self.ventana, borderwidth=3, relief="solid", bg="light blue")
        self.contenedor_lista.configure(height=10, width=10)
        self.contenedor_lista.grid(row=1, column=0, sticky="nsew")
        self.contenedor_lista.grid_rowconfigure(1, weight=1)
        self.contenedor_lista.grid_columnconfigure(0, weight=1)
        self.lienzo_buscador = TK.Canvas(self.contenedor_lista)
        self.barra_deslizadora = TK.Scrollbar(self.contenedor_lista, orient="vertical", command=self.lienzo_buscador.yview)
        self.lienzo_buscador.configure(yscrollcommand=self.barra_deslizadora.set)
        self.lienzo_buscador.grid(row=0, column=0, sticky="nswe")
        self.barra_deslizadora.grid(row=0, column=1, sticky="ns")
        self.lista_usuarios = TK.Frame(self.lienzo_buscador)

        for i in usuarios:
            self.usuarios.append((
                TK.Label(self.lista_usuarios, text=i[1]),
                TK.Button(self.lista_usuarios, text="Agregar", command=lambda: self.agregarUsuario(i[0])),
                TK.Button(self.lista_usuarios, text="Eliminar", command=lambda: self.eliminarUsuario(i[0]))
            ))
            self.usuarios[-1][0].grid(row=len(self.usuarios), column=0)
            self.usuarios[-1][1].grid(row=len(self.usuarios), column=1)
            self.usuarios[-1][2].grid(row=len(self.usuarios), column=2)

        self.lista_usuarios.config(bg="lightgreen")
        self.lienzo_buscador.create_window((0, 0), window=self.lista_usuarios, anchor="nw")
        self.lista_usuarios.update_idletasks()
        self.lienzo_buscador.config(scrollregion=self.lienzo_buscador.bbox("all"))

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


    def agregarUsuario(self, id_usuario):
        consultaInsert("INSERT INTO `usuarios_grupos`(`id_grupo`, `id_usuario`) VALUES (%s, %s)", (self.id_grupo, id_usuario))

    def eliminarUsuario(self, id_usuario):
        consultaInsert("UPDATE `usuarios_grupos` SET `estado`='[value-5]' WHERE id_usuario = %s", (id_usuario))



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
        print("hola")
        self.ventana = TK.Toplevel(ventana)
        print("hola")
        self.colores = ""
        self.etiquetas = [
            TK.Label(self.ventana, text="Nombre proyecto"),
            TK.Label(self.ventana, text="Descripcion proyecto")
        ]
        self.entradas = [
            TK.Entry(self.ventana),
            TK.Entry(self.ventana)
        ]
        self.boton =  TK.Button(self.ventana, command=lambda: accion(self.entradas[0].get(), self.entradas[1].get()))

        self.etiquetas[0].grid(row=0, column=0)
        self.etiquetas[1].grid(row=1, column=0)
        self.entradas[0].grid(row=2, column=0)
        self.entradas[1].grid(row=3, column=0)
        self.boton.grid(row=4, column=0)
        


class Presentacion(Interfaz):
    def __init__(self, id_presentacion, permiso):
        self.id = id_presentacion
        # imagen = ""
        # self.imagen = TK.PhotoImage(file= "../img/" + imagen)
        # self.etiqueta_imagen = TK.Label(image=self.imagen)
        encabezado = ""
        contenido = []

        titulo = consultaSelectUnica("SELECT `id`, `encabezado`, `fecha_comienzo`, `fecha_finalizacion`, `definicion`, `proposito` FROM `presentaciones` WHERE id = %s", (id_presentacion))
        etapas = consultaSelect("SELECT * FROM `presentaciones` WHERE id_solicitud = %s AND tipo = 'etapa' ORDER BY id DESC", (id_presentacion))
        contenido = consultaSelect("SELECT `id`, `subtitulo`, `contenido` FROM `contenido` WHERE id_presentacion = %s", (id_presentacion))

        self.ventana = TK.Toplevel(ventana)
        self.botones_etapas = []
        self.cuerpo = []
        self.contenido_cuerpo = []
        for i in range(len(etapas)):
            self.botones_etapas.append(TK.Button(self.ventana, text=etapas[i]["encabezado"], command= lambda: self.abrir_etapa(self.etapas[i]["id"])))
        self.encabezado = TK.Label(self.ventana, text=titulo[0])
        self.contenido = []
        for i in range(len(contenido)):
            self.contenido_cuerpo.append(
                TK.Frame(self.ventana)
            )
            self.cuerpo.append((
                TK.Label(self.contenido_cuerpo[-1], text=contenido[i]["subtitulo"]),
                TK.Label(self.contenido_cuerpo[-1], text=contenido[i]["contenido"])
            ))
            self.contenido_cuerpo[-1].grid(row=i, column=0)
            self.cuerpo[-1][0].grid(row=0, column=1)
            self.cuerpo[-1][1].grid(row=1, column=1)


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



class Perfil(Interfaz):
    def __init__(self, id_usuario, permiso, nombre, email):
        
        invitaciones = consultaSelect("SELECT `id`, `id_grupo`, `id_usuario`, `rol`, `estado` FROM `usuarios_grupos` WHERE id_usuario = %s AND estado = 'pendiente'", (id_usuario))

        self.ventana = TK.Toplevel(ventana)
        self.etiqueta_perfil = TK.Label(self.ventana, text="Perfil")
        self.contenedor_datos = TK.Frame(self.ventana)
        self.etiqueta_nombre = [
            TK.Label(self.ventana, text="Nombre: "),
            TK.Label(self.ventana, text="")
            ]
        self.etiqueta_id = [
            TK.Label(self.ventana, text="ID: "),
            TK.Label(self.ventana, text="")
            ]
        self.etiqueta_email = [
            TK.Label(self.ventana, text="Email: "),
            TK.Label(self.ventana, text="")
        ]
        self.etiqueta_permiso = [
            TK.Label(self.ventana, text="Permisos: "),
            TK.Label(self.ventana, text="")
        ]
        self.etiqueta_solicitudes = TK.Label(self.ventana, text="Solicitudes")

        self.solicitudes = []

        self.contenedor_solicitudes = TK.Frame(self.ventana, borderwidth=3, relief="solid", bg="light blue")
        self.contenedor_solicitudes.configure(height=10, width=10)
        self.contenedor_solicitudes.grid_rowconfigure(1, weight=1)
        self.contenedor_solicitudes.grid_columnconfigure(0, weight=1)
        self.lienzo_solicitudes = TK.Canvas(self.contenedor_solicitudes)
        self.barra_deslizadora_solicitudes = TK.Scrollbar(self.contenedor_solicitudes, orient="vertical", command=self.lienzo_solicitudes.yview)
        self.lienzo_solicitudes.configure(yscrollcommand=self.barra_deslizadora_solicitudes.set)
        self.lienzo_solicitudes.grid(row=0, column=0, sticky="nswe")
        self.barra_deslizadora_solicitudes.grid(row=0, column=1, sticky="ns")
        self.lista_solicitudes = TK.Frame(self.lienzo_solicitudes)



        self.lista_solicitudes.config(bg="lightgreen")
        self.lienzo_solicitudes.create_window((0, 0), window=self.lista_solicitudes, anchor="nw")
        self.lista_solicitudes.update_idletasks()
        self.lienzo_solicitudes.config(scrollregion=self.lienzo_solicitudes.bbox("all"))


        self.invitaciones = []

        self.contenedor_invitaciones = TK.Frame(self.ventana, borderwidth=3, relief="solid", bg="light blue")
        self.contenedor_invitaciones.configure(height=10, width=10)
        self.contenedor_invitaciones.grid_rowconfigure(1, weight=1)
        self.contenedor_invitaciones.grid_columnconfigure(0, weight=1)
        self.lienzo_invitaciones = TK.Canvas(self.contenedor_invitaciones)
        self.barra_deslizadora_invitaciones = TK.Scrollbar(self.contenedor_invitaciones, orient="vertical", command=self.lienzo_invitaciones.yview)
        self.lienzo_invitaciones.configure(yscrollcommand=self.barra_deslizadora_invitaciones.set)
        self.lienzo_invitaciones.grid(row=0, column=0, sticky="nswe")
        self.barra_deslizadora_invitaciones.grid(row=0, column=1, sticky="ns")
        self.lista_invitaciones = TK.Frame(self.lienzo_invitaciones)

        for i in invitaciones:
            self.invitaciones.append(
                TK.Label(self.lista_invitaciones, text=i[0]),
                TK.Button(self.lista_invitaciones, text="Aceptar"),
                TK.Button(self.lista_invitaciones, text="Rechazar")
            )
            

        self.lista_invitaciones.config(bg="lightgreen")
        self.lienzo_invitaciones.create_window((0, 0), window=self.lista_invitaciones, anchor="nw")
        self.lista_invitaciones.update_idletasks()
        self.lienzo_invitaciones.config(scrollregion=self.lienzo_invitaciones.bbox("all"))