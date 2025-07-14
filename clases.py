from PySide6 import QtWidgets as QW
from PySide6 import QtGui as QG
from PySide6.QtCore import Qt
from sistema import ConexionBaseDeDatos

class VentanaPrincipal(QW.QMainWindow):
    def __init__(self, sesion):
        super().__init__()
        self.resize(768, 450)
        self.setStyleSheet(
            "background-color: #000d20;"
        )
        self.setWindowTitle("Calera")

        #Datos de sesion
        self.sesion = sesion

        
        conexion = ConexionBaseDeDatos()
        proyectos = conexion.obtener_proyectos_usuario()

        #Contenedor central
        contenedor_central = QW.QWidget(self)
        self.setCentralWidget(contenedor_central)
        
        #Contenedor general de los objetos
        contenedor_menu = QW.QHBoxLayout(contenedor_central)
        contenedor_perfil = QW.QVBoxLayout()
        contenedor_proyectos = QW.QVBoxLayout()
        contenedor_acciones_perfil = QW.QVBoxLayout()
        contenedor_invitaciones = QW.QVBoxLayout()
        ventana_botones_proyectos = QW.QWidget()
        contenedor_botones_proyectos = QW.QHBoxLayout(ventana_botones_proyectos)

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
        self.boton_administrador = QW.QPushButton("Administrar")
        boton_abrir_buscador_proyectos = QW.QPushButton("Ver más")
        boton = QW.QPushButton(proyectos[1])

        #Acciones de los botones
        boton_abrir_buscador_proyectos.clicked.connect(lambda: self.abrirBuscadorProyectos())
        self.boton_iniciar_sesion.clicked.connect(lambda: self.abrirInicioSesion())
        self.boton_registrar_usuario.clicked.connect(lambda: self.abrirRegistroUsuario())
        self.boton_cerrar_sesion.clicked.connect(lambda: self.cerrarSesion())
        self.boton_administrador.clicked.connect(lambda: self.abrirPanelAdministrador())

        #Etiqueta
        etiqueta_creditos = QW.QLabel("Desarrollado por Bruno Fornasar González")
        etiqueta_invitaciones = QW.QLabel("Invitaciones")
        self.etiqueta_no_invitaciones = QW.QLabel("No se han encontrado resultados")
        #  ¯\_(ツ)_/¯ para usar en algún momento

        #Foto de perfil
        self.imagen_perfil = QW.QLabel("Inicie Sesión")
        imagen_logo = QW.QLabel("Calera")

        #Agregar widgets al contenedor
        contenedor_proyectos.addWidget(imagen_logo)
        contenedor_proyectos.addWidget(ventana_botones_proyectos)  # Justo antes del boton "ver mas"
        contenedor_perfil.addWidget(self.imagen_perfil, 2)
        contenedor_perfil.addWidget(self.boton_iniciar_sesion, 2)
        contenedor_perfil.addWidget(self.boton_registrar_usuario, 2)
        contenedor_perfil.addWidget(self.boton_cerrar_sesion, 4)
        contenedor_perfil.addWidget(self.boton_administrador, 4)
        self.boton_cerrar_sesion.hide()
        self.boton_administrador.hide()
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
        self.imagen_perfil.setAlignment(Qt.AlignCenter)
        self.imagen_perfil.setStyleSheet(
            "font-size: 30px;" \
            "color: #dfecff;"
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
        etiqueta_creditos.setStyleSheet("color: #dfecff;")
        etiqueta_creditos.setAlignment(Qt.AlignBottom)

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
        self.boton_administrador.setStyleSheet(estilos_generales_botones)
        self.boton_registrar_usuario.setStyleSheet(estilos_generales_botones)
        boton_abrir_buscador_proyectos.setStyleSheet(estilos_generales_botones)
        boton.setStyleSheet(estilos_generales_botones)

        #Estilos imágenes
        imagen_logo.setStyleSheet(
            """
            font-size: 100px;
            color: #dfecff;"""
        )
        imagen_logo.setAlignment(Qt.AlignCenter)

        self.iniciarSesion()

        

        if proyectos[2]:
            pixmap = QG.QPixmap("./img/" + proyectos[2])
            icono = QG.QIcon(pixmap)
            boton.setIcon(icono)

        boton.clicked.connect(lambda _, id=proyectos[0], nombre=proyectos[1]: self.abrir_presentacion_proyecto(id, nombre))
        contenedor_botones_proyectos.addWidget(boton)

        self.show()

    def mostrarInvitaciones(self):
        conexion = ConexionBaseDeDatos()
        invitaciones = conexion.obtener_invitaciones(self.sesion["id"])
        if invitaciones != []:
            for i in invitaciones:
                invitacion = Invitaciones(i[0], i[1])
                self.contenedor_scroll_invitaciones.addWidget(invitacion)
        else:
            self.contenedor_scroll_invitaciones.addWidget(self.etiqueta_no_invitaciones)
    
    def ocultarInvitaciones(self):
        for i in range(self.contenedor_scroll_invitaciones.count()):
            self.contenedor_scroll_invitaciones.itemAt(i).widget().hide()

    def abrirBuscadorProyectos(self):
        self.close()
        self.buscador = BuscadorProyectos(self.sesion)
    
    def abrirInicioSesion(self):
        self.close()
        self.form = FormularioInicioSesion(self.sesion)

    def abrirRegistroUsuario(self):
        self.close()
        self.form = FormularioRegistro(self.sesion)

    def abrirPanelAdministrador(self):
        self.close()
        self.panel = TablaUsuarios(self.sesion)

    def cerrarSesion(self):
        self.boton_cerrar_sesion.hide()
        self.boton_administrador.hide()
        self.boton_iniciar_sesion.show()
        self.boton_registrar_usuario.show()
        self.imagen_perfil.setText("Inicie Sesión")
        self.ocultarInvitaciones()
        self.sesion = {
            "id": 0,
            "nombre": "",
            "permiso": "UE"
        }

    def iniciarSesion(self):
        if self.sesion["id"] != 0:
            self.boton_cerrar_sesion.show()
            if self.sesion["permiso"] == "AD":
                self.boton_administrador.show()
            self.boton_iniciar_sesion.hide()
            self.boton_registrar_usuario.hide()
            self.imagen_perfil.setText("Hola, " + self.sesion["nombre"])
            self.mostrarInvitaciones()

    # Método para abrir presentación

    def abrir_presentacion_proyecto(self, id_proyecto, nombre):
        self.close()
        self.ventana_presentacion = GruposProyecto(nombre, id_proyecto, self.sesion)
        self.ventana_presentacion.show()


class Invitaciones(QW.QFrame):
    def __init__(self, id_invitacion, proyecto):
        super().__init__()

        self.setStyleSheet(
            """
            background-color: #001a40;
            border-radius: 10px;
            """
        )

        self.conexion = ConexionBaseDeDatos()

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

        #Acciones botones
        boton_aceptar.clicked.connect(lambda: self.aceptarInvitacion(id_invitacion))
        boton_rechazar.clicked.connect(lambda: self.rechazarInvitacion(id_invitacion))

        #Agregar elementos
        contenedor_botones.addWidget(boton_aceptar)
        contenedor_botones.addWidget(boton_rechazar)
        contenedor_etiquetas.addWidget(etiqueta_notificacion)
        contenedor_etiquetas.addWidget(etiqueta_nombre_proyecto)

        #Agregar contenedores
        contenedor_central.addWidget(cuadro_contenedor_etiquetas)
        contenedor_central.addLayout(contenedor_botones)
        cuadro_contenedor_etiquetas.setLayout(contenedor_etiquetas)

        #Estilos botones
        boton_rechazar.setStyleSheet("""QPushButton{
        background-color: #df1300;
        }""")
        boton_aceptar.setStyleSheet("""QPushButton{
        background-color: #00ff1d;
        }
        QPushButton:hover{
        background-color: #00bf16;
        }""")

        #Estilos etiquetas
        self.resize(50, 50)
        etiqueta_notificacion.setStyleSheet("color: #dfecff;")
        etiqueta_notificacion.setAlignment(Qt.AlignCenter)
        etiqueta_nombre_proyecto.setStyleSheet("color: #dfecff;")
        etiqueta_nombre_proyecto.setAlignment(Qt.AlignCenter)

    def aceptarInvitacion(self, id_invitacion):
        self.conexion.aceptar_invitacion(id_invitacion)
        self.hide()
        self.close()

    def rechazarInvitacion(self, id_invitacion):
        self.conexion.rechazar_invitacion(id_invitacion)
        self.hide()
        self.close()
        
class BuscadorProyectos(QW.QWidget):
    def __init__(self, sesion: dict):
        super().__init__()
        self.setStyleSheet("background-color: #001a40;")
        self.resize(350, 350)

        self.sesion = sesion
        self.conexion = ConexionBaseDeDatos()

        # Datos
        proyectos = self.conexion.obtener_proyectos_para_buscador()

        # Contenedor central
        contenedor_lista = QW.QVBoxLayout(self)

        # Header de navegación
        header = QW.QHBoxLayout()
        boton_volver = QW.QPushButton("Inicio")
        boton_volver.clicked.connect(self.volverInicio)
        boton_volver.setStyleSheet(self.estilo_boton())
        header.addWidget(boton_volver, alignment=Qt.AlignmentFlag.AlignLeft)
        boton_crear_nuevo_proyecto = QW.QPushButton("Crear Proyecto")
        boton_crear_nuevo_proyecto.clicked.connect(self.abrirFormularioCrearProyecto)
        boton_crear_nuevo_proyecto.setStyleSheet(self.estilo_boton())
        header.addWidget(boton_crear_nuevo_proyecto, alignment=Qt.AlignmentFlag.AlignLeft)
        if self.sesion["permiso"] == "UE":
            boton_crear_nuevo_proyecto.hide()
        contenedor_lista.addLayout(header)

        if proyectos:
            # Etiqueta principal
            etiqueta_lista_proyectos = QW.QLabel("Proyectos disponibles")
            etiqueta_lista_proyectos.setStyleSheet("color: #dfecff; font-size: 25px;")
            etiqueta_lista_proyectos.setAlignment(Qt.AlignmentFlag.AlignCenter)

            # Tabla de proyectos
            self.tabla_proyectos = QW.QTableWidget(len(proyectos), 2)
            self.tabla_proyectos.setHorizontalHeaderLabels(["Proyectos", "Tema"])
            self.tabla_proyectos.setEditTriggers(QW.QAbstractItemView.NoEditTriggers)
            self.tabla_proyectos.setSelectionBehavior(QW.QTableWidget.SelectRows)
            self.tabla_proyectos.setSelectionMode(QW.QTableWidget.SingleSelection)
            self.tabla_proyectos.setStyleSheet(
                "background-color: #000d20; color: #dfecff; gridline-color: #dfecff;"
            )
            self.tabla_proyectos.horizontalHeader().setStretchLastSection(False)
            self.tabla_proyectos.setColumnWidth(0, int(self.width() * 0.6))

            for fila, (nombre, tema, _) in enumerate(proyectos):
                self.tabla_proyectos.setItem(fila, 0, QW.QTableWidgetItem(nombre))
                self.tabla_proyectos.setItem(fila, 1, QW.QTableWidgetItem(tema))

            # Botón para abrir grupos del proyecto
            boton_abrir_grupos_proyecto = QW.QPushButton("¿Quiénes participaron?")
            boton_abrir_grupos_proyecto.setStyleSheet(self.estilo_boton())
            boton_abrir_grupos_proyecto.clicked.connect(lambda: self.abrirGruposProyecto(proyectos))

            # Agregar widgets
            contenedor_lista.addWidget(etiqueta_lista_proyectos)
            contenedor_lista.addWidget(self.tabla_proyectos)
            contenedor_lista.addWidget(boton_abrir_grupos_proyecto)
        else:
            etiqueta_vacio = QW.QLabel("No hay proyectos registrados")
            etiqueta_vacio.setAlignment(Qt.AlignmentFlag.AlignCenter)
            etiqueta_vacio.setStyleSheet("color: #dfecff; font-size: 20px;")
            contenedor_lista.addWidget(etiqueta_vacio)

        self.show()

    def estilo_boton(self):
        return (
            "QPushButton {"
            "background-color: #004dbf;"
            "border-radius: 3px;"
            "color: #dfecff;"
            "padding: 10px;"
            "}"
            "QPushButton:hover {"
            "background-color: #00409f;"
            "}"
        )
    
    def abrirFormularioCrearProyecto(self):
        self.close()
        self.form = FormularioNuevoProyecto(self.sesion)

    def abrirGruposProyecto(self, proyectos):
        fila = self.tabla_proyectos.currentRow()
        if fila >= 0:
            nombre = self.tabla_proyectos.item(fila, 0).text()
            id_proyecto = proyectos[fila][2]
            self.close()
            self.grupo = GruposProyecto(nombre, id_proyecto, self.sesion)

    def volverInicio(self):
        self.close()
        self.ventana = VentanaPrincipal(self.sesion)

class GruposProyecto(QW.QWidget):
    def __init__(self, nombre_proyecto, id_proyecto, sesion):
        super().__init__()
        self.setStyleSheet("background-color: #000d20;")
        self.resize(600, 400)

        self.sesion = sesion
        self.id_proyecto = id_proyecto
        self.conexion = ConexionBaseDeDatos()

        # Datos (simulados)
        proyectos = self.conexion.obtener_grupos_proyectos(id_proyecto)

        contenedor_central = QW.QVBoxLayout(self)

        # Header
        header = QW.QHBoxLayout()
        boton_volver = QW.QPushButton("Volver")
        boton_volver.setStyleSheet("""
            QPushButton {
                background-color: #004dbf;
                color: #dfecff;
                border-radius: 3px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #00409f;
            }
        """)
        boton_volver.clicked.connect(self.volverInicio)
        header.addWidget(boton_volver, alignment=Qt.AlignLeft)
        boton_inscribirse = QW.QPushButton("Inscribirse")
        boton_inscribirse.setStyleSheet("""
            QPushButton {
                background-color: #104dbf;
                color: #dfecff;
                border-radius: 3px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #00409f;
            }
        """)
        boton_inscribirse.clicked.connect(self.abrirFormularioInscripcion)
        header.addWidget(boton_inscribirse, alignment=Qt.AlignLeft)
        contenedor_central.addLayout(header)

        # Título
        etiqueta_titulo = QW.QLabel(nombre_proyecto)
        etiqueta_titulo.setStyleSheet("color: #dfecff; font-size: 30px;")
        etiqueta_titulo.setAlignment(Qt.AlignCenter)
        contenedor_central.addWidget(etiqueta_titulo)

        # Scroll area
        area_scroll = QW.QScrollArea()
        area_scroll.setWidgetResizable(True)
        ventana_scroll = QW.QWidget()
        layout_scroll = QW.QVBoxLayout(ventana_scroll)

        # Agregar grupos
        for i in proyectos:
            if self.conexion.es_administrador(i[3], self.sesion["id"]) != None:
                miembro = True
            else:
                miembro = False
            grupo = GrupoDeProyecto(i[3], i[1], miembro, i[2], i[0], self.sesion)
            layout_scroll.addLayout(grupo)

        area_scroll.setWidget(ventana_scroll)
        contenedor_central.addWidget(area_scroll)
        self.show()

    def volverInicio(self):
        self.close()
        VentanaPrincipal(self.sesion)

    def abrirFormularioInscripcion(self):
        self.close()
        self.form = FormularioNuevoGrupo(self.sesion, self.id_proyecto)


class GrupoDeProyecto(QW.QVBoxLayout):
    def __init__(self, id, nombre, miembro, imagen, id_grupo, sesion):
        super().__init__()

        self.sesion = sesion

        # Contenedor principal
        contenedor_principal = QW.QFrame()
        contenedor_principal.setStyleSheet("""
            background-color: #001a40;
            border-radius: 10px;
        """)
        layout_contenedor = QW.QVBoxLayout(contenedor_principal)

        # Etiqueta
        etiqueta_nombre = QW.QLabel(nombre)
        etiqueta_nombre.setStyleSheet("color: #dfecff; font-size: 20px;")
        etiqueta_nombre.setAlignment(Qt.AlignCenter)

        # Imagen
        imagen_proyecto = QW.QLabel()
        imagen_proyecto.resize(200, 170)
        imagen_proyecto.setScaledContents(True)
        pixmap = QG.QPixmap("./img/" + imagen)
        pixmap = pixmap.scaled(imagen_proyecto.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        imagen_proyecto.setPixmap(pixmap)

        # Botones
        boton_ver_proyecto = QW.QPushButton("Ver más")
        boton_administrar = QW.QPushButton("Administrar")

        estilo_boton = """
            QPushButton {
                background-color: #004dbf;
                color: #dfecff;
                border-radius: 3px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #00409f;
            }
        """
        boton_ver_proyecto.setStyleSheet(estilo_boton)
        boton_administrar.setStyleSheet(estilo_boton)

        boton_ver_proyecto.clicked.connect(lambda: self.abrirProyecto(id_grupo, sesion, miembro, id))
        boton_administrar.clicked.connect(lambda: self.abrirAdministradorProyectos(id))

        layout_botones = QW.QHBoxLayout()
        layout_botones.addWidget(boton_ver_proyecto)
        if miembro:
            layout_botones.addWidget(boton_administrar)

        layout_contenedor.addWidget(etiqueta_nombre)
        layout_contenedor.addWidget(imagen_proyecto)
        layout_contenedor.addLayout(layout_botones)

        self.addWidget(contenedor_principal)

        self.ventana = ""

    def abrirProyecto(self, id_grupo, sesion, miembro, id_presentacion):
        self.parentWidget().parentWidget().parentWidget().parentWidget().close()
        Presentacion(self.sesion, id_grupo, miembro, id_presentacion)

    def abrirAdministradorProyectos(self, id_grupo):
        self.parentWidget().parentWidget().parentWidget().parentWidget().close()
        self.ventana = AdministradorProyecto(self.sesion, id_grupo)


class FormularioRegistro(QW.QWidget):
    def __init__(self, sesion: dict):
        super().__init__()
        self.setWindowTitle("Registro de Usuario")
        self.sesion = sesion
        self.setStyleSheet("background-color: #000d20;")

        # Header
        header = QW.QHBoxLayout()
        boton_volver = QW.QPushButton("Volver")
        boton_volver.clicked.connect(self.volver_a_principal)
        boton_volver.setStyleSheet(self.estilo_boton())
        header.addWidget(boton_volver)
        header.addStretch()

        # Contenedor central
        contenedor_central = QW.QVBoxLayout(self)
        contenedor_formulario = QW.QFormLayout()

        # Titulo
        etiqueta_titulo = QW.QLabel("Registro de usuario")
        etiqueta_titulo.setAlignment(Qt.AlignCenter)
        etiqueta_titulo.setStyleSheet("color: #dfecff; font-size: 20px;")

        # Entradas
        self.entrada_nombre = QW.QLineEdit()
        self.entrada_email = QW.QLineEdit()
        self.entrada_contra = QW.QLineEdit()
        for entrada in [self.entrada_nombre, self.entrada_email, self.entrada_contra]:
            entrada.setMinimumHeight(20)
            entrada.setStyleSheet("""
            color: #dfecff;""")
        self.entrada_contra.setEchoMode(QW.QLineEdit.Password)

        # Boton
        boton_enviar = QW.QPushButton("¡Registrarme!")
        boton_enviar.setStyleSheet(self.estilo_boton())
        boton_enviar.clicked.connect(lambda: self.enviarFormulario(self.sesion))

        # Agregar elementos
        contenedor_central.addLayout(header)
        contenedor_central.addWidget(etiqueta_titulo)
        contenedor_central.addLayout(contenedor_formulario)
        contenedor_formulario.addRow("Nombre: ", self.entrada_nombre)
        contenedor_formulario.addRow("Correo electrónico: ", self.entrada_email)
        contenedor_formulario.addRow("Contraseña: ", self.entrada_contra)
        contenedor_central.addWidget(boton_enviar)

        self.show()

    def estilo_boton(self):
        return (
            "QPushButton{"
            "background-color: #004dbf;"
            "border-radius: 3px;"
            "color: #dfecff;"
            "padding: 10px 10px;"
            "}"
            "QPushButton:hover{"
            "background-color: #00409f;"
            "}"
        )

    def enviarFormulario(self, sesion):
        nombre = self.entrada_nombre.text()
        email = self.entrada_email.text()
        contra = self.entrada_contra.text()

        conexion = ConexionBaseDeDatos()
        conexion.registrar_usuario(nombre, email, contra)

        self.close()
        self.ventana = FormularioInicioSesion(sesion)

    def volver_a_principal(self):
        self.close()
        self.ventana = VentanaPrincipal(self.sesion)


class FormularioInicioSesion(QW.QWidget):
    def __init__(self, sesion: dict):
        super().__init__()
        self.setWindowTitle("Inicio de Sesión")
        self.sesion = sesion
        self.setStyleSheet("background-color: #000d20;")

        # Header
        header = QW.QHBoxLayout()
        boton_volver = QW.QPushButton("Volver")
        boton_volver.clicked.connect(self.volver_a_principal)
        boton_volver.setStyleSheet(self.estilo_boton())
        header.addWidget(boton_volver)
        header.addStretch()

        # Contenedor central
        contenedor_central = QW.QVBoxLayout(self)
        contenedor_formulario = QW.QFormLayout()

        # Titulo
        etiqueta_titulo = QW.QLabel("Inicio de Sesión")
        etiqueta_titulo.setAlignment(Qt.AlignCenter)
        etiqueta_titulo.setStyleSheet("color: #dfecff; font-size: 20px;")

        # Entradas
        self.entrada_nombre = QW.QLineEdit()
        self.entrada_email = QW.QLineEdit()
        self.entrada_contra = QW.QLineEdit()
        for entrada in [self.entrada_email, self.entrada_contra]:
            entrada.setMinimumHeight(20)
            entrada.setStyleSheet("""
            color: #dfecff;""")
        self.entrada_contra.setEchoMode(QW.QLineEdit.Password)

        # Boton
        boton_enviar = QW.QPushButton("Iniciar Sesión")
        boton_enviar.setStyleSheet(self.estilo_boton())
        boton_enviar.clicked.connect(lambda: self.enviarFormulario(self.sesion))

        # Agregar elementos
        contenedor_central.addLayout(header)
        contenedor_central.addWidget(etiqueta_titulo)
        contenedor_central.addLayout(contenedor_formulario)
        contenedor_formulario.addRow("Correo electrónico: ", self.entrada_email)
        contenedor_formulario.addRow("Contraseña: ", self.entrada_contra)
        contenedor_central.addWidget(boton_enviar)

        self.etiqueta_error = QW.QLabel("No se pudo iniciar sesión")
        self.etiqueta_error.setStyleSheet("color: red;")
        self.etiqueta_error.setAlignment(Qt.AlignCenter)
        self.etiqueta_error.hide()
        self.layout().insertWidget(3, self.etiqueta_error)

        self.show()

    def estilo_boton(self):
        return (
            "QPushButton{"
            "background-color: #004dbf;"
            "border-radius: 3px;"
            "color: #dfecff;"
            "padding: 10px 10px;"
            "}"
            "QPushButton:hover{"
            "background-color: #00409f;"
            "}"
        )

    def enviarFormulario(self, sesion):
        email = self.entrada_email.text()
        contra = self.entrada_contra.text()

        conexion = ConexionBaseDeDatos()
        datos = conexion.obtener_usuario(email, contra)  # Se espera que esto retorne (id, nombre, permiso)

        if datos:
            sesion["id"] = datos[0]
            sesion["nombre"] = datos[2]
            sesion["permiso"] = datos[3]

            self.close()
            self.ventana = VentanaPrincipal(sesion)
        else:
            self.etiqueta_error.show()

    def volver_a_principal(self):
        self.close()
        self.ventana = VentanaPrincipal(self.sesion)


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
    def __init__(self, sesion, id, miembro, id_presentacion):
        super().__init__()

        self.resize(800, 500)
        self.setStyleSheet("background-color: #000d20;")
        self.sesion = sesion
        self.id = id
        self.miembro = miembro
        self.id_grupo = id_presentacion
        self.conexion = ConexionBaseDeDatos()

        self.presentaciones = self.conexion.obtener_presentaciones_hermanas(id)
        datos = self.conexion.obtener_datos_presentacion(id)
        print(self.id_grupo, id)
        self.setWindowTitle(datos[1])
        datos_contenido = self.conexion.obtener_contenido_presentacion(id)
        self.contenidos = []

        layout_principal = QW.QVBoxLayout(self)

        header = QW.QHBoxLayout()
        boton_volver_buscador = QW.QPushButton("Volver a Buscador")
        boton_volver_principal = QW.QPushButton("Volver al Inicio")

        estilo_boton = ("QPushButton {"
                        "background-color: #004dbf;"
                        "border-radius: 3px;"
                        "color: #dfecff;"
                        "padding: 5px 10px;"
                        "}"
                        "QPushButton:hover {"
                        "background-color: #00409f;"
                        "}")

        boton_volver_buscador.setStyleSheet(estilo_boton)
        boton_volver_principal.setStyleSheet(estilo_boton)

        boton_volver_buscador.clicked.connect(self.abrirBuscador)
        boton_volver_principal.clicked.connect(self.abrirPrincipal)

        header.addWidget(boton_volver_buscador)
        header.addStretch()
        header.addWidget(boton_volver_principal)

        layout_principal.addLayout(header)

        contenedor_general = QW.QHBoxLayout()
        barra_lateral = QW.QVBoxLayout()

        etiqueta_barra = QW.QLabel("Otras presentaciones")
        etiqueta_barra.setStyleSheet("font-size: 18px; color: #dfecff;")
        etiqueta_barra.setAlignment(Qt.AlignCenter)
        barra_lateral.addWidget(etiqueta_barra)

        for presentacion_id in self.presentaciones:
            boton = QW.QPushButton(presentacion_id[1])
            boton.setStyleSheet(estilo_boton)
            boton.setMaximumHeight(40)
            boton.setMinimumHeight(30)
            boton.clicked.connect(lambda checked, pid=presentacion_id[0]: self.abrirPresentacion(pid))
            barra_lateral.addWidget(boton)
            barra_lateral.setAlignment(Qt.AlignTop)

        if self.miembro:
            boton_nueva = QW.QPushButton("Nueva presentación")
            boton_nueva.setStyleSheet(estilo_boton)
            boton_nueva.clicked.connect(self.abrirFormularioNuevaPresentacion)
            barra_lateral.addWidget(boton_nueva)

        contenedor_general.addLayout(barra_lateral, 2)

        contenedor_contenido = QW.QVBoxLayout()
        etiqueta_titulo = QW.QLabel(datos[1])
        etiqueta_titulo.setStyleSheet("color: #dfecff; font-size: 50px;")
        etiqueta_titulo.setAlignment(Qt.AlignCenter)
        contenedor_contenido.addWidget(etiqueta_titulo)

        if self.miembro:
            boton_nuevo_contenido = QW.QPushButton("Nuevo contenido")
            boton_nuevo_contenido.setStyleSheet(estilo_boton)
            boton_nuevo_contenido.clicked.connect(self.abrirFormularioNuevoContenido)
            contenedor_contenido.addWidget(boton_nuevo_contenido)

        area_scroll = QW.QScrollArea()
        area_scroll.setWidgetResizable(True)
        widget_scroll = QW.QWidget()
        layout_scroll = QW.QVBoxLayout(widget_scroll)
        area_scroll.setWidget(widget_scroll)

        for i in datos_contenido:
            contenido = ContenidoPresentacion(i[0], i[1], i[2], i[3])
            layout_scroll.addLayout(contenido)

        contenedor_contenido.addWidget(area_scroll)
        contenedor_general.addLayout(contenedor_contenido, 8)

        layout_principal.addLayout(contenedor_general)

        self.show()

    def abrirBuscador(self):
        self.close()
        self.buscador = BuscadorProyectos(self.sesion)

    def abrirPrincipal(self):
        self.close()
        self.principal = VentanaPrincipal(self.sesion)

    def abrirPresentacion(self, id):
        self.close()
        self.nueva_presentacion = Presentacion(self.sesion, id, self.miembro)

    def abrirFormularioNuevaPresentacion(self):
        self.close()
        self.nuevo_form = FormularioNuevaPresentacion(self.sesion, self.id_grupo, self.id)

    def abrirFormularioNuevoContenido(self):
        self.close()
        self.form_contenido = FormularioNuevoContenido(self.sesion, self.id)


class ContenidoPresentacion(QW.QHBoxLayout):
    def __init__(self, id, encabezado, desc, imagen):
        super().__init__()

        self.contenedor_contenido = QW.QVBoxLayout()
        contenedor_imagen = QW.QVBoxLayout()

        contenedor_estilos_contenido = QW.QFrame()
        contenedor_estilos_imagen = QW.QFrame()

        contenedor_estilos_contenido.setStyleSheet(
            "background-color: #001a40; border-radius: 10px;"
        )
        contenedor_estilos_imagen.setStyleSheet(
            "background-color: #001a40; border-radius: 10px;"
        )

        self.etiqueta_encabezado = QW.QLabel(encabezado)
        self.etiqueta_encabezado.setStyleSheet("color: #dfecff; font-size: 20px;")
        self.etiqueta_encabezado.setAlignment(Qt.AlignCenter)

        self.etiqueta_descripcion = QW.QLabel(desc)
        self.etiqueta_descripcion.setStyleSheet("color: #dfecff;")
        self.etiqueta_descripcion.setAlignment(Qt.AlignCenter)

        self.contenedor_contenido.addWidget(self.etiqueta_encabezado)
        self.contenedor_contenido.addWidget(self.etiqueta_descripcion)
        contenedor_estilos_contenido.setLayout(self.contenedor_contenido)
        self.addWidget(contenedor_estilos_contenido)

        if imagen != "1":
            imagen_complementaria = QW.QLabel()
            imagen_complementaria.resize(50, 50)
            imagen_complementaria.setScaledContents(True)
            pixmap = QG.QPixmap("./img/" + imagen)
            pixmap_escalado = pixmap.scaled(imagen_complementaria.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
            imagen_complementaria.setPixmap(pixmap_escalado)
            contenedor_imagen.addWidget(imagen_complementaria)
            contenedor_estilos_imagen.setLayout(contenedor_imagen)
            self.addWidget(contenedor_estilos_imagen)


class AdministradorProyecto(QW.QWidget):
    def __init__(self, sesion, id_grupo):
        super().__init__()
        self.setStyleSheet("background-color: #001a40;")
        self.setWindowTitle("Administrador de Proyecto")
        self.resize(700, 600)

        self.sesion = sesion
        self.conexion = ConexionBaseDeDatos()

        # Datos simulados de miembros y usuarios disponibles
        self.datos_miembros = self.conexion.obtener_miembros_grupo(id_grupo)
        
        self.id_grupo = id_grupo

        self.datos_usuarios = self.conexion.obtener_miembros_agregables(id_grupo)

        # Layout principal
        layout_principal = QW.QVBoxLayout(self)

        # Header
        header = QW.QHBoxLayout()
        boton_volver = QW.QPushButton("Volver")
        boton_volver.clicked.connect(self.volver)
        boton_volver.setStyleSheet(self.estilo_boton())
        header.addWidget(boton_volver)
        header.addStretch()
        layout_principal.addLayout(header)

        # Etiqueta miembros
        etiqueta_miembros = QW.QLabel("Miembros del proyecto")
        etiqueta_miembros.setStyleSheet("color: #dfecff; font-size: 18px;")
        layout_principal.addWidget(etiqueta_miembros)

        # Tabla de miembros
        self.tabla_miembros = QW.QTableWidget(0, 3)
        self.tabla_miembros.setHorizontalHeaderLabels(["Nombre", "Rol", "Estado"])
        self.tabla_miembros.setSelectionBehavior(QW.QTableWidget.SelectRows)
        self.tabla_miembros.setSelectionMode(QW.QTableWidget.SingleSelection)
        self.tabla_miembros.itemChanged.connect(self.valor_modificado)
        layout_principal.addWidget(self.tabla_miembros)

        self.boton_estado = QW.QPushButton()
        self.boton_estado.hide()
        layout_principal.addWidget(self.boton_estado)

        self.tabla_miembros.itemSelectionChanged.connect(self.actualizar_boton_estado)

        # Cargar datos miembros
        self.cargar_miembros()

        # Etiqueta para agregar miembros
        etiqueta_usuarios = QW.QLabel("Agregar nuevos miembros")
        etiqueta_usuarios.setStyleSheet("color: #dfecff; font-size: 18px;")
        layout_principal.addWidget(etiqueta_usuarios)

        # Tabla usuarios disponibles
        self.tabla_usuarios = QW.QTableWidget(0, 1)
        self.tabla_usuarios.setHorizontalHeaderLabels(["Nombre"])
        self.tabla_usuarios.setSelectionBehavior(QW.QTableWidget.SelectRows)
        self.tabla_usuarios.setSelectionMode(QW.QTableWidget.MultiSelection)
        layout_principal.addWidget(self.tabla_usuarios)
        self.cargar_usuarios()

        # Botón agregar a miembros
        boton_agregar = QW.QPushButton("Agregar a miembros")
        boton_agregar.setStyleSheet(self.estilo_boton(expandir=True))
        boton_agregar.clicked.connect(self.agregar_miembros)
        layout_principal.addWidget(boton_agregar)
        self.show()

    def estilo_boton(self, expandir=False):
        style = """QPushButton {
            background-color: #004dbf;
            color: #dfecff;
            border-radius: 3px;
            padding: 10px;
        }
        QPushButton:hover {
            background-color: #00409f;
        }
        """
        if expandir:
            style += "QPushButton { width: 100%; }"
        return style

    def cargar_miembros(self):
        self.tabla_miembros.blockSignals(True)
        self.tabla_miembros.setRowCount(0)
        for id_u, nombre, rol, estado in self.datos_miembros:
            row = self.tabla_miembros.rowCount()
            self.tabla_miembros.insertRow(row)
            self.tabla_miembros.setItem(row, 0, QW.QTableWidgetItem(nombre))
            rol_item = QW.QTableWidgetItem(rol)
            rol_item.setFlags(rol_item.flags() | Qt.ItemIsEditable)
            self.tabla_miembros.setItem(row, 1, rol_item)
            self.tabla_miembros.setItem(row, 2, QW.QTableWidgetItem(estado))
        self.tabla_miembros.blockSignals(False)
        self.tabla_miembros.resizeColumnsToContents()
        self.tabla_miembros.setColumnWidth(0, self.width() * 0.6)

    def cargar_usuarios(self):
        self.tabla_usuarios.setRowCount(0)
        for _, nombre in self.datos_usuarios:
            row = self.tabla_usuarios.rowCount()
            self.tabla_usuarios.insertRow(row)
            self.tabla_usuarios.setItem(row, 0, QW.QTableWidgetItem(nombre))

    def actualizar_boton_estado(self):
        fila = self.tabla_miembros.currentRow()
        print(fila)
        if fila == -1:
            self.boton_estado.hide()

        estado = self.tabla_miembros.item(fila, 2).text()
        id_usuario = self.datos_miembros[fila][0]
        if estado == "activo":
            self.configurar_boton_estado("Expulsar", "#df1300", "#a00000", lambda: self.cambiar_estado(fila, "expulsado", id_usuario))
        elif estado == "expulsado":
            self.configurar_boton_estado("Reincorporar", "#ffff00", "#cccc00", lambda: self.cambiar_estado(fila, "activo", id_usuario))
        elif estado == "pendiente":
            self.configurar_boton_estado("Cancelar", "#004dbf", "#00409f", lambda: self.cambiar_estado(fila, "rechazado", id_usuario))
        elif estado == "rechazado":
            self.configurar_boton_estado("Reinvitar", "#00ff1d", "#00bf16", lambda: self.cambiar_estado(fila, "pendiente", id_usuario))

    def configurar_boton_estado(self, texto, color, hover, accion):
        self.boton_estado.setText(texto)
        self.boton_estado.setStyleSheet(f"""
            QPushButton {{
                background-color: {color};
                color: black;
                border-radius: 3px;
                padding: 10px;
            }}
            QPushButton:hover {{
                background-color: {hover};
            }}
        """)
        self.boton_estado.clicked.disconnect()
        self.boton_estado.clicked.connect(accion)
        self.boton_estado.show()

    def cambiar_estado(self, fila, nuevo_estado, id_usuario):
        self.datos_miembros[fila] = (*self.datos_miembros[fila][:3], nuevo_estado)
        self.cargar_miembros()
        self.conexion.cambiar_estado_miembro(id_usuario, self.id_grupo, nuevo_estado)
        print(f"Acción sobre usuario {id_usuario}, nuevo estado: {nuevo_estado}")

    def valor_modificado(self, item):
        if item.column() == 1:
            fila = item.row()
            self.conexion.cambiar_rol_miembro(self.datos_miembros[fila][0], self.id_grupo, item.text())
            print(f"Nuevo rol para usuario {self.datos_miembros[fila][0]}: {item.text()}")

    def agregar_miembros(self):
        filas_seleccionadas = self.tabla_usuarios.selectionModel().selectedRows()
        for index in sorted(filas_seleccionadas, reverse=True):
            fila = index.row()
            id_usuario = self.datos_usuarios[fila][0]
            nombre = self.datos_usuarios[fila][1]
            self.datos_miembros.append((id_usuario, nombre, "Ninguno", "pendiente"))
            self.conexion.invitar_usuario_grupo(id_usuario, self.id_grupo)
            self.datos_miembros.append(tuple([id_usuario, nombre, "Ninguno", "pendiente"]))
            print(f"Usuario {id_usuario} agregado como pendiente")
            self.tabla_usuarios.removeRow(fila)
        self.cargar_miembros()

    def volver(self):
        VentanaPrincipal(self.sesion)
        self.close()

class FormularioNuevoProyecto(QW.QWidget):
    def __init__(self, sesion: dict):
        super().__init__()
        self.sesion = sesion
        self.conexion = ConexionBaseDeDatos()
        self.setWindowTitle("Nuevo Proyecto")

        layout = QW.QVBoxLayout()

        titulo = QW.QLabel("Formulario Nuevo Proyecto")
        titulo.setAlignment(Qt.AlignCenter)
        layout.addWidget(titulo)

        self.entrada_nombre_proyecto = QW.QLineEdit()
        self.entrada_nombre_proyecto.setPlaceholderText("Nombre del proyecto")
        layout.addWidget(self.entrada_nombre_proyecto)

        self.entrada_tema_proyecto = QW.QLineEdit()
        self.entrada_tema_proyecto.setPlaceholderText("Tema del proyecto")
        layout.addWidget(self.entrada_tema_proyecto)

        boton_crear = QW.QPushButton("Crear Proyecto")
        boton_crear.clicked.connect(self.enviarFormulario)
        layout.addWidget(boton_crear)

        self.setLayout(layout)

        self.show()

    def enviarFormulario(self):
        nombre = self.entrada_nombre_proyecto.text()
        tema = self.entrada_tema_proyecto.text()

        print("Nombre del proyecto:", nombre)
        print("Tema del proyecto:", tema)
        print("ID Usuario:", self.sesion.get("id"))
        self.conexion.crear_proyecto(self.sesion["id"], nombre, tema)

        self.close()
        self.ventana = BuscadorProyectos(self.sesion)
        self.ventana.show()

class FormularioNuevoGrupo(QW.QWidget):
    def __init__(self, sesion: dict, id_proyecto):
        super().__init__()
        self.sesion = sesion
        self.conexion = ConexionBaseDeDatos()
        self.setWindowTitle("Nuevo grupo")

        self.id_proyecto = id_proyecto

        layout = QW.QVBoxLayout(self)

        self.titulo = QW.QLabel("Crear un Nuevo Grupo")
        self.titulo.setAlignment(Qt.AlignCenter)
        self.titulo.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(self.titulo)

        self.entrada_nombre_grupo = QW.QLineEdit()
        self.entrada_nombre_grupo.setPlaceholderText("Nombre grupo")
        layout.addWidget(self.entrada_nombre_grupo)

        self.boton_crear = QW.QPushButton("Crear grupo")
        self.boton_crear.clicked.connect(self.enviarFormulario)
        layout.addWidget(self.boton_crear)

        self.show()

    def enviarFormulario(self):
        nombre_grupo = self.entrada_nombre_grupo.text()
        print(f"Datos ingresados: {nombre_grupo}")
        self.conexion.crear_grupo(nombre_grupo)
        self.conexion.ingresar_lider_grupo(self.sesion["id"])
        self.conexion.enviar_solicitud(self.id_proyecto)
        self.conexion.crear_presentacion_principal(nombre_grupo)
        self.close()
        self.ventana = BuscadorProyectos(self.sesion)

class FormularioNuevaPresentacion(QW.QWidget):
    def __init__(self, sesion: dict, id_grupo: int, id_presentacion):
        super().__init__()
        self.sesion = sesion
        self.id_grupo = id_grupo
        self.id_presentacion = id_presentacion
        self.conexion = ConexionBaseDeDatos()
        self.setWindowTitle("Nueva presentación")

        layout = QW.QVBoxLayout(self)

        self.titulo = QW.QLabel("Crear una Nueva Presentación")
        self.titulo.setAlignment(Qt.AlignCenter)
        self.titulo.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(self.titulo)

        self.entrada_nombre_presentacion = QW.QLineEdit()
        self.entrada_nombre_presentacion.setPlaceholderText("Nombre presentacion")
        layout.addWidget(self.entrada_nombre_presentacion)

        self.boton_crear = QW.QPushButton("Crear presentación")
        self.boton_crear.clicked.connect(self.enviarFormulario)
        layout.addWidget(self.boton_crear)

        self.show()

    def enviarFormulario(self):
        nombre_presentacion = self.entrada_nombre_presentacion.text()
        print(f"Datos ingresados: {nombre_presentacion}, ID grupo: {self.id_grupo}")
        self.conexion.crear_nueva_presentacion(nombre_presentacion, self.id_grupo)
        self.close()
        self.ventana = Presentacion(self.sesion, self.id_presentacion, True)

class FormularioNuevoContenido(QW.QWidget):
    def __init__(self, sesion: dict, id_presentacion: int):
        super().__init__()
        self.sesion = sesion
        self.id_presentacion = id_presentacion
        self.setWindowTitle("Nuevo contenido")

        self.conexion = ConexionBaseDeDatos()

        layout = QW.QVBoxLayout(self)

        self.titulo = QW.QLabel("Crear Nuevo Contenido")
        self.titulo.setAlignment(Qt.AlignCenter)
        self.titulo.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(self.titulo)

        self.entrada_encabezado = QW.QLineEdit()
        self.entrada_encabezado.setPlaceholderText("Encabezado")
        layout.addWidget(self.entrada_encabezado)

        self.entrada_descripcion = QW.QTextEdit()
        self.entrada_descripcion.setPlaceholderText("Descripción")
        layout.addWidget(self.entrada_descripcion)

        self.boton_crear = QW.QPushButton("Crear contenido")
        self.boton_crear.clicked.connect(self.enviarFormulario)
        layout.addWidget(self.boton_crear)

        self.show()

    def enviarFormulario(self):
        encabezado = self.entrada_encabezado.text()
        descripcion = self.entrada_descripcion.toPlainText()
        print(f"Datos ingresados: Encabezado: {encabezado}, Descripción: {descripcion}, ID presentación: {self.id_presentacion}")
        self.conexion.crear_nuevo_contenido(encabezado, descripcion, self.id_presentacion)
        self.close()
        self.ventana = Presentacion(self.sesion, self.id_presentacion, True)

class TablaUsuarios(QW.QWidget):
    def __init__(self, sesion: dict):
        super().__init__()
        self.sesion = sesion
        self.conexion = ConexionBaseDeDatos()
        self.setWindowTitle("Gestión de Usuarios")
        self.setStyleSheet("background-color: #000d20; color: #dfecff;")

        layout = QW.QVBoxLayout(self)

        titulo = QW.QLabel("Usuarios del sistema")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(titulo)

        # Tabla
        self.tabla = QW.QTableWidget()
        self.tabla.setColumnCount(4)
        self.tabla.setHorizontalHeaderLabels(["ID", "Nombre", "Email", "Permisos"])
        self.tabla.setStyleSheet("QHeaderView::section { background-color: #004dbf; color: white; }"
                                 "QTableWidget { background-color: #dfecff; color: black; }")

        # Datos de prueba
        self.datos_usuarios = self.conexion.obtener_usuarios_administrables()

        self.tabla.setRowCount(len(self.datos_usuarios))
        permisos_opciones = ["UE", "PR", "AD"]

        for fila, (id_u, nombre, email, permiso) in enumerate(self.datos_usuarios):
            self.tabla.setItem(fila, 0, QW.QTableWidgetItem(str(id_u)))
            self.tabla.setItem(fila, 1, QW.QTableWidgetItem(nombre))
            self.tabla.setItem(fila, 2, QW.QTableWidgetItem(email))

            combo = QW.QComboBox()
            combo.addItems(permisos_opciones)
            combo.setCurrentText(permiso)
            combo.currentIndexChanged.connect(lambda index, row=fila: self.imprimirFila(row))
            self.tabla.setCellWidget(fila, 3, combo)

        layout.addWidget(self.tabla)

        # Botón de volver
        boton_volver = QW.QPushButton("Volver al Inicio")
        boton_volver.setStyleSheet(
            "QPushButton { background-color: #004dbf; border-radius: 3px; color: #dfecff; padding: 10px; }"
            "QPushButton:hover { background-color: #00409f; }"
        )
        boton_volver.clicked.connect(self.volverInicio)
        layout.addWidget(boton_volver)

        self.show()

    def imprimirFila(self, fila):
        id_u = self.tabla.item(fila, 0).text()
        nombre = self.tabla.item(fila, 1).text()
        email = self.tabla.item(fila, 2).text()
        permisos = self.tabla.cellWidget(fila, 3).currentText()
        print(f"Fila actualizada: ID: {id_u}, Nombre: {nombre}, Email: {email}, Permisos: {permisos}")
        self.conexion.administrar_usuario(id_u, nombre, email, permisos, self.datos_usuarios[fila][0])

    def volverInicio(self):
        self.close()
        self.ventana = VentanaPrincipal(self.sesion)
        self.ventana.show()
