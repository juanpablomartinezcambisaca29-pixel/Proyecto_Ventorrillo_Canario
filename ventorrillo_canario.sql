/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19-11.8.6-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: Ventorrillo_Canario
-- ------------------------------------------------------
-- Server version	11.8.6-MariaDB-0+deb13u1 from Debian

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*M!100616 SET @OLD_NOTE_VERBOSITY=@@NOTE_VERBOSITY, NOTE_VERBOSITY=0 */;

--
-- Table structure for table `Categorías`
--

DROP TABLE IF EXISTS `Categorías`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Categorías` (
  `Id_categoría` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) NOT NULL,
  PRIMARY KEY (`Id_categoría`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Categorías`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Categorías` WRITE;
/*!40000 ALTER TABLE `Categorías` DISABLE KEYS */;
INSERT INTO `Categorías` VALUES
(1,'Entrantes'),
(2,'Platos Principales'),
(3,'Bebidas'),
(4,'Postres'),
(5,'Pescados'),
(6,'Vinos'),
(7,'Guarniciones');
/*!40000 ALTER TABLE `Categorías` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `Detalle_Pedidos`
--

DROP TABLE IF EXISTS `Detalle_Pedidos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Detalle_Pedidos` (
  `Id_detalle` int(11) NOT NULL AUTO_INCREMENT,
  `Id_pedido` int(11) DEFAULT NULL,
  `Id_plato` int(11) DEFAULT NULL,
  `Cantidad` int(11) NOT NULL,
  PRIMARY KEY (`Id_detalle`),
  KEY `Fk_pedido` (`Id_pedido`),
  KEY `Fk_plato` (`Id_plato`),
  CONSTRAINT `Fk_pedido` FOREIGN KEY (`Id_pedido`) REFERENCES `Pedidos` (`Id_pedido`) ON DELETE CASCADE,
  CONSTRAINT `Fk_plato` FOREIGN KEY (`Id_plato`) REFERENCES `Platos` (`Id_plato`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Detalle_Pedidos`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Detalle_Pedidos` WRITE;
/*!40000 ALTER TABLE `Detalle_Pedidos` DISABLE KEYS */;
INSERT INTO `Detalle_Pedidos` VALUES
(1,1,5,2),
(2,1,7,1),
(3,2,2,1),
(4,3,8,1),
(5,3,10,2);
/*!40000 ALTER TABLE `Detalle_Pedidos` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `Mesas`
--

DROP TABLE IF EXISTS `Mesas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Mesas` (
  `Id_mesa` int(11) NOT NULL AUTO_INCREMENT,
  `Número_mesa` int(11) NOT NULL,
  `Capacidad` int(11) NOT NULL,
  PRIMARY KEY (`Id_mesa`),
  UNIQUE KEY `Número_mesa` (`Número_mesa`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Mesas`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Mesas` WRITE;
/*!40000 ALTER TABLE `Mesas` DISABLE KEYS */;
INSERT INTO `Mesas` VALUES
(1,1,4),
(2,2,2),
(3,3,6),
(4,4,4),
(5,5,8),
(6,6,2);
/*!40000 ALTER TABLE `Mesas` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `Pedidos`
--

DROP TABLE IF EXISTS `Pedidos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Pedidos` (
  `Id_pedido` int(11) NOT NULL AUTO_INCREMENT,
  `Id_mesa` int(11) DEFAULT NULL,
  `Fecha_pedido` datetime DEFAULT current_timestamp(),
  `Estado` varchar(20) DEFAULT 'Pendiente',
  PRIMARY KEY (`Id_pedido`),
  KEY `Fk_mesa` (`Id_mesa`),
  CONSTRAINT `Fk_mesa` FOREIGN KEY (`Id_mesa`) REFERENCES `Mesas` (`Id_mesa`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Pedidos`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Pedidos` WRITE;
/*!40000 ALTER TABLE `Pedidos` DISABLE KEYS */;
INSERT INTO `Pedidos` VALUES
(1,1,'2026-04-28 19:34:40','En preparación'),
(2,3,'2026-04-28 19:34:40','Pendiente'),
(3,5,'2026-04-28 19:34:40','Completado');
/*!40000 ALTER TABLE `Pedidos` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `Platos`
--

DROP TABLE IF EXISTS `Platos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Platos` (
  `Id_plato` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(100) NOT NULL,
  `Precio` decimal(10,2) NOT NULL,
  `Id_categoría` int(11) DEFAULT NULL,
  PRIMARY KEY (`Id_plato`),
  KEY `Fk_categoría` (`Id_categoría`),
  CONSTRAINT `Fk_categoría` FOREIGN KEY (`Id_categoría`) REFERENCES `Categorías` (`Id_categoría`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Platos`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Platos` WRITE;
/*!40000 ALTER TABLE `Platos` DISABLE KEYS */;
INSERT INTO `Platos` VALUES
(1,'Jamón Ibérico',14.50,1),
(2,'Solomillo al Whisky',18.00,2),
(3,'Coca Cola',2.50,4),
(4,'Tarta de Queso',5.00,2),
(5,'Papas con Mojo',5.50,1),
(6,'Queso Asado con Miel',7.00,1),
(7,'Gofio Escaldao',6.00,1),
(8,'Cherne a la Plancha',14.00,5),
(9,'Copa de Vino Tinto',3.00,6),
(10,'Mousse de Gofio',4.50,4);
/*!40000 ALTER TABLE `Platos` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*M!100616 SET NOTE_VERBOSITY=@OLD_NOTE_VERBOSITY */;

-- Dump completed on 2026-04-29 18:54:51
