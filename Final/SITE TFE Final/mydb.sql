-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le :  mar. 18 juin 2019 à 14:12
-- Version du serveur :  5.7.26
-- Version de PHP :  7.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `mydb`
--

-- --------------------------------------------------------

--
-- Structure de la table `attaques`
--

DROP TABLE IF EXISTS `attaques`;
CREATE TABLE IF NOT EXISTS `attaques` (
  `idAttaques` int(11) NOT NULL AUTO_INCREMENT,
  `Nom` varchar(45) DEFAULT NULL,
  `Force` int(11) DEFAULT NULL,
  `Precision` int(11) DEFAULT NULL,
  `Type` varchar(45) DEFAULT NULL,
  `skill-level` int(11) DEFAULT NULL,
  PRIMARY KEY (`idAttaques`)
) ENGINE=InnoDB AUTO_INCREMENT=95 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `attaques`
--

INSERT INTO `attaques` (`idAttaques`, `Nom`, `Force`, `Precision`, `Type`, `skill-level`) VALUES
(1, 'Absorb', 20, 100, 'grass', 10),
(2, 'Acid', 40, 100, 'poison', 8),
(3, 'Aurora Beam', 65, 100, 'ice', 40),
(4, 'Barrage', 35, 85, 'normal', 15),
(5, 'Bind', 35, 85, 'normal', 15),
(6, 'Bite', 60, 100, 'dark', 25),
(7, 'Blizzard', 110, 70, 'ice', 40),
(8, 'Body Slam', 85, 100, 'normal', 45),
(9, 'Bone Club', 65, 85, 'ground', 26),
(10, 'Bonemerang', 60, 90, 'ground', 26),
(11, 'Bubble', 40, 100, 'water', 13),
(12, 'Bubble Beam', 65, 100, 'water', 37),
(13, 'Clamp', 55, 85, 'water', 25),
(14, 'Comet Punch', 36, 85, 'normal', 34),
(15, 'Confusion', 50, 100, 'psychic', 50),
(16, 'Constrict', 10, 100, 'normal', 43),
(17, 'Crabhammer', 100, 90, 'water', 63),
(18, 'Cut', 50, 95, 'normal', 45),
(19, 'Dig', 80, 100, 'ground', 29),
(20, 'Dizzy Punch', 70, 100, 'normal', 43),
(21, 'Double Kick', 30, 100, 'fighting', 18),
(22, 'Double-Edge', 120, 100, 'normal', 61),
(23, 'Dragon Rage', 50, 100, 'dragon', 56),
(24, 'Dream Eater', 100, 100, 'psychic', 44),
(25, 'Drill Peck', 80, 100, 'flying', 37),
(26, 'Earthquake', 100, 100, 'ground', 55),
(27, 'Egg Bomb', 100, 75, 'normal', 43),
(28, 'Ember', 40, 100, 'fire', 15),
(29, 'Explosion', 250, 50, 'normal', 46),
(30, 'Fire Blast', 110, 85, 'fire', 52),
(31, 'Fire Punch', 75, 100, 'fire', 34),
(32, 'Flamethrower', 90, 100, 'fire', 34),
(33, 'Fly ', 90, 95, 'flying', 36),
(34, 'Fury Attack', 35, 100, 'normal', 34),
(35, 'Gust', 40, 100, 'flying', 24),
(36, 'Headbutt', 70, 100, 'normal', 60),
(37, 'High Jump Kick', 130, 80, 'fighting', 58),
(38, 'Horn Attack', 65, 100, 'normal', 43),
(39, 'Hydro Pump', 110, 80, 'water', 51),
(40, 'Hyper Beam', 150, 90, 'normal', 60),
(41, 'Hyper Fang', 80, 90, 'normal', 38),
(42, 'Ice Beam', 90, 100, 'ice', 45),
(43, 'Ice Punch', 75, 100, 'ice', 64),
(44, 'Jump Kick', 100, 75, 'Fighting', 37),
(45, 'Karate Chop', 50, 100, 'fighting', 24),
(46, 'Leech Life', 80, 100, 'grass', 41),
(47, 'Lick', 30, 100, 'ghost', 26),
(48, 'Mega Drain', 40, 100, 'grass', 32),
(49, 'Mega Kick', 120, 75, 'normal', 45),
(50, 'Mega Punch', 80, 85, 'normal', 34),
(51, 'Pay Day', 40, 100, 'normal', 22),
(52, 'Peck', 35, 100, 'flying', 26),
(53, 'Petal Dance', 120, 100, 'grass', 35),
(54, 'Pin Missile', 25, 95, 'bug', 26),
(55, 'Poison sting', 15, 100, 'poison', 27),
(56, 'Pound', 40, 100, 'normal', 34),
(57, 'Psybeam', 65, 100, 'psychic', 32),
(58, 'Psychic', 90, 100, 'psychic', 46),
(59, 'Quick attack', 40, 100, 'normal', 25),
(60, 'Rage', 20, 100, 'normal', 15),
(61, 'Razor Leaf', 55, 95, 'grass', 29),
(62, 'Razor Wind', 80, 100, 'normal', 41),
(63, 'Rock Slide', 50, 90, 'rock', 36),
(64, 'Rock Throw', 75, 90, 'rock', 45),
(65, 'Rolling Kick', 60, 85, 'Fighting', 37),
(66, 'Scratch', 40, 100, 'normal', 17),
(67, 'Self Destruct ', 200, 100, 'normal', 68),
(68, 'Skull Bash', 130, 100, 'normal', 62),
(69, 'Sky Attack', 140, 90, 'flying', 56),
(70, 'Slam', 80, 70, 'normal', 44),
(71, 'Slash', 70, 100, 'normal', 48),
(72, 'Sludge', 65, 100, 'poison', 37),
(73, 'Smog', 30, 100, 'poison', 27),
(74, 'Solar Beam', 120, 100, 'grass', 53),
(75, 'Stomp', 65, 100, 'normal', 54),
(76, 'Strength', 80, 100, 'normal', 60),
(77, 'Struggle', 50, 100, 'normal', 26),
(78, 'Submission', 80, 80, 'fighting', 53),
(79, 'Surf', 90, 100, 'water', 40),
(80, 'Swift', 60, 100, 'normal', 43),
(81, 'Tackle', 40, 100, 'normal', 35),
(82, 'Take Down', 90, 85, 'normal', 66),
(83, 'Thrash', 120, 100, 'normal', 68),
(84, 'Thunder', 110, 70, 'electric', 45),
(85, 'Thunder Punch', 75, 100, 'electric', 33),
(86, 'Thunder Shock', 40, 100, 'electric', 21),
(87, 'Thunderbolt', 90, 100, 'electric', 52),
(88, 'Tri Attack', 80, 100, 'normal', 33),
(89, 'Twineedle', 25, 100, 'bug', 19),
(90, 'Vice grip', 55, 100, 'normal', 25),
(91, 'vine whip', 45, 100, 'grass', 30),
(92, 'Water Gun', 40, 100, 'water', 37),
(93, 'Waterfall', 80, 100, 'water', 69),
(94, 'Wing Attack', 60, 100, 'flying', 39);

