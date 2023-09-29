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
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `usuario_id` int NOT NULL AUTO_INCREMENT,
  `nombre_usuario` varchar(16) NOT NULL,
  `correo_electronico` varchar(50) NOT NULL,
  `contrasena` varchar(50) NOT NULL,
  `fecha_nacimiento` varchar(50) NOT NULL,
  `nombre` varchar(50) DEFAULT NULL,
  `apellido` varchar(50) DEFAULT NULL,
  `foto_perfil` blob,
  PRIMARY KEY (`usuario_id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'Maurez7','gomezmauroleonel3@gmail.com','Masterking7+','2001-09-14','Mauro','Gomez',NULL),(2,'Franchesco','dadsadad@gmail.com','123456','2001-09-14','Francisco','Liendro',NULL),(3,'Raul777','raulrios9877@gmail.com','raul789001','1982-06-10','Raul','Alfonsin',NULL),(4,'Jeipe22','jeipe990we@gmail.com','juanpaa22+','2003-02-07','Juan','Echeverria',NULL),(10,'Rios777','fafafaf23232@gmail.com','pato123','2023-09-13','Raul','Rios',NULL),(11,'FBarroso','ferda@gmail.com','Fer17','1988-01-17','Fernando ','Barroso',NULL),(12,'daniel2130','daniel@cualquiera.com','dani731','2023-09-26','Daniel','jjjj',NULL),(13,'daniel2130','daniel@cualquiera.com','dani731','2023-09-26','Daniel','jjjj',NULL),(14,'daniel2130','daniel@cualquiera.com','dani731','2023-09-26','Daniel','jjjj',NULL),(15,'daniel2130','daniel@cualquiera.com','dani731','2023-09-26','Daniel','jjjj',NULL),(16,'daniel2130','daniel@cualquiera.com','dani731','2023-09-26','Daniel','jjjj',NULL),(17,'daniel2130','daniel@cualquiera.com','dani731','2023-09-26','Daniel','jjjj',NULL),(18,'daniel2130','daniel@cualquiera.com','dani731','2023-09-26','Daniel','jjjj',NULL),(19,'CLau','clau@gmail.com','CLau765','2023-09-12','CLau','chavarria',NULL);
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-28 17:54:22
