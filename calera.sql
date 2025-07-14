-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 14-07-2025 a las 19:26:49
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `calera`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `contenido`
--

CREATE TABLE `contenido` (
  `id` int(11) NOT NULL,
  `subtitulo` varchar(255) DEFAULT NULL,
  `contenido` text DEFAULT NULL,
  `img` text DEFAULT '1',
  `decoracion` text DEFAULT NULL,
  `id_presentacion` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `contenido`
--

INSERT INTO `contenido` (`id`, `subtitulo`, `contenido`, `img`, `decoracion`, `id_presentacion`) VALUES
(6, 'HOLA', 'TEXTO DE PRUEBA PaARA COMPROBAR QUE FUNCIONA DE MANERA CORRECTA EL CREADOR DE CONTENIDO', 'Sparkle 213--.jpg', NULL, 1),
(7, 'HOLA2', 'Texto de prueba de bvuelta para ver sui funciona', '1', NULL, 1),
(8, 'SONUS', 'SONUS es un sonometro', '1', NULL, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estilo`
--

CREATE TABLE `estilo` (
  `id` int(11) NOT NULL,
  `tipografia` text NOT NULL DEFAULT 'sans-serif',
  `color_encabezado` text NOT NULL DEFAULT '#000000',
  `color_contenido` text NOT NULL DEFAULT '#000000',
  `color_bloque` text NOT NULL DEFAULT '#ffffff',
  `bordes_bloque` text NOT NULL DEFAULT 'none',
  `bordes_letra` text NOT NULL DEFAULT 'none',
  `color_bordes_bloque` text NOT NULL DEFAULT '#000000',
  `color_bordes_letra` text NOT NULL DEFAULT '#000000',
  `id_contenido` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `estilo`
--

INSERT INTO `estilo` (`id`, `tipografia`, `color_encabezado`, `color_contenido`, `color_bloque`, `bordes_bloque`, `bordes_letra`, `color_bordes_bloque`, `color_bordes_letra`, `id_contenido`) VALUES
(2, 'serif', '#7d4040', '#ffb3b3', '#c58181', 'dashed', 'none', '#7a1f1f', '#000000', 6),
(3, 'sans-serif', '#702929', '#000000', '#ffffff', 'none', 'none', '#000000', '#000000', 7);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `grupos`
--

CREATE TABLE `grupos` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `escudo` text NOT NULL DEFAULT 'escudo.png'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `grupos`
--

INSERT INTO `grupos` (`id`, `nombre`, `escudo`) VALUES
(8, 'Los tontos enmascarados', 'escudo.png'),
(10, 'Robotin', 'escudo.png'),
(11, 'Robotin', 'escudo.png');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `presentaciones`
--

CREATE TABLE `presentaciones` (
  `id` int(11) NOT NULL,
  `encabezado` varchar(100) DEFAULT NULL,
  `fecha_comienzo` varchar(255) DEFAULT NULL,
  `fecha_finalizacion` varchar(255) DEFAULT NULL,
  `definicion` text DEFAULT NULL,
  `proposito` text DEFAULT NULL,
  `id_grupo` int(11) NOT NULL,
  `imagen_portada` text NOT NULL DEFAULT 'proyecto_por_defecto.jpg',
  `tipo` varchar(100) NOT NULL DEFAULT 'etapa',
  `color_titulo` varchar(30) NOT NULL DEFAULT '#000000',
  `color_fondo` varchar(30) NOT NULL DEFAULT '#ffffff',
  `color_borde` varchar(30) NOT NULL DEFAULT '#000000',
  `grosor_borde` varchar(30) NOT NULL DEFAULT '1.1rem',
  `tipo_borde` varchar(30) NOT NULL DEFAULT 'solid',
  `tipografia` varchar(100) NOT NULL DEFAULT 'sans-serif'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `presentaciones`
--

INSERT INTO `presentaciones` (`id`, `encabezado`, `fecha_comienzo`, `fecha_finalizacion`, `definicion`, `proposito`, `id_grupo`, `imagen_portada`, `tipo`, `color_titulo`, `color_fondo`, `color_borde`, `grosor_borde`, `tipo_borde`, `tipografia`) VALUES
(1, 'Los tontos enmascarados', NULL, NULL, NULL, NULL, 8, 'Sparkle 210.jpg', 'principal', '#390f0f', '#ffb3b3', '#f86868', '0.7rem', 'dotted', 'serif'),
(2, 'SONUS', NULL, NULL, NULL, NULL, 11, 'proyecto_por_defecto.jpg', 'principal', '#000000', '#ffffff', '#000000', '1.1rem', 'solid', 'sans-serif');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proyectos`
--

CREATE TABLE `proyectos` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `descripcion` text DEFAULT NULL,
  `tema` varchar(255) DEFAULT 'general',
  `id_creador` int(11) NOT NULL,
  `imagen` text NOT NULL DEFAULT 'proyecto_por_defecto.jpg'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `proyectos`
--

INSERT INTO `proyectos` (`id`, `nombre`, `descripcion`, `tema`, `id_creador`, `imagen`) VALUES
(3, 'Robots SUMO', 'Pelea épica entre robots destinados a empujarse los unos a los otros para quedarse con el trono.', 'robotica', 6, 'proyecto_por_defecto.jpg'),
(4, 'SONUS', NULL, 'Electronica', 6, 'proyecto_por_defecto.jpg');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `solicitudes`
--

CREATE TABLE `solicitudes` (
  `id` int(11) NOT NULL,
  `encabezado` varchar(100) DEFAULT NULL,
  `contenido` text DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `hora` time DEFAULT NULL,
  `estado` varchar(100) DEFAULT 'pendiente',
  `id_grupo` int(11) DEFAULT NULL,
  `id_proyecto` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `solicitudes`
--

INSERT INTO `solicitudes` (`id`, `encabezado`, `contenido`, `fecha`, `hora`, `estado`, `id_grupo`, `id_proyecto`) VALUES
(2, NULL, NULL, NULL, NULL, 'aceptado', 8, 3),
(3, NULL, NULL, NULL, NULL, 'aceptado', 11, 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `contra` varchar(100) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `permisos` text DEFAULT 'UE'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombre`, `contra`, `email`, `permisos`) VALUES
(2, 'Pepe', '123', 'pepe@gmail.com', 'UE'),
(3, 'Jorgito', '123', 'jorgito@gmail.com', 'UE'),
(4, 'Estaban', '123', 'esteban@gmail.com', 'UE'),
(6, 'Bruno', '123', 'bruno@gmail.com', 'AD'),
(7, 'Juancito', '123', 'juancito@gmail.com', 'UE'),
(8, 'Kakaroto', '1', 'kara@gmail.com', 'PR');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios_grupos`
--

CREATE TABLE `usuarios_grupos` (
  `id` int(11) NOT NULL,
  `id_grupo` int(11) DEFAULT NULL,
  `id_usuario` int(11) DEFAULT NULL,
  `rol` varchar(255) DEFAULT 'ninguno',
  `estado` varchar(30) NOT NULL DEFAULT 'pendiente'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios_grupos`
--

INSERT INTO `usuarios_grupos` (`id`, `id_grupo`, `id_usuario`, `rol`, `estado`) VALUES
(7, 8, 2, 'lider', 'activo'),
(10, 8, 4, 'aaaa', 'expulsado'),
(16, 8, 7, 'ninguno', 'rechazado'),
(17, 8, 3, 'ninguno', 'activo'),
(18, 8, 8, 'Goku', 'pendiente'),
(19, 11, 3, 'lider', 'activo');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `contenido`
--
ALTER TABLE `contenido`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_presentacion` (`id_presentacion`);

--
-- Indices de la tabla `estilo`
--
ALTER TABLE `estilo`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_contenido` (`id_contenido`);

--
-- Indices de la tabla `grupos`
--
ALTER TABLE `grupos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `presentaciones`
--
ALTER TABLE `presentaciones`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_grupo` (`id_grupo`);

--
-- Indices de la tabla `proyectos`
--
ALTER TABLE `proyectos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_creador` (`id_creador`);

--
-- Indices de la tabla `solicitudes`
--
ALTER TABLE `solicitudes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_grupo` (`id_grupo`),
  ADD KEY `id_proyecto` (`id_proyecto`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indices de la tabla `usuarios_grupos`
--
ALTER TABLE `usuarios_grupos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_grupo` (`id_grupo`,`id_usuario`),
  ADD KEY `id_usuario` (`id_usuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `contenido`
--
ALTER TABLE `contenido`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `estilo`
--
ALTER TABLE `estilo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `grupos`
--
ALTER TABLE `grupos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `presentaciones`
--
ALTER TABLE `presentaciones`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `proyectos`
--
ALTER TABLE `proyectos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `solicitudes`
--
ALTER TABLE `solicitudes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `usuarios_grupos`
--
ALTER TABLE `usuarios_grupos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `contenido`
--
ALTER TABLE `contenido`
  ADD CONSTRAINT `contenido_ibfk_1` FOREIGN KEY (`id_presentacion`) REFERENCES `presentaciones` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `estilo`
--
ALTER TABLE `estilo`
  ADD CONSTRAINT `estilo_ibfk_1` FOREIGN KEY (`id_contenido`) REFERENCES `contenido` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `presentaciones`
--
ALTER TABLE `presentaciones`
  ADD CONSTRAINT `presentaciones_ibfk_1` FOREIGN KEY (`id_grupo`) REFERENCES `grupos` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `proyectos`
--
ALTER TABLE `proyectos`
  ADD CONSTRAINT `proyectos_ibfk_1` FOREIGN KEY (`id_creador`) REFERENCES `usuarios` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `solicitudes`
--
ALTER TABLE `solicitudes`
  ADD CONSTRAINT `solicitudes_ibfk_1` FOREIGN KEY (`id_grupo`) REFERENCES `grupos` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `solicitudes_ibfk_2` FOREIGN KEY (`id_proyecto`) REFERENCES `proyectos` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `usuarios_grupos`
--
ALTER TABLE `usuarios_grupos`
  ADD CONSTRAINT `usuarios_grupos_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `usuarios_grupos_ibfk_2` FOREIGN KEY (`id_grupo`) REFERENCES `grupos` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
