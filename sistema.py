import mysql.connector

class ConexionBaseDeDatos:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="calera"
        )

    def obtener_usuario(self, email, contrasena):
        cursor = self.conexion.cursor()
        consulta = """
            SELECT id, contra, nombre, permisos
            FROM usuarios
            WHERE email = %s AND contra = %s
        """
        cursor.execute(consulta, (email, contrasena))
        resultado = cursor.fetchone()
        cursor.close()
        return resultado

    def registrar_usuario(self, nombre, email, contrasena):
        cursor = self.conexion.cursor()
        consulta = """
            INSERT INTO usuarios (nombre, email, contra)
            VALUES (%s, %s, %s)
        """
        cursor.execute(consulta, (nombre, email, contrasena))
        self.conexion.commit()
        cursor.close()

    def obtener_invitaciones(self, id_usuario):
        cursor = self.conexion.cursor()
        cursor.execute('''
            SELECT usuarios_grupos.id, proyectos.nombre
            FROM usuarios_grupos
            JOIN grupos ON usuarios_grupos.id_grupo = grupos.id JOIN solicitudes ON solicitudes.id_grupo = grupos.id JOIN proyectos ON proyectos.id = solicitudes.id_proyecto
            WHERE usuarios_grupos.id_usuario = %s AND usuarios_grupos.estado = 'pendiente'
        ''', tuple([id_usuario]))
        return cursor.fetchall()

    # Aceptar invitación
    def aceptar_invitacion(self, id_invitacion):
        cursor = self.conexion.cursor()
        cursor.execute('''
            UPDATE usuarios_grupos
            SET estado = 'activo'
            WHERE id = %s
        ''', tuple([id_invitacion]))
        self.conexion.commit()

    # Rechazar invitación
    def rechazar_invitacion(self, id_invitacion):
        cursor = self.conexion.cursor()
        cursor.execute('''
            UPDATE usuarios_grupos
            SET estado = 'rechazado'
            WHERE id = %s
        ''', tuple([id_invitacion]))
        self.conexion.commit()

    def obtener_proyectos_para_buscador(self):
        cursor = self.conexion.cursor()
        cursor.execute('''
            SELECT nombre, tema, id
            FROM proyectos
        ''')
        return cursor.fetchall()
    
    def obtener_proyectos_usuario(self):
        cursor = self.conexion.cursor()
        consulta = """
            SELECT `id`, `nombre`, `imagen` FROM `proyectos` ORDER BY id DESC
        """
        cursor.execute(consulta)
        resultado = cursor.fetchone()
        cursor.close()
        return resultado
    
    def obtener_grupos_proyectos(self, id_proyecto):
        cursor = self.conexion.cursor()
        cursor.execute('''
            SELECT p.`id`, g.nombre, p.`imagen_portada`, g.id FROM `presentaciones` p JOIN grupos g ON g.id = p.id_grupo JOIN solicitudes s ON s.id_grupo = g.id WHERE s.id_proyecto = %s;
        ''', (id_proyecto,))
        return cursor.fetchall()
    
    def obtener_datos_presentacion(self, id_presentacion):
        cursor = self.conexion.cursor()
        consulta = """
            SELECT `id`, `encabezado`, `imagen_portada`, `tipo` FROM `presentaciones` WHERE id = %s
        """
        cursor.execute(consulta, (id_presentacion,))
        resultado = cursor.fetchone()
        cursor.close()
        return resultado
    
    def obtener_presentaciones_hermanas(self, id_presentacion):
        cursor = self.conexion.cursor()
        cursor.execute('''
            SELECT `id`, `encabezado` FROM `presentaciones` WHERE id_grupo = (SELECT id_grupo FROM presentaciones WHERE id = %s)
        ''', (id_presentacion,))
        return cursor.fetchall()
    
    def obtener_contenido_presentacion(self, id_presentacion):
        cursor = self.conexion.cursor()
        cursor.execute('''
            SELECT `id`, `subtitulo`, `contenido`, `img` FROM `contenido` WHERE id_presentacion = %s
        ''', (id_presentacion,))
        return cursor.fetchall()
    
    def es_administrador(self, id_grupo, id_usuario):
        cursor = self.conexion.cursor()
        consulta = """
            SELECT 1 FROM `usuarios_grupos` WHERE id_usuario = %s AND id_grupo = %s
        """
        cursor.execute(consulta, (id_usuario, id_grupo))
        resultado = cursor.fetchone()
        cursor.close()
        return resultado
    
    def obtener_miembros_grupo(self, id_grupo):
        cursor = self.conexion.cursor()
        cursor.execute('''
            SELECT ug.`id_usuario`, u.nombre, ug.`rol`, ug.`estado` FROM `usuarios_grupos` ug JOIN usuarios u ON u.id = ug.id_usuario WHERE id_grupo = %s
        ''', (id_grupo,))
        return cursor.fetchall()
    
    def obtener_miembros_agregables(self, id_grupo):
        cursor = self.conexion.cursor()
        cursor.execute('''
            SELECT `id`, `nombre` FROM `usuarios` u WHERE EXISTS(SELECT 1 FROM usuarios_grupos ug WHERE ug.id_grupo = %s AND ug.id_usuario = u.id) != 1
        ''', (id_grupo,))
        return cursor.fetchall()
    
    def cambiar_estado_miembro(self, id_usuario, id_grupo, estado):
        cursor = self.conexion.cursor()
        cursor.execute('''
            UPDATE `usuarios_grupos` SET `estado`=%s WHERE  id_usuario = %s AND id_grupo = %s
        ''', (estado, id_usuario, id_grupo))
        self.conexion.commit()

    def cambiar_rol_miembro(self, id_usuario, id_grupo, rol):
        cursor = self.conexion.cursor()
        cursor.execute('''
            UPDATE `usuarios_grupos` SET `rol`=%s WHERE id_usuario = %s AND id_grupo = %s
        ''', (rol, id_usuario, id_grupo))
        self.conexion.commit()

    def invitar_usuario_grupo(self, id_usuario, id_grupo):
        cursor = self.conexion.cursor()
        cursor.execute('''
            INSERT INTO `usuarios_grupos`(`id_grupo`, `id_usuario`) VALUES (%s,%s)
        ''', (id_grupo, id_usuario))
        self.conexion.commit()

    def crear_proyecto(self, id_usuario, nombre, tema):
        cursor = self.conexion.cursor()
        cursor.execute('''
            INSERT INTO `proyectos`(`nombre`, `tema`, `id_creador`) VALUES (%s, %s, %s)
        ''', (nombre, tema, id_usuario))
        self.conexion.commit()

    def ingresar_lider_grupo(self, id_usuario):
        cursor = self.conexion.cursor()
        cursor.execute('''
            INSERT INTO `usuarios_grupos`(`id_grupo`, `id_usuario`, rol, estado) VALUES ((SELECT MAX(`id`) FROM `grupos`),%s, 'lider', 'activo')
        ''', (id_usuario))
        self.conexion.commit()

    def crear_grupo(self, id_usuario, nombre, tema):
        cursor = self.conexion.cursor()
        cursor.execute('''
            INSERT INTO `proyectos`(`nombre`, `tema`, `id_creador`) VALUES (%s, %s, %s)
        ''', (nombre, tema, id_usuario))
        self.conexion.commit()

    def crear_nueva_presentacion(self, id_usuario, nombre, tema):
        cursor = self.conexion.cursor()
        cursor.execute('''
            INSERT INTO `proyectos`(`nombre`, `tema`, `id_creador`) VALUES (%s, %s, %s)
        ''', (nombre, tema, id_usuario))
        self.conexion.commit()

    def crear_nuevo_contenido(self, id_usuario, nombre, tema):
        cursor = self.conexion.cursor()
        cursor.execute('''
            INSERT INTO `proyectos`(`nombre`, `tema`, `id_creador`) VALUES (%s, %s, %s)
        ''', (nombre, tema, id_usuario))
        self.conexion.commit()