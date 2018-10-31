-- MySQL dump 10.13  Distrib 5.7.21, for Linux (x86_64)
--
-- Host: localhost    Database: Aluses
-- ------------------------------------------------------
-- Server version	5.7.21-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Flight`
--

DROP TABLE IF EXISTS `Flight`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Flight` (
  `idFlight` int(11) NOT NULL AUTO_INCREMENT,
  `departure` varchar(45) NOT NULL,
  `arrival` varchar(45) NOT NULL,
  `idPlane` int(11) NOT NULL,
  `flightDepartureDatetime` datetime NOT NULL,
  `flightArrivalDatetime` datetime NOT NULL,
  `percentDiscount` int(11) NOT NULL,
  PRIMARY KEY (`idFlight`),
  KEY `fk_Flight_Plane1_idx` (`idPlane`),
  CONSTRAINT `fk_Flight_Plane1` FOREIGN KEY (`idPlane`) REFERENCES `Plane` (`idPlane`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Flight`
--

LOCK TABLES `Flight` WRITE;
/*!40000 ALTER TABLE `Flight` DISABLE KEYS */;
INSERT INTO `Flight` VALUES (1,'Buenos Aires','Miami',1,'2018-10-11 07:00:00','2018-10-11 15:00:00',5),(2,'Buenos Aires','Tokio',2,'2018-10-26 13:00:00','2018-10-27 03:30:00',10),(3,'Buenos Aires','Londres',1,'2018-11-05 10:00:00','2018-11-15 17:00:00',20),(4,'Buenos Aires','Paris',2,'2018-10-25 16:00:00','2018-10-31 01:00:00',10),(5,'Buenos Aires','Rumania',1,'2018-10-18 02:30:00','2018-10-23 17:50:00',5),(6,'Buenos Aires ','Holanda',2,'2018-12-05 17:45:00','2018-12-25 15:35:00',15);
/*!40000 ALTER TABLE `Flight` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Flight_has_User`
--

DROP TABLE IF EXISTS `Flight_has_User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Flight_has_User` (
  `idFlight` int(11) NOT NULL,
  `idUser` int(11) NOT NULL,
  `seatNumber` int(11) NOT NULL,
  PRIMARY KEY (`idFlight`,`idUser`),
  KEY `fk_Flight_has_Person_Person1_idx` (`idUser`),
  KEY `fk_Flight_has_Person_Flight1_idx` (`idFlight`),
  KEY `fk_Flight_has_Person_Seats1_idx` (`seatNumber`),
  CONSTRAINT `fk_Flight_has_Person_Flight1` FOREIGN KEY (`idFlight`) REFERENCES `Flight` (`idFlight`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Flight_has_Person_Person1` FOREIGN KEY (`idUser`) REFERENCES `User` (`idUser`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Flight_has_Person_Seats1` FOREIGN KEY (`seatNumber`) REFERENCES `Seats` (`seatNumber`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Flight_has_User`
--

LOCK TABLES `Flight_has_User` WRITE;
/*!40000 ALTER TABLE `Flight_has_User` DISABLE KEYS */;
INSERT INTO `Flight_has_User` VALUES (1,11,1),(3,4,1),(3,11,1),(3,12,1),(4,12,3);
/*!40000 ALTER TABLE `Flight_has_User` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Plane`
--

DROP TABLE IF EXISTS `Plane`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Plane` (
  `idPlane` int(11) NOT NULL AUTO_INCREMENT,
  `modelCode` int(11) NOT NULL,
  `constructionDay` date NOT NULL,
  PRIMARY KEY (`idPlane`),
  KEY `fk_Plane_PlaneModel1_idx` (`modelCode`),
  CONSTRAINT `fk_Plane_PlaneModel1` FOREIGN KEY (`modelCode`) REFERENCES `PlaneModel` (`code`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Plane`
--

LOCK TABLES `Plane` WRITE;
/*!40000 ALTER TABLE `Plane` DISABLE KEYS */;
INSERT INTO `Plane` VALUES (1,1,'2018-05-15'),(2,2,'2018-04-25');
/*!40000 ALTER TABLE `Plane` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PlaneModel`
--

DROP TABLE IF EXISTS `PlaneModel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PlaneModel` (
  `code` int(11) NOT NULL AUTO_INCREMENT,
  `seatQuantity` int(11) NOT NULL,
  PRIMARY KEY (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PlaneModel`
--

LOCK TABLES `PlaneModel` WRITE;
/*!40000 ALTER TABLE `PlaneModel` DISABLE KEYS */;
INSERT INTO `PlaneModel` VALUES (1,5555),(2,555);
/*!40000 ALTER TABLE `PlaneModel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Seats`
--

DROP TABLE IF EXISTS `Seats`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Seats` (
  `seatNumber` int(11) NOT NULL AUTO_INCREMENT,
  `modelCode` int(11) NOT NULL,
  `seatClass` varchar(45) NOT NULL,
  PRIMARY KEY (`seatNumber`),
  KEY `fk_Seats_PlaneModel1_idx` (`modelCode`),
  CONSTRAINT `fk_Seats_PlaneModel1` FOREIGN KEY (`modelCode`) REFERENCES `PlaneModel` (`code`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Seats`
--

LOCK TABLES `Seats` WRITE;
/*!40000 ALTER TABLE `Seats` DISABLE KEYS */;
INSERT INTO `Seats` VALUES (1,1,'premium'),(2,1,'Turis'),(3,2,'normal'),(4,2,'premium');
/*!40000 ALTER TABLE `Seats` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `User` (
  `idUser` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `lastname` varchar(45) NOT NULL,
  `mail` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `administrador` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`idUser`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (4,'Sebastian','Elustondo','sebastianelustondo@gmail.com','Patuco20',1),(11,'nico','pru','np01@gmail.com','nico1234',0),(12,'Dario','Andreatini','TUPAPIRICO@GAMIL.COM','12345',0);
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-31 16:40:45
