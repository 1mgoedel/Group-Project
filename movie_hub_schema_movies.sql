-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: movie_hub_schema
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `movies`
--

DROP TABLE IF EXISTS `movies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movies` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `poster` varchar(255) DEFAULT NULL,
  `plot` longtext,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movies`
--

LOCK TABLES `movies` WRITE;
/*!40000 ALTER TABLE `movies` DISABLE KEYS */;
INSERT INTO `movies` VALUES (1,'Star Wars: Episode V - The Empire Strikes Back','movie_posters/Star_Wars__Episode_V_-_The_Empire_Strikes_Back.jpg','After the Rebels are overpowered by the Empire, Luke Skywalker begins his Jedi training with Yoda, while his friends are pursued across the galaxy by Darth Vader and bounty hunter Boba Fett.','2024-03-27 22:37:10','2024-03-27 22:37:10'),(2,'The Incredibles','movie_posters/The_Incredibles.jpg','While trying to lead a quiet suburban life, a family of undercover superheroes are forced into action to save the world.','2024-03-27 22:39:10','2024-03-27 22:39:10'),(3,'Groundhog Day','movie_posters/Groundhog_Day.jpg','A narcissistic, self-centered weatherman finds himself in a time loop on Groundhog Day.','2024-03-27 22:39:46','2024-03-27 22:39:46'),(4,'Mad Max: Fury Road','movie_posters/Mad_Max__Fury_Road.jpg','In a post-apocalyptic wasteland, a woman rebels against a tyrannical ruler in search for her homeland with the aid of a group of female prisoners, a psychotic worshiper and a drifter named Max.','2024-03-27 22:40:21','2024-03-27 22:40:21'),(5,'Pirates of the Caribbean: The Curse of the Black Pearl','movie_posters/Pirates_of_the_Caribbean__The_Curse_of_the_Black_Pearl.jpg','Blacksmith Will Turner teams up with eccentric pirate \"Captain\" Jack Sparrow to save his love, the governor\'s daughter, from Jack\'s former pirate allies, who are now undead.','2024-03-27 22:41:03','2024-03-27 22:41:03'),(6,'The Terminator','movie_posters/The_Terminator.jpg','A human soldier is sent from 2029 to 1984 to stop an almost indestructible cyborg killing machine, sent from the same year, which has been programmed to execute a young woman whose unborn son is the key to humanity\'s future salvat...','2024-03-27 22:41:42','2024-03-27 22:41:42'),(7,'Jaws','movie_posters/Jaws.jpg','When a killer shark unleashes chaos on a beach community off Cape Cod, it\'s up to a local sheriff, a marine biologist, and an old seafarer to hunt the beast down.','2024-03-27 22:42:15','2024-03-27 22:42:15'),(8,'Ratatouille','movie_posters/Ratatouille.jpg','A rat who can cook makes an unusual alliance with a young kitchen worker at a famous Paris restaurant.','2024-03-27 22:42:43','2024-03-27 22:42:43'),(9,'Monsters, Inc.','movie_posters/Monsters,_Inc..jpg','In order to power the city, monsters have to scare children so that they scream. However, the children are toxic to the monsters, and after a child gets through, two monsters realize things may not be what they think.','2024-03-27 22:43:24','2024-03-27 22:43:24'),(10,'My Neighbor Totoro','movie_posters/My_Neighbor_Totoro.jpg','When two girls move to the country to be near their ailing mother, they have adventures with the wondrous forest spirits who live nearby.','2024-03-27 22:43:53','2024-03-27 22:43:53'),(11,'Avatar','movie_posters/Avatar.jpg','A paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.','2024-03-28 01:22:22','2024-03-28 01:22:22'),(12,'Cars 2','movie_posters/Cars_2.jpg','Star race car Lightning McQueen and his pal Mater head overseas to compete in the World Grand Prix race. But the road to the championship becomes rocky as Mater gets caught up in an intriguing adventure of his own: international e...','2024-03-28 01:39:35','2024-03-28 01:39:35');
/*!40000 ALTER TABLE `movies` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-28  2:37:08
