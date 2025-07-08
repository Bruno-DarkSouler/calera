from PySide6 import QtWidgets as QW
from PySide6 import QtGui as QG
from PySide6.QtCore import Qt

class VentanaPrincipal(QW.QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(768, 450)
        self.setStyleSheet(
            "background-color: #000d20;"
        )
        self.setWindowTitle("Calera")

        #Datos de sesion
        self.sesion = {
            "id": 0,
            "nombre": "",
            "permiso": "UE"
        }

        #Contenedor central
        contenedor_central = QW.QWidget(self)
        self.setCentralWidget(contenedor_central)
        
        #Contenedor general de los objetos
        contenedor_menu = QW.QHBoxLayout(contenedor_central)
        contenedor_perfil = QW.QVBoxLayout()
        contenedor_proyectos = QW.QVBoxLayout()
        contenedor_acciones_perfil = QW.QVBoxLayout()
        contenedor_invitaciones = QW.QVBoxLayout()

        #Contenedores de estilo
        cuadro_contenedor_perfil = QW.QFrame()
        cuadro_contenedor_proyectos = QW.QFrame()

        #Area de scroll de invitaciones
        self.area_scroll_invitaciones = QW.QScrollArea()
        self.area_scroll_invitaciones.setWidgetResizable(True)
        self.ventana_area_scroll_invitaciones = QW.QWidget()
        self.contenedor_scroll_invitaciones = QW.QVBoxLayout(self.ventana_area_scroll_invitaciones)

        #Botones
        self.boton_iniciar_sesion = QW.QPushButton("Iniciar Sesión")
        self.boton_registrar_usuario = QW.QPushButton("Registrarse")
        self.boton_cerrar_sesion = QW.QPushButton("Cerrar Sesión")
        boton_abrir_buscador_proyectos = QW.QPushButton("Ver más")

        #Acciones de los botones
        boton_abrir_buscador_proyectos.clicked.connect(lambda: self.abrirBuscadorProyectos())
        self.boton_iniciar_sesion.clicked.connect(lambda: self.abrirInicioSesion())
        self.boton_registrar_usuario.clicked.connect(lambda: self.abrirRegistroUsuario())
        self.boton_cerrar_sesion.clicked.connect(lambda: self.cerrarSesion())

        #Etiqueta
        etiqueta_creditos = QW.QLabel("Desarrollado por Bruno Fornasar González")
        etiqueta_invitaciones = QW.QLabel("Invitaciones")
        self.etiqueta_no_invitaciones = QW.QLabel("No se han encontrado resultados")
        #  ¯\_(ツ)_/¯ para usar en algún momento

        #Foto de perfil
        imagen_perfil = QW.QLabel("Inicie Sesión")
        imagen_logo = QW.QLabel("Calera")

        #Agregar widgets al contenedor
        contenedor_proyectos.addWidget(imagen_logo)
        contenedor_perfil.addWidget(imagen_perfil, 2)
        contenedor_perfil.addWidget(self.boton_iniciar_sesion, 2)
        contenedor_perfil.addWidget(self.boton_registrar_usuario, 2)
        contenedor_perfil.addWidget(self.boton_cerrar_sesion, 4)
        self.boton_cerrar_sesion.hide()
        contenedor_proyectos.addWidget(boton_abrir_buscador_proyectos)
        contenedor_proyectos.addWidget(etiqueta_creditos)
        contenedor_invitaciones.addWidget(etiqueta_invitaciones, 2)

        #Agregar contenedores
        contenedor_menu.addWidget(cuadro_contenedor_perfil, 3)
        contenedor_menu.addWidget(cuadro_contenedor_proyectos, 7)
        cuadro_contenedor_perfil.setLayout(contenedor_perfil)
        cuadro_contenedor_proyectos.setLayout(contenedor_proyectos)
        contenedor_perfil.addLayout(contenedor_acciones_perfil, 5)
        contenedor_perfil.addLayout(contenedor_invitaciones, 5)
        contenedor_invitaciones.addWidget(self.area_scroll_invitaciones, 8)
        self.area_scroll_invitaciones.setWidget(self.ventana_area_scroll_invitaciones)
        self.ventana_area_scroll_invitaciones.setLayout(self.contenedor_scroll_invitaciones)

        #Estilos contenedores
        cuadro_contenedor_perfil.setStyleSheet(
            "background-color: #001a40;" \
            "border-radius: 10px;"
        )
        cuadro_contenedor_proyectos.setStyleSheet(
            "background-color: #001a40;" \
            "border-radius: 10px;"
        )
        self.ventana_area_scroll_invitaciones.setStyleSheet(
            """background-color: #000d20;"""
        )

        #Estilos etiquetas
        imagen_perfil.setAlignment(Qt.AlignCenter)
        imagen_perfil.setStyleSheet(
            "font-size: 30px;"
        )
        etiqueta_invitaciones.setAlignment(Qt.AlignCenter)
        etiqueta_invitaciones.setStyleSheet(
            """
            font-size: 20px;
            color: #dfecff;"""
        )
        self.etiqueta_no_invitaciones.setAlignment(Qt.AlignCenter)
        self.etiqueta_no_invitaciones.setStyleSheet(
            """
            color: #dfecff;"""
        )

        #Estilos botones
        estilos_generales_botones = "QPushButton{" \
        "background-color: #004dbf;" \
        "border-radius: 3px;" \
        "color: #dfecff;" \
        "padding: 10px 0px;" \
        "font-size: 15px;" \
        "}" \
        "QPushButton:hover{" \
        "background-color: #00409f;" \
        "}"
        self.boton_iniciar_sesion.setStyleSheet(estilos_generales_botones)
        self.boton_cerrar_sesion.setStyleSheet(estilos_generales_botones)
        self.boton_registrar_usuario.setStyleSheet(estilos_generales_botones)
        boton_abrir_buscador_proyectos.setStyleSheet(estilos_generales_botones)

        #Estilos imágenes
        imagen_logo.setStyleSheet(
            """
            font-size: 100px;
            color: #dfecff;"""
        )
        imagen_logo.setAlignment(Qt.AlignCenter)

        self.show()

    def mostrarInvitaciones(self):
        invitaciones = [(1, "Robot SUMO"), (1, "Robot SUMO")]
        if invitaciones != []:
            for i in invitaciones:
                invitacion = Invitaciones(i[0], i[1])
                self.contenedor_scroll_invitaciones.addWidget(invitacion)
        else:
            self.contenedor_scroll_invitaciones.addWidget(self.etiqueta_no_invitaciones)

    def abrirBuscadorProyectos(self):
        buscador_proyectos = BuscadorProyectos(self.sesion)
    
    def abrirInicioSesion(self):
        # formulario = FormularioInicioSesion(self.sesion)
        self.boton_cerrar_sesion.show()
        self.boton_iniciar_sesion.hide()
        self.boton_registrar_usuario.hide()
        self.mostrarInvitaciones()

    def abrirRegistroUsuario(self):
        # formulario = FormularioRegistro(self.sesion)
        self.boton_cerrar_sesion.show()
        self.boton_iniciar_sesion.hide()
        self.boton_registrar_usuario.hide()

    def cerrarSesion(self):
        self.boton_cerrar_sesion.hide()
        self.boton_iniciar_sesion.show()
        self.boton_registrar_usuario.show()

    def iniciarSesion(self, email, contra):
        self.sesion["nombre"]

class Invitaciones(QW.QFrame):
    def __init__(self, id_invitacion, proyecto):
        super().__init__()

        #Contenedores
        contenedor_central = QW.QVBoxLayout()
        contenedor_botones = QW.QHBoxLayout()
        contenedor_etiquetas = QW.QVBoxLayout()
        
        #Contenedores estilos
        cuadro_contenedor_etiquetas = QW.QFrame()

        #Configurar contenedor central
        self.setLayout(contenedor_central)

        #Etiquetas
        etiqueta_notificacion = QW.QLabel("Te invitaron de...")
        etiqueta_nombre_proyecto = QW.QLabel(proyecto)

        #Botones
        boton_aceptar = QW.QPushButton("Aceptar")
        boton_rechazar = QW.QPushButton("Rechazar")

        #Agregar elementos
        contenedor_botones.addWidget(boton_aceptar)
        contenedor_botones.addWidget(boton_rechazar)
        contenedor_etiquetas.addWidget(etiqueta_notificacion)
        contenedor_etiquetas.addWidget(etiqueta_nombre_proyecto)

        #Agregar contenedores
        contenedor_central.addWidget(cuadro_contenedor_etiquetas)
        contenedor_central.addLayout(contenedor_botones)
        cuadro_contenedor_etiquetas.setLayout(contenedor_etiquetas)

        #Estilos botones 0066ff
        boton_rechazar.setStyleSheet("""QPushButton{
        background-color: #df1300;
        }""")
        boton_aceptar.setStyleSheet("""QPushButton{
        background-color: #00ff1d;
        }
        QPushButton:hover{
        background-color: #00bf16;
        }""")
        

class BuscadorProyectos(QW.QWidget):
    # def __init__(self, /, parent = ..., f = ..., *, modal = ..., windowModality = ..., enabled = ..., geometry = ..., frameGeometry = ..., normalGeometry = ..., x = ..., y = ..., pos = ..., frameSize = ..., size = ..., width = ..., height = ..., rect = ..., childrenRect = ..., childrenRegion = ..., sizePolicy = ..., minimumSize = ..., maximumSize = ..., minimumWidth = ..., minimumHeight = ..., maximumWidth = ..., maximumHeight = ..., sizeIncrement = ..., baseSize = ..., palette = ..., font = ..., cursor = ..., mouseTracking = ..., tabletTracking = ..., isActiveWindow = ..., focusPolicy = ..., focus = ..., contextMenuPolicy = ..., updatesEnabled = ..., visible = ..., minimized = ..., maximized = ..., fullScreen = ..., sizeHint = ..., minimumSizeHint = ..., acceptDrops = ..., windowTitle = ..., windowIcon = ..., windowIconText = ..., windowOpacity = ..., windowModified = ..., toolTip = ..., toolTipDuration = ..., statusTip = ..., whatsThis = ..., accessibleName = ..., accessibleDescription = ..., accessibleIdentifier = ..., layoutDirection = ..., autoFillBackground = ..., styleSheet = ..., locale = ..., windowFilePath = ..., inputMethodHints = ...):
    #     super().__init__(parent, f, modal=modal, windowModality=windowModality, enabled=enabled, geometry=geometry, frameGeometry=frameGeometry, normalGeometry=normalGeometry, x=x, y=y, pos=pos, frameSize=frameSize, size=size, width=width, height=height, rect=rect, childrenRect=childrenRect, childrenRegion=childrenRegion, sizePolicy=sizePolicy, minimumSize=minimumSize, maximumSize=maximumSize, minimumWidth=minimumWidth, minimumHeight=minimumHeight, maximumWidth=maximumWidth, maximumHeight=maximumHeight, sizeIncrement=sizeIncrement, baseSize=baseSize, palette=palette, font=font, cursor=cursor, mouseTracking=mouseTracking, tabletTracking=tabletTracking, isActiveWindow=isActiveWindow, focusPolicy=focusPolicy, focus=focus, contextMenuPolicy=contextMenuPolicy, updatesEnabled=updatesEnabled, visible=visible, minimized=minimized, maximized=maximized, fullScreen=fullScreen, sizeHint=sizeHint, minimumSizeHint=minimumSizeHint, acceptDrops=acceptDrops, windowTitle=windowTitle, windowIcon=windowIcon, windowIconText=windowIconText, windowOpacity=windowOpacity, windowModified=windowModified, toolTip=toolTip, toolTipDuration=toolTipDuration, statusTip=statusTip, whatsThis=whatsThis, accessibleName=accessibleName, accessibleDescription=accessibleDescription, accessibleIdentifier=accessibleIdentifier, layoutDirection=layoutDirection, autoFillBackground=autoFillBackground, styleSheet=styleSheet, locale=locale, windowFilePath=windowFilePath, inputMethodHints=inputMethodHints)
    def __init__(self, sesion: dict):
        super().__init__()
        
        #Datos
        proyectos = [
            ("Robot SUMO", "Electrónica"),
            ("SONUS", "Electrónica"),
            ("Mesa abatible", "Carpintería")
        ]

        #Contenedor central
        contenedor_lista = QW.QVBoxLayout(self)
        # contenedor_solicitudes = QW.QVBoxLayout(self)

        #Etiquetas
        etiqueta_lista_proyectos = QW.QLabel("Proyectos disponibles")
        etiqueta_solicitudes = QW.QLabel("Grupos solicitantes")

        #Botones
        boton_abrir_grupos_proyecto = QW.QPushButton("¿Quiénes participaron?")

        #Acciones de los botones
        boton_abrir_grupos_proyecto.clicked.connect(lambda: self.abrirGruposProyecto())

        #Lista de proyectos
        self.tabla_proyectos = QW.QTableWidget(len(proyectos), 2)
        self.tabla_proyectos.setHorizontalHeaderLabels(["Proyectos", "Tema"])
        self.tabla_proyectos.setSelectionBehavior(QW.QTableWidget.SelectRows)
        self.tabla_proyectos.setSelectionMode(QW.QTableWidget.SingleSelection)

        #Agregar contenido a la tabla
        for fila, (nombre, tema) in enumerate(proyectos):
            self.tabla_proyectos.setItem(fila, 0, QW.QTableWidgetItem(nombre))
            self.tabla_proyectos.setItem(fila, 1, QW.QTableWidgetItem(tema))

        #Agregar elementos al contenedor
        contenedor_lista.addWidget(etiqueta_lista_proyectos)
        contenedor_lista.addWidget(self.tabla_proyectos)
        contenedor_lista.addWidget(boton_abrir_grupos_proyecto)

        self.show()


    def abrirGruposProyecto(self):
        fila = self.tabla_proyectos.currentRow()
        if fila >= 0:
            print(self.tabla_proyectos.item(fila, 0).text())

class GruposProyecto(QW.QWidget):
    def __init__(self, nombre_proyecto):
        super().__init__()
        self.resize(500, 300)
        
        #Datos
        proyectos = [
            (1, "Robot SUMO", True, "robot_sumo.jpeg"),
            (2, "SONUS", True, "proyecto_por_defecto.jpg"),
            (3, "Mesa abatible", True, "robot_sumo.jpeg")
        ]

        #Instancias de los grupos del proyecto
        grupos_proyecto = []

        #Contenedores
        contenedor_central = QW.QVBoxLayout(self)

        #Área de scroll de los grupos
        area_scroll_grupos = QW.QScrollArea()
        area_scroll_grupos.setWidgetResizable(True)

        #Ventana del área scrolleable
        ventana_area_scroll_grupos = QW.QWidget()

        #Contenedor grupos
        contenedor_grupos = QW.QVBoxLayout(ventana_area_scroll_grupos)

        #Ingreso de datos en la lista de instancias
        for i in proyectos:
            grupos_proyecto.append(GrupoDeProyecto(i[0], i[1], i[2], i[3]))
            contenedor_grupos.addLayout(grupos_proyecto[-1])

        #Mostrar elementos
        area_scroll_grupos.setWidget(ventana_area_scroll_grupos)
        contenedor_central.addWidget(area_scroll_grupos)

        self.show()


    def abrirGruposProyecto(self, tabla_proyectos):
        fila = tabla_proyectos.currentRow()
        if fila >= 0:
            print(tabla_proyectos.item(fila, 0).text())

class GrupoDeProyecto(QW.QVBoxLayout):
    def __init__(self, id, nombre, miembro, imagen):
        super().__init__()
        
        #Contenedores
        contenedor_botones = QW.QHBoxLayout()

        #Etiquetas
        etiqueta_nombre = QW.QLabel(nombre)

        #Imágenes
        imagen_proyecto = QW.QLabel()
        imagen_proyecto.resize(50, 170)
        imagen_proyecto.setScaledContents(True)
        mapa_pixeles_imagen_proyecto = QG.QPixmap("./img/" + imagen)
        escalado_mapa_pixeles_imagen_proyecto = mapa_pixeles_imagen_proyecto.scaled(imagen_proyecto.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        imagen_proyecto.setPixmap(escalado_mapa_pixeles_imagen_proyecto)

        #Botones
        boton_ver_proyecto = QW.QPushButton("Ver más")
        boton_administrar_proyecto = QW.QPushButton("Administrar")

        #Acciones de botones
        boton_ver_proyecto.clicked.connect(lambda: self.abrirProyecto(id))
        boton_administrar_proyecto.clicked.connect(lambda: self.abrirAdministradorProyectos(id))

        #Llenar layout de botones
        contenedor_botones.addWidget(boton_ver_proyecto)
        if miembro == True:
            contenedor_botones.addWidget(boton_administrar_proyecto)

        #Llenar contenedor general
        self.addWidget(etiqueta_nombre)
        self.addWidget(imagen_proyecto)
        self.addLayout(contenedor_botones)

    def abrirProyecto(self, id_grupo):
        print("Abrir proyecto " + str(id_grupo))

    def abrirAdministradorProyectos(self, id_grupo):
        print("Abrir el administrador de proyectos " + str(id_grupo))

class FormularioRegistro(QW.QWidget):
    def __init__(self, sesion: dict):
        super().__init__()

        self.setWindowTitle("Inicio de Sesión")
        self.sesion = sesion
        
        #contenedor_central
        contenedor_central = QW.QVBoxLayout(self)
        contenedor_formulario = QW.QFormLayout()

        #Título del formulario
        etiqueta_titulo_formulario = QW.QLabel("Registro de usuario")
        etiqueta_titulo_formulario.setAlignment(Qt.AlignCenter)
        etiqueta_titulo_formulario.setStyleSheet(
            "font-size: 20px;" \
            "text-align: center;" \
            "background-color: #999;"
        )

        #Entradas de datos
        self.entrada_nombre = QW.QLineEdit()
        self.entrada_email = QW.QLineEdit()
        self.entrada_contra = QW.QLineEdit()
        self.entrada_contra.setEchoMode(QW.QLineEdit.Password)

        #Botón
        boton_enviar_formulario = QW.QPushButton("¡Registrarme!")
        boton_enviar_formulario.clicked.connect(lambda: self.enviarFormulario(self.sesion))

        #Mostrar Las columnas y filas
        contenedor_central.addWidget(etiqueta_titulo_formulario)
        contenedor_central.addLayout(contenedor_formulario)
        contenedor_formulario.addRow("Nombre: ", self.entrada_nombre)
        contenedor_formulario.addRow("Correo electrónico: ", self.entrada_email)
        contenedor_formulario.addRow("Contraseña: ", self.entrada_contra)
        contenedor_central.addWidget(boton_enviar_formulario)

        self.show()

    def enviarFormulario(self, sesion):
        print(self.entrada_contra.text())

class FormularioInicioSesion(QW.QWidget):
    def __init__(self, sesion: dict):
        super().__init__()

        self.setWindowTitle("Inicio de Sesión")
        
        #contenedor_central
        contenedor_central = QW.QVBoxLayout(self)
        contenedor_formulario = QW.QFormLayout()

        #Título del formulario
        etiqueta_titulo_formulario = QW.QLabel("Registro de usuario")
        etiqueta_titulo_formulario.setAlignment(Qt.AlignCenter)
        etiqueta_titulo_formulario.setStyleSheet(
            "font-size: 20px;" \
            "text-align: center;" \
            "background-color: #999;"
        )

        #Entradas de datos
        self.entrada_email = QW.QLineEdit()
        self.entrada_contra = QW.QLineEdit()
        self.entrada_contra.setEchoMode(QW.QLineEdit.Password)

        #Botón
        boton_enviar_formulario = QW.QPushButton("¡Registrarme!")
        boton_enviar_formulario.clicked.connect(lambda: self.enviarFormulario(self.sesion))

        #Mostrar Las columnas y filas
        contenedor_central.addWidget(etiqueta_titulo_formulario)
        contenedor_central.addLayout(contenedor_formulario)
        contenedor_formulario.addRow("Correo electrónico: ", self.entrada_email)
        contenedor_formulario.addRow("Contraseña: ", self.entrada_contra)
        contenedor_central.addWidget(boton_enviar_formulario)

        self.show()

    def enviarFormulario(self, sesion):
        print("Hola")

class FormularioCreacionProyecto(QW.QWidget):
    def __init__(self, sesion: dict):
        super().__init__()

        self.setWindowTitle("Inicio de Sesión")
        
        #contenedor_central
        contenedor_central = QW.QVBoxLayout(self)
        contenedor_formulario = QW.QFormLayout()

        #Título del formulario
        etiqueta_titulo_formulario = QW.QLabel("Registro de usuario")
        etiqueta_titulo_formulario.setAlignment(Qt.AlignCenter)
        etiqueta_titulo_formulario.setStyleSheet(
            "font-size: 20px;" \
            "text-align: center;" \
            "background-color: #999;"
        )

        #Entradas de datos
        self.entrada_nombre = QW.QLineEdit()
        self.entrada_email = QW.QLineEdit()
        self.entrada_contra = QW.QLineEdit()
        self.entrada_contra.setEchoMode(QW.QLineEdit.Password)

        #Botón
        boton_enviar_formulario = QW.QPushButton("¡Registrarme!")
        boton_enviar_formulario.clicked.connect(lambda: self.enviarFormulario(self.sesion))

        #Mostrar Las columnas y filas
        contenedor_central.addWidget(etiqueta_titulo_formulario)
        contenedor_central.addLayout(contenedor_formulario)
        contenedor_formulario.addRow("Nombre: ", self.entrada_nombre)
        contenedor_formulario.addRow("Correo electrónico: ", self.entrada_email)
        contenedor_formulario.addRow("Contraseña: ", self.entrada_contra)
        contenedor_central.addWidget(boton_enviar_formulario)

        self.show()

    def enviarFormulario(self, sesion):
        print("Hola")

class PanelAdministradorGrupos(QW.QWidget):
    def __init__(self, sesion: dict):
        super().__init__()

        #Datos
        self.sesion = sesion
        miembros = (
            (1, "Bruno Fornasar", "activo"),
            (2, "Pepito lol", "activo"),
            (3, "Ferrusio xd", "pendiente"),
            (4, "Jorgito jaja", "pendiente"),
            (5, "Camil gol", "rechazado")
        )

        no_miembros = (
            (1, "Bruno Fornasar"),
            (2, "Pepito lol"),
            (3, "Ferrusio xd"),
            (4, "Jorgito jaja"),
            (5, "Camil gol")
        )
        
        #Contenedores
        contenedor_general = QW.QHBoxLayout(self)
        contenedor_tabla_miembros = QW.QVBoxLayout()
        contenedor_tabla_no_miembros = QW.QVBoxLayout()

        #Botones


        #Tablas
        self.tabla_miembros = QW.QTableWidget(len(miembros), 3)
        self.tabla_no_miembros = QW.QTableWidget(len(no_miembros), 2)

        #Configurar las cabeceras de las tablas
        self.tabla_miembros.setHorizontalHeaderLabels(["ID", "Nombre", "Estado"])
        self.tabla_no_miembros.setHorizontalHeaderLabels(["ID", "Nombre"])

        #Configurar modo de selección de las tablas para que solo se pueda seleccionar una fila a la vez
        self.tabla_miembros.setSelectionBehavior(QW.QTableWidget.SelectRows)
        self.tabla_miembros.setSelectionMode(QW.QTableWidget.SingleSelection)
        self.tabla_no_miembros.setSelectionBehavior(QW.QTableWidget.SelectRows)
        self.tabla_no_miembros.setSelectionMode(QW.QTableWidget.SingleSelection)

        #Llenar las tablas
        for fila, (identificador, nombre, estado) in enumerate(miembros):
            self.tabla_miembros.setItem(fila, 0, QW.QTableWidgetItem(str(identificador)))
            self.tabla_miembros.setItem(fila, 1, QW.QTableWidgetItem(nombre))
            self.tabla_miembros.setItem(fila, 2, QW.QTableWidgetItem(estado))
            self.tabla_miembros.item(fila, 0).setTextAlignment(Qt.AlignCenter)
        for fila, (identificador, nombre) in enumerate(no_miembros):
            self.tabla_no_miembros.setItem(fila, 0, QW.QTableWidgetItem(str(identificador)))
            self.tabla_no_miembros.setItem(fila, 1, QW.QTableWidgetItem(nombre))
            self.tabla_no_miembros.item(fila, 0).setTextAlignment(Qt.AlignCenter)

        #Estilos de la tabla
        # self.tabla_miembros.item(fila, 0).setS

        #Mostrar elementos
        contenedor_general.addLayout(contenedor_tabla_miembros, 6)
        contenedor_general.addLayout(contenedor_tabla_no_miembros, 4)
        contenedor_tabla_miembros.addWidget(self.tabla_miembros)
        contenedor_tabla_no_miembros.addWidget(self.tabla_no_miembros)

        self.show()

class Presentacion(QW.QWidget):
    def __init__(self, sesion):
        super().__init__()

        #Sesion
        editar = sesion["editar"]

        #Datos
        datos = (1, "Robot SUMO", "imagen", "principal")

        #Datos de contenido de proyectos
        datos_contenido = [
            (0, "Encabezado", "Descripcion"),
            (0, "Encabezado", "Descripcion"),
            (0, "Encabezado", "Descripcion")
        ]

        #Instancias de los contenidos del proyecto
        contenidos = []
        
        #Imagen principal en caso de ser presentacion principal
        if datos != None:
            if datos[3] == "principal":
                imagen_proyecto = QW.QLabel()
                imagen_proyecto.resize(50, 170)
                imagen_proyecto.setScaledContents(True)
                mapa_pixeles_imagen_proyecto = QG.QPixmap("./img/" + datos[2])
                imagen_proyecto.setPixmap(mapa_pixeles_imagen_proyecto)

        #Opciones de edicion
        if editar == True:
            self.habilitar_edicion = QW.QCheckBox("Habilitar edicion")

        #Titulo
        etiqueta = QW.QLabel(datos[1])

class ContenidoPresentacion(QW.QWidget):
    def __init__(self, id, encabezado, desc, imagen, editar):
        super().__init__()

        #Contenedores
        contenedor_ventana = QW.QHBoxLayout(self)
        contenedor_central = QW.QHBoxLayout()
        self.contenedor_contenido = QW.QVBoxLayout()
        contenedor_imagen = QW.QVBoxLayout()

        #Contenedores estilos
        contenedor_estilos_contenido = QW.QFrame()

        #Etiquetas
        self.etiqueta_encabezado = QW.QLabel(encabezado)
        self.etiqueta_descripcion = QW.QLabel(desc)

        #Imagen
        if imagen != None:
            imagen_complementaria = QW.QLabel()
            imagen_complementaria.resize(50, 50)
            imagen_complementaria.setScaledContents(True)
            mapa_pixeles_imagen_complementaria = QG.QPixmap("./img/" + imagen)
            imagen_complementaria.setPixmap(mapa_pixeles_imagen_complementaria)

        #Opciones editor
        if editar == True:
            #Botones
            boton_color_letra = QW.QPushButton("Cambiar color de la letra")
            boton_color_letra.clicked.connect(lambda: self.abrirSelectorColorLetra())
            
            #Colores
            self.color_letra = QW.QColorDialog()
            self.color_letra.currentColorChanged.connect(lambda: self.cambiarColorLetra())


        #Agregar Widgets
        self.contenedor_contenido.addWidget(self.etiqueta_encabezado)
        self.contenedor_contenido.addWidget(self.etiqueta_descripcion)
        self.contenedor_contenido.addWidget(boton_color_letra)

        #Agregar contenedores
        contenedor_ventana.addWidget(contenedor_estilos_contenido)
        contenedor_estilos_contenido.setLayout(contenedor_central)
        contenedor_central.addLayout(self.contenedor_contenido)
        contenedor_central.addLayout(contenedor_imagen)
            
        self.show()

    def mostrarModoEdicion(self):
        print()

    def abrirSelectorColorLetra(self):
        self.color_letra.getColor(initial=QG.QColor(255, 0, 0), parent=self.contenedor_contenido, title="Color letra", options=QW.QColorDialog.ColorDialogOption.DontUseNativeDialog)
        print(self.color_letra.currentColor())

    def cambiarColorLetra(self):
        print("HOLAAAAA")
        print(self.color_letra.currentColor())
        # self.etiqueta_encabezado.setStyleSheet("color:")