-- --------------------------------------------------------

--
-- Structure de la table `attaquespokemon`
--

DROP TABLE IF EXISTS `attaquespokemon`;
CREATE TABLE IF NOT EXISTS `attaquespokemon` (
  `idAttaquesPokemon` int(11) NOT NULL AUTO_INCREMENT,
  `Attaques_idAttaques` int(11) NOT NULL,
  `appartientpokemon` int(11) NOT NULL,
  PRIMARY KEY (`idAttaquesPokemon`),
  KEY `cle secondaire pokemon` (`appartientpokemon`),
  KEY `cle secondaire attaques` (`Attaques_idAttaques`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `basepokemon`
--

DROP TABLE IF EXISTS `basepokemon`;
CREATE TABLE IF NOT EXISTS `basepokemon` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Nom` varchar(45) NOT NULL,
  `Type` varchar(45) NOT NULL,
  `HPMAX` int(11) NOT NULL,
  `Vitesse` int(11) NOT NULL,
  `Attaque` int(11) NOT NULL,
  `Defence` int(11) NOT NULL,
  `Special` int(11) NOT NULL,
  `numberofuses` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=152 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `basepokemon`
--

INSERT INTO `basepokemon` (`id`, `Nom`, `Type`, `HPMAX`, `Vitesse`, `Attaque`, `Defence`, `Special`, `numberofuses`) VALUES
(1, 'Bulbasaur', 'grass,poison', 45, 45, 49, 49, 65, 0),
(2, 'Ivysaur', 'grass,poison', 60, 60, 62, 63, 80, 0),
(3, 'Venusaur', 'grass,poison', 80, 80, 82, 83, 100, 0),
(4, 'Charmander', 'fire', 39, 65, 52, 43, 55, 0),
(5, 'Charmeleon', 'fire', 58, 80, 64, 58, 73, 0),
(6, 'Charizard', 'fire,flying', 78, 100, 84, 78, 94, 0),
(7, 'Squirtle', 'water', 44, 43, 48, 65, 57, 0),
(8, 'Wartortle', 'water', 59, 58, 63, 80, 73, 0),
(9, 'Blastoise', 'water', 79, 78, 83, 100, 95, 0),
(10, 'Caterpie', 'bug', 45, 45, 30, 35, 20, 0),
(11, 'Metapod', 'bug', 50, 30, 20, 55, 25, 0),
(12, 'Butterfree', 'bug,flying', 60, 70, 45, 50, 58, 0),
(13, 'Weedle', 'bug,poison', 40, 50, 35, 30, 20, 0),
(14, 'Kakuna', 'bug,poison', 45, 35, 25, 50, 25, 0),
(15, 'Beedril', 'bug,poison', 65, 75, 90, 40, 65, 0),
(16, 'Pidgey', 'normal,flying', 40, 56, 45, 40, 35, 0),
(17, 'Pidgeotto', 'normal,flying', 63, 71, 60, 55, 50, 0),
(18, 'Pidgeot', 'normal,flying', 83, 101, 80, 75, 70, 0),
(19, 'Rattata', 'normal', 30, 72, 56, 35, 30, 0),
(20, 'Raticate', 'normal', 55, 97, 81, 60, 60, 0),
(21, 'Spearow', 'normal,flying', 40, 70, 60, 30, 31, 0),
(22, 'Fearow', 'normal,flying', 65, 100, 90, 65, 61, 0),
(23, 'ekans', 'poison', 35, 55, 60, 44, 47, 0),
(24, 'Arbok', 'Poison', 60, 80, 95, 69, 72, 0),
(25, 'Pikachu', 'electric', 35, 90, 55, 40, 50, 0),
(26, 'Raichu', 'electric', 60, 110, 90, 55, 85, 0),
(27, 'Sandshrew', 'ground', 50, 40, 75, 85, 25, 0),
(28, 'Sandslash', 'ground', 75, 65, 100, 110, 50, 0),
(29, 'Nidoran♀', 'Poison', 55, 41, 47, 52, 40, 0),
(30, 'Nidorina', 'Poison', 70, 56, 62, 67, 55, 0),
(31, 'Nidoqueen', 'poison,ground', 90, 76, 92, 87, 80, 0),
(32, 'Nidoran♂', 'poison', 46, 50, 57, 40, 40, 0),
(33, 'Nidorino', 'poison', 61, 65, 72, 57, 55, 0),
(34, 'Nidoking', 'poison,ground', 81, 85, 102, 77, 80, 0),
(35, 'Clefairy', 'fairy', 70, 35, 45, 48, 63, 0),
(36, 'Clefable', 'fairy', 95, 60, 70, 73, 90, 0),
(37, 'Vulpix', 'fire', 38, 65, 41, 40, 65, 0),
(38, 'Ninetailes', 'fire', 73, 100, 76, 75, 90, 0),
(39, 'Jigglypuff', 'normal,fairy', 115, 20, 45, 20, 35, 0),
(40, 'Wigglytuff', 'normal,fairy', 140, 45, 70, 45, 67, 0),
(41, 'Zubat', 'poison,flying', 40, 55, 45, 35, 35, 0),
(42, 'Golbat', 'poison,flying', 75, 90, 80, 70, 70, 0),
(43, 'Oddish', 'grass,poison', 45, 30, 50, 55, 70, 0),
(44, 'Gloom', 'grass,poison', 60, 40, 65, 70, 80, 0),
(45, 'Vileplume', 'grass,poison', 75, 50, 80, 85, 100, 0),
(46, 'Paras', 'bug,grass', 35, 25, 70, 55, 50, 0),
(47, 'parasect', 'bug,grass', 60, 30, 95, 80, 70, 0),
(48, 'Venonat', 'bug,poison', 60, 45, 55, 50, 47, 0),
(49, 'Venomoth', 'bug,poison', 70, 90, 65, 60, 83, 0),
(50, 'Diglett', 'ground', 10, 95, 55, 25, 40, 0),
(51, 'Dugtrio', 'ground', 35, 120, 100, 50, 60, 0),
(52, 'Meowth', 'normal', 40, 90, 45, 35, 40, 0),
(53, 'Persian', 'normal', 65, 115, 70, 60, 65, 0),
(54, 'Psyduck', 'water', 50, 55, 52, 48, 57, 0),
(55, 'Golduck', 'water', 80, 85, 82, 78, 87, 0),
(56, 'Mankey', 'fighting', 40, 70, 80, 35, 40, 0),
(57, 'Primeape', 'fighting', 65, 95, 105, 60, 65, 0),
(58, 'Growlithe', 'fire', 55, 60, 70, 45, 60, 0),
(59, 'Arcanine', 'fire', 90, 95, 110, 80, 90, 0),
(60, 'poliwag', 'water', 40, 90, 80, 40, 40, 0),
(61, 'polywhirl', 'water', 65, 90, 65, 65, 50, 0),
(62, 'poliwrath', 'water,fighting', 90, 70, 95, 95, 80, 0),
(63, 'Abra', 'psychic', 25, 90, 20, 15, 80, 0),
(64, 'Kadabra', 'psychic', 40, 105, 35, 30, 90, 0),
(65, 'Alakazam', 'psychic', 55, 120, 50, 45, 115, 0),
(66, 'Machop', 'fighting', 70, 35, 80, 50, 35, 0),
(67, 'Machoke', 'fighting', 80, 45, 100, 70, 55, 0),
(68, 'Machamp', 'fighting', 90, 55, 130, 80, 75, 0),
(69, 'Bellsprout', 'grass,poison', 50, 40, 75, 35, 50, 0),
(70, 'Weepinbell', 'grass,poison', 65, 55, 90, 50, 65, 0),
(71, 'Victreebell', 'grass,poison', 80, 70, 105, 65, 85, 0),
(72, 'tentacool', 'water,poison', 40, 70, 40, 35, 75, 0),
(73, 'Tentacruel', 'water,poison', 80, 100, 70, 65, 100, 0),
(74, 'Geodude', 'rock,ground', 40, 20, 80, 100, 30, 0),
(75, 'Graveler', 'rock,ground', 55, 35, 95, 115, 45, 0),
(76, 'Golem', 'rock,ground', 80, 45, 120, 130, 60, 0),
(77, 'Ponyta', 'fire', 50, 90, 85, 55, 65, 0),
(78, 'Rapidash', 'fire', 65, 105, 100, 70, 80, 0),
(79, 'Slowpoke', 'water,psychic', 90, 15, 65, 65, 40, 0),
(80, 'Slowbro', 'water,psychic', 95, 30, 75, 110, 90, 0),
(81, 'Magnemite', 'electric,steel', 25, 45, 35, 70, 75, 0),
(82, 'Magneton', 'electric,steel', 50, 70, 60, 95, 120, 0),
(83, 'Farfetch\'d', 'normal,flying', 52, 60, 90, 55, 60, 0),
(84, 'Doduo', 'normal,flying', 35, 75, 85, 45, 35, 0),
(85, 'Dodrio', 'normal,flying', 60, 110, 110, 70, 60, 0),
(86, 'Seel', 'water', 65, 45, 45, 55, 57, 0),
(87, 'Dewgong', 'water,ice', 90, 70, 70, 80, 83, 0),
(88, 'Grimer', 'poison', 80, 25, 80, 50, 45, 0),
(89, 'Muk', 'poison', 105, 50, 105, 75, 87, 0),
(90, 'Shelder', 'water', 30, 40, 65, 100, 35, 0),
(91, 'Cloyster', 'water,ice', 50, 70, 95, 180, 65, 0),
(92, 'Gastly', 'ghost,poison', 30, 80, 35, 30, 65, 0),
(93, 'Haunter', 'ghost,poison', 45, 95, 50, 45, 85, 0),
(94, 'Gengar', 'ghost,poison', 60, 110, 65, 65, 103, 0),
(95, 'Onix', 'rock,ground', 35, 70, 45, 160, 37, 0),
(96, 'Drowzee', 'psychic', 60, 42, 48, 45, 83, 0),
(97, 'Hypno', 'psychic', 85, 67, 73, 70, 90, 0),
(98, 'Krabby', 'water', 30, 50, 105, 90, 25, 0),
(99, 'Kingler', 'water', 55, 75, 130, 115, 50, 0),
(100, 'Voltorb', 'electric', 40, 100, 30, 50, 55, 0),
(101, 'Electrode', 'electric', 60, 150, 50, 70, 80, 0),
(102, 'Exeggcute', 'grass,psychic', 60, 40, 40, 80, 52, 0),
(103, 'Exeggutor', 'grass,psychic', 95, 55, 95, 85, 90, 0),
(104, 'Cubone', 'ground', 50, 35, 50, 95, 45, 0),
(105, 'Marowak', 'ground', 60, 45, 80, 110, 65, 0),
(106, 'Hitmonlee', 'fighting', 50, 87, 120, 53, 77, 0),
(107, 'Hitmonchan', 'fighting', 50, 76, 105, 79, 77, 0),
(108, 'Lickitung', 'normal', 90, 30, 55, 75, 67, 0),
(109, 'Koffing', 'poison', 40, 35, 65, 95, 57, 0),
(110, 'Weezing', 'poison', 65, 60, 90, 120, 77, 0),
(111, 'Rhyhorn', 'ground,rock', 80, 25, 85, 95, 30, 0),
(112, 'Rhydon', 'ground,rock', 105, 40, 130, 120, 45, 0),
(113, 'Chansey', 'normal', 250, 50, 5, 5, 73, 0),
(114, 'Tangela', 'grass', 65, 60, 55, 115, 70, 0),
(115, 'Kangaskhan', 'normal', 105, 90, 95, 80, 60, 0),
(116, 'Horsea', 'water', 30, 60, 40, 70, 50, 0),
(117, 'Seadra', 'water', 55, 85, 65, 95, 70, 0),
(118, 'Goldeen', 'water', 45, 63, 67, 60, 35, 0),
(119, 'Seaking', 'water', 80, 68, 92, 65, 73, 0),
(120, 'Staryu', 'water', 30, 85, 45, 55, 63, 0),
(121, 'Starmie', 'water,psychic', 60, 115, 75, 85, 93, 0),
(122, 'Mr. Mime', 'psychic,fairy', 40, 90, 45, 65, 110, 0),
(123, 'Scyther', 'bug,flying', 70, 105, 110, 80, 67, 0),
(124, 'Jynx', 'ice,psychic', 65, 95, 50, 35, 105, 0),
(125, 'Electabuzz', 'electric', 65, 105, 83, 57, 90, 0),
(126, 'Magmar', 'fire', 65, 93, 95, 57, 93, 0),
(127, 'Pinsir', 'bug', 65, 85, 125, 100, 63, 0),
(128, 'Tauros', 'normal', 75, 110, 100, 95, 55, 0),
(129, 'Magikarp', 'water', 20, 80, 10, 55, 17, 0),
(130, 'Gyarados', 'water,flying', 95, 81, 125, 79, 80, 0),
(131, 'Lapras', 'water,ice', 130, 60, 85, 80, 90, 0),
(132, 'Ditto', 'normal', 48, 48, 48, 48, 48, 0),
(133, 'Eevee', 'normal', 55, 55, 55, 50, 55, 0),
(134, 'Vaporeon', 'water', 130, 65, 65, 60, 102, 0),
(135, 'Jolteon', 'electric', 65, 130, 65, 60, 103, 0),
(136, 'Flareon', 'fire', 65, 65, 130, 60, 103, 0),
(137, 'Porygon', 'normal', 65, 40, 60, 70, 80, 0),
(138, 'Omanyte', 'rock,water', 35, 35, 40, 100, 77, 0),
(139, 'Omastar', 'rock,water', 70, 55, 60, 125, 87, 0),
(140, 'Kabuto', 'rock,water', 30, 55, 80, 90, 50, 0),
(141, 'Kabutops', 'rock,water', 60, 80, 115, 105, 67, 0),
(142, 'Aerodactyl', 'rock,flying', 80, 130, 105, 65, 67, 0),
(143, 'Snorlax', 'normal', 160, 30, 110, 65, 87, 0),
(144, 'Articuno', 'ice,flying', 90, 85, 85, 100, 110, 0),
(145, 'Zapdos', 'electric,flying', 90, 100, 90, 85, 113, 0),
(146, 'Moltres', 'fire,flying', 90, 90, 100, 90, 105, 0),
(147, 'Dratini', 'dragon', 41, 50, 64, 45, 50, 0),
(148, 'Dragonair', 'dragon', 61, 70, 84, 65, 70, 0),
(149, 'Dragonite', 'dragon,flying', 91, 80, 134, 95, 100, 0),
(150, 'Mewtwo', 'psychic', 106, 130, 110, 90, 122, 0),
(151, 'Mew', 'psychic', 100, 100, 100, 100, 100, 0);

-- --------------------------------------------------------

--
-- Structure de la table `equipe`
--

DROP TABLE IF EXISTS `equipe`;
CREATE TABLE IF NOT EXISTS `equipe` (
  `idEquipe` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`idEquipe`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `joueur`
--

DROP TABLE IF EXISTS `joueur`;
CREATE TABLE IF NOT EXISTS `joueur` (
  `idJoueur` int(11) NOT NULL AUTO_INCREMENT,
  `Nom` varchar(45) DEFAULT NULL,
  `Prenom` varchar(45) DEFAULT NULL,
  `Mail` varchar(45) DEFAULT NULL,
  `Login` varchar(45) DEFAULT NULL,
  `MDP` varchar(45) DEFAULT NULL,
  `nbwins` int(11) DEFAULT NULL,
  `nbparties` int(11) DEFAULT NULL,
  `scoremax` int(11) DEFAULT NULL,
  PRIMARY KEY (`idJoueur`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `joueur`
--

INSERT INTO `joueur` (`idJoueur`, `Nom`, `Prenom`, `Mail`, `Login`, `MDP`, `nbwins`, `nbparties`, `scoremax`) VALUES
(2, 'azdsvsddv', 'Adrien', 'amontariol3@gmail.com', '123456', 'e10adc3949ba59abbe56e057f20f883e', 2, 2, 2),
(3, 'Montariol', 'Adrien', 'sivydv@gmail.com', '123', '202cb962ac59075b964b07152d234b70', 0, 0, 0),
(4, 'Montariol', 'Adrien', 'rgvdv@gmail.com', '153', 'b3e3e393c77e35a4a3f3cbd1e429b5dc', 0, 0, 0);

-- --------------------------------------------------------

--
-- Structure de la table `objets`
--

DROP TABLE IF EXISTS `objets`;
CREATE TABLE IF NOT EXISTS `objets` (
  `idObjets` int(11) NOT NULL AUTO_INCREMENT,
  `Nom` varchar(45) DEFAULT NULL,
  `quantité` int(11) NOT NULL,
  `refsac` int(11) NOT NULL,
  PRIMARY KEY (`idObjets`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `objetsbase`
--

DROP TABLE IF EXISTS `objetsbase`;
CREATE TABLE IF NOT EXISTS `objetsbase` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `personnage`
--

DROP TABLE IF EXISTS `personnage`;
CREATE TABLE IF NOT EXISTS `personnage` (
  `idPersonnage` int(11) NOT NULL AUTO_INCREMENT,
  `Equipe_idEquipe` int(11) NOT NULL,
  `Sac_idSac` int(11) NOT NULL,
  PRIMARY KEY (`idPersonnage`),
  KEY `Cle secondaire notre equipe` (`Equipe_idEquipe`),
  KEY `cle secondaire sac` (`Sac_idSac`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `pnj`
--

DROP TABLE IF EXISTS `pnj`;
CREATE TABLE IF NOT EXISTS `pnj` (
  `idPNJ` int(11) NOT NULL AUTO_INCREMENT,
  `Nom` varchar(45) DEFAULT NULL,
  `Type` varchar(45) DEFAULT NULL,
  `Equipe_idEquipe` int(11) NOT NULL,
  PRIMARY KEY (`idPNJ`),
  KEY `clesecondaireequipe` (`Equipe_idEquipe`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `pokemon`
--

DROP TABLE IF EXISTS `pokemon`;
CREATE TABLE IF NOT EXISTS `pokemon` (
  `idPokemon` int(11) NOT NULL AUTO_INCREMENT,
  `Numero` int(11) NOT NULL,
  `Nom` varchar(45) DEFAULT NULL,
  `Type` varchar(45) NOT NULL,
  `lvl` int(11) NOT NULL,
  `Hp` int(11) DEFAULT NULL,
  `HPMAX` int(11) NOT NULL,
  `Vitesse` int(11) DEFAULT NULL,
  `Attaque` int(11) DEFAULT NULL,
  `Defence` int(11) DEFAULT NULL,
  `Special` int(11) DEFAULT NULL,
  `appartientequipe` int(11) NOT NULL,
  PRIMARY KEY (`idPokemon`),
  KEY `Cle secondaire equipe` (`appartientequipe`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `sac`
--

DROP TABLE IF EXISTS `sac`;
CREATE TABLE IF NOT EXISTS `sac` (
  `idSac` int(11) NOT NULL,
  PRIMARY KEY (`idSac`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `attaquespokemon`
--
ALTER TABLE `attaquespokemon`
  ADD CONSTRAINT `cle_secondaire_attaques` FOREIGN KEY (`Attaques_idAttaques`) REFERENCES `attaques` (`idAttaques`),
  ADD CONSTRAINT `cle_secondaire_pokemon` FOREIGN KEY (`appartientpokemon`) REFERENCES `pokemon` (`idPokemon`);

--
-- Contraintes pour la table `personnage`
--
ALTER TABLE `personnage`
  ADD CONSTRAINT `clesecondaireequipe2` FOREIGN KEY (`Equipe_idEquipe`) REFERENCES `equipe` (`idEquipe`),
  ADD CONSTRAINT `clesecondairesacoui` FOREIGN KEY (`Sac_idSac`) REFERENCES `sac` (`idSac`);

--
-- Contraintes pour la table `pnj`
--
ALTER TABLE `pnj`
  ADD CONSTRAINT `clesecondaireequipe3` FOREIGN KEY (`Equipe_idEquipe`) REFERENCES `equipe` (`idEquipe`);

--
-- Contraintes pour la table `pokemon`
--
ALTER TABLE `pokemon`
  ADD CONSTRAINT `clesecondaireequipe1` FOREIGN KEY (`appartientequipe`) REFERENCES `equipe` (`idEquipe`);

--
-- Contraintes pour la table `sac`
--
ALTER TABLE `sac`
  ADD CONSTRAINT `clesecondairesac` FOREIGN KEY (`idSac`) REFERENCES `objets` (`idObjets`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
