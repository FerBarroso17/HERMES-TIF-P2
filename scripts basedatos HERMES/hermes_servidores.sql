-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: hermes
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `servidores`
--

DROP TABLE IF EXISTS `servidores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `servidores` (
  `servidor_id` int NOT NULL AUTO_INCREMENT,
  `nombre_servidor` varchar(50) NOT NULL,
  `descripcion` text,
  `fecha_creacion` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `propietario_id` int NOT NULL,
  `foto_servidor` blob,
  PRIMARY KEY (`servidor_id`),
  KEY `propietario_id` (`propietario_id`),
  CONSTRAINT `servidores_ibfk_1` FOREIGN KEY (`propietario_id`) REFERENCES `usuarios` (`usuario_id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servidores`
--

LOCK TABLES `servidores` WRITE;
/*!40000 ALTER TABLE `servidores` DISABLE KEYS */;
INSERT INTO `servidores` VALUES (1,'servidor 19hs','prueba','2023-09-26 22:20:23',11,NULL),(2,'servidor 19:23 hs','prueba','2023-09-26 22:23:52',11,NULL),(3,'Mi servidor','Este es mi servidor','2023-09-27 20:28:50',12,NULL),(4,'Mi servidor 2','servidor 2','2023-09-27 20:46:05',12,NULL),(5,'Mi servidor 3','servidor 3','2023-09-27 20:48:30',12,NULL),(6,'Mi servidor 4','servidor 4','2023-09-27 20:50:37',12,NULL),(7,'Mi servidor 5','servidor 5','2023-09-27 20:59:14',12,NULL),(8,'Mi servidor 5','servidor 5','2023-09-27 21:02:43',12,NULL),(9,'Mi servidor 5','servidor 5','2023-09-27 21:04:13',12,NULL),(10,'Mi servidor 5','servidor 5','2023-09-27 21:12:02',12,NULL),(11,'Mi servidor 5','servidor 5','2023-09-27 21:14:49',12,NULL),(12,'Mi servidor 5','servidor 5','2023-09-27 21:15:42',12,NULL),(13,'Mi servidor 5','servidor 5','2023-09-27 21:19:23',12,NULL),(14,'Mi servidor 5','servidor 5','2023-09-27 21:21:06',12,NULL),(15,'servidor prueba 8','servidor prueba 8','2023-09-27 23:31:55',11,NULL),(16,'servidor matias','fasdfasdf','2023-09-28 01:48:29',12,NULL),(17,'servidor noche 3am','prueba de zombie','2023-09-28 06:03:53',11,NULL),(18,'servidor 17:17','prueba usuario CLau','2023-09-28 20:17:25',19,NULL);
/*!40000 ALTER TABLE `servidores` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-28 17:54:21
