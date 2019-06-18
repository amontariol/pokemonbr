BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "attaques" (
	"idAttaques"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"Nom"	VARCHAR(45) DEFAULT NULL COLLATE NOCASE,
	"Force"	INT DEFAULT NULL,
	"Precision"	INT DEFAULT NULL,
	"Type"	VARCHAR(45) DEFAULT NULL COLLATE NOCASE,
	"skilllevel"	INT DEFAULT NULL
);
CREATE TABLE IF NOT EXISTS "personnage" (
	"idPersonnage"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"Equipe_idEquipe"	INT NOT NULL,
	"Sac_idSac"	INT NOT NULL,
	CONSTRAINT "clesecondaireequipe2" FOREIGN KEY("Equipe_idEquipe") REFERENCES "equipe"("idEquipe") ON DELETE RESTRICT ON UPDATE RESTRICT,
	CONSTRAINT "clesecondairesacoui" FOREIGN KEY("Sac_idSac") REFERENCES "sac"("idSac") ON DELETE RESTRICT ON UPDATE RESTRICT
);
CREATE TABLE IF NOT EXISTS "attaquespokemon" (
	"idAttaquesPokemon"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"Attaques_idAttaques"	INT NOT NULL,
	"appartientpokemon"	INT NOT NULL,
	CONSTRAINT "cle_secondaire_attaques" FOREIGN KEY("Attaques_idAttaques") REFERENCES "attaques"("idAttaques") ON DELETE RESTRICT ON UPDATE RESTRICT,
	CONSTRAINT "cle_secondaire_pokemon" FOREIGN KEY("appartientpokemon") REFERENCES "pokemon"("idPokemon") ON DELETE RESTRICT ON UPDATE RESTRICT
);
CREATE TABLE IF NOT EXISTS "pokemon" (
	"idPokemon"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"Numero"	INT NOT NULL,
	"Nom"	VARCHAR(45) DEFAULT NULL COLLATE NOCASE,
	"Type"	VARCHAR(45) NOT NULL COLLATE NOCASE,
	"lvl"	INT NOT NULL,
	"Hp"	INT DEFAULT NULL,
	"HPMAX"	INT NOT NULL,
	"Vitesse"	INT DEFAULT NULL,
	"Attaque"	INT DEFAULT NULL,
	"Defence"	INT DEFAULT NULL,
	"Special"	INT DEFAULT NULL,
	"appartientequipe"	INT NOT NULL,
	CONSTRAINT "clesecondaireequipe1" FOREIGN KEY("appartientequipe") REFERENCES "equipe"("idEquipe") ON DELETE RESTRICT ON UPDATE RESTRICT
);
CREATE TABLE IF NOT EXISTS "pnj" (
	"idPNJ"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"Nom"	VARCHAR(45) DEFAULT NULL COLLATE NOCASE,
	"Type"	VARCHAR(45) DEFAULT NULL COLLATE NOCASE,
	"Equipe_idEquipe"	INT NOT NULL,
	CONSTRAINT "clesecondaireequipe3" FOREIGN KEY("Equipe_idEquipe") REFERENCES "equipe"("idEquipe") ON DELETE RESTRICT ON UPDATE RESTRICT
);
CREATE TABLE IF NOT EXISTS "objetsbase" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"nom"	VARCHAR(50) NOT NULL COLLATE NOCASE
);
CREATE TABLE IF NOT EXISTS "sac" (
	"idSac"	INT NOT NULL,
	PRIMARY KEY("idSac"),
	CONSTRAINT "clesecondairesac" FOREIGN KEY("idSac") REFERENCES "objets"("idObjets") ON DELETE RESTRICT ON UPDATE RESTRICT
);
CREATE TABLE IF NOT EXISTS "joueur" (
	"idJoueur"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"Nom"	VARCHAR(45) DEFAULT NULL COLLATE NOCASE,
	"Prenom"	VARCHAR(45) DEFAULT NULL COLLATE NOCASE,
	"Mail"	VARCHAR(45) DEFAULT NULL COLLATE NOCASE,
	"Login"	VARCHAR(45) DEFAULT NULL COLLATE NOCASE,
	"MDP"	VARCHAR(45) DEFAULT NULL COLLATE NOCASE,
	"nbwins"	INT DEFAULT NULL,
	"nbparties"	INT DEFAULT NULL,
	"scoremax"	INT DEFAULT NULL
);
CREATE TABLE IF NOT EXISTS "objets" (
	"idObjets"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"Nom"	VARCHAR(45) DEFAULT NULL COLLATE NOCASE,
	"quantité"	INT NOT NULL,
	"refsac"	INT NOT NULL
);
CREATE TABLE IF NOT EXISTS "basepokemon" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"Nom"	VARCHAR(45) NOT NULL COLLATE NOCASE,
	"Type"	VARCHAR(45) NOT NULL COLLATE NOCASE,
	"HPMAX"	INT NOT NULL,
	"Vitesse"	INT NOT NULL,
	"Attaque"	INT NOT NULL,
	"Defence"	INT NOT NULL,
	"Special"	INT NOT NULL,
	"numberofuses"	INT NOT NULL
);
CREATE TABLE IF NOT EXISTS "equipe" (
	"idEquipe"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT
);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (1,'Absorb',20,100,'grass',10);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (2,'Acid',40,100,'poison',8);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (3,'Aurora Beam',65,100,'ice',30);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (4,'Barrage',35,85,'normal',15);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (5,'Bind',35,85,'normal',12);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (6,'Bite',60,100,'dark',25);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (7,'Blizzard',110,70,'ice',40);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (8,'Body Slam',85,100,'normal',45);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (9,'Bone Club',65,85,'ground',19);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (10,'Bonemerang',60,90,'ground',26);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (11,'Bubble',40,100,'water',13);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (12,'Bubble Beam',65,100,'water',37);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (13,'Clamp',55,85,'water',25);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (14,'Comet Punch',36,85,'normal',34);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (15,'Confusion',50,100,'psychic',50);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (16,'Constrict',10,100,'normal',42);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (17,'Crabhammer',100,90,'water',63);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (18,'Cut',50,95,'normal',45);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (19,'Dig',80,100,'ground',29);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (20,'Dizzy Punch',70,100,'normal',45);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (21,'Double Kick',30,100,'fighting',18);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (22,'Double-Edge',120,100,'normal',61);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (23,'Dragon Rage',50,100,'dragon',56);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (24,'Dream Eater',100,100,'psychic',57);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (25,'Drill Peck',80,100,'flying',37);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (26,'Earthquake',100,100,'ground',55);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (27,'Egg Bomb',100,75,'normal',47);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (28,'Ember',40,100,'fire',15);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (29,'Explosion',250,50,'normal',46);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (30,'Fire Blast',110,85,'fire',52);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (31,'Fire Punch',75,100,'fire',34);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (32,'Flamethrower',90,100,'fire',42);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (33,'Fly ',90,95,'flying',36);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (34,'Fury Attack',35,100,'normal',29);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (35,'Gust',40,100,'flying',24);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (36,'Headbutt',70,100,'normal',58);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (37,'High Jump Kick',130,80,'fighting',58);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (38,'Horn Attack',65,100,'normal',43);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (39,'Hydro Pump',110,80,'water',51);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (40,'Hyper Beam',150,90,'normal',57);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (41,'Hyper Fang',80,90,'normal',38);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (42,'Ice Beam',90,100,'ice',45);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (43,'Ice Punch',75,100,'ice',64);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (44,'Jump Kick',100,75,'Fighting',37);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (45,'Karate Chop',50,100,'fighting',24);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (46,'Leech Life',80,100,'grass',41);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (47,'Lick',30,100,'ghost',26);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (48,'Mega Drain',40,100,'grass',32);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (49,'Mega Kick',120,75,'normal',45);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (50,'Mega Punch',80,85,'normal',37);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (51,'Pay Day',40,100,'normal',22);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (52,'Peck',35,100,'flying',26);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (53,'Petal Dance',120,100,'grass',35);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (54,'Pin Missile',25,95,'bug',26);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (55,'Poison sting',15,100,'poison',27);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (56,'Pound',40,100,'normal',32);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (57,'Psybeam',65,100,'psychic',32);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (58,'Psychic',90,100,'psychic',44);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (59,'Quick attack',40,100,'normal',25);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (60,'Rage',20,100,'normal',18);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (61,'Razor Leaf',55,95,'grass',29);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (62,'Razor Wind',80,100,'normal',41);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (63,'Rock Slide',50,90,'rock',36);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (64,'Rock Throw',75,90,'rock',45);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (65,'Rolling Kick',60,85,'Fighting',31);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (66,'Scratch',40,100,'normal',17);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (67,'Self Destruct ',200,100,'normal',67);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (68,'Skull Bash',130,100,'normal',62);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (69,'Sky Attack',140,90,'flying',56);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (70,'Slam',80,70,'normal',44);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (71,'Slash',70,100,'normal',48);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (72,'Sludge',65,100,'poison',37);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (73,'Smog',30,100,'poison',47);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (74,'Solar Beam',120,100,'grass',53);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (75,'Stomp',65,100,'normal',54);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (76,'Strength',80,100,'normal',60);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (77,'Struggle',50,100,'normal',26);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (78,'Submission',80,80,'fighting',53);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (79,'Surf',90,100,'water',40);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (80,'Swift',60,100,'normal',40);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (81,'Tackle',40,100,'normal',35);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (82,'Take Down',90,85,'normal',66);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (83,'Thrash',120,100,'normal',68);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (84,'Thunder',110,70,'electric',45);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (85,'Thunder Punch',75,100,'electric',33);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (86,'Thunder Shock',40,100,'electric',21);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (87,'Thunderbolt',90,100,'electric',52);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (88,'Tri Attack',80,100,'normal',33);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (89,'Twineedle',25,100,'bug',19);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (90,'Vice grip',55,100,'normal',27);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (91,'vine whip',45,100,'grass',30);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (92,'Water Gun',40,100,'water',21);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (93,'Waterfall',80,100,'water',69);
INSERT INTO "attaques" ("idAttaques","Nom","Force","Precision","Type","skilllevel") VALUES (94,'Wing Attack',60,100,'flying',39);
INSERT INTO "joueur" ("idJoueur","Nom","Prenom","Mail","Login","MDP","nbwins","nbparties","scoremax") VALUES (9,'azdsvsddv','Adrien','amontariol3@gmail.com','123456','e10adc3949ba59abbe56e057f20f883e',NULL,NULL,NULL);
INSERT INTO "joueur" ("idJoueur","Nom","Prenom","Mail","Login","MDP","nbwins","nbparties","scoremax") VALUES (10,'montariol','eric','oui@mail.com','123','202cb962ac59075b964b07152d234b70',NULL,NULL,NULL);
INSERT INTO "joueur" ("idJoueur","Nom","Prenom","Mail","Login","MDP","nbwins","nbparties","scoremax") VALUES (11,'azdsvsddv','Adrien','amontariol3@gmail.com','12','c20ad4d76fe97759aa27a0c99bff6710',NULL,NULL,NULL);
INSERT INTO "joueur" ("idJoueur","Nom","Prenom","Mail","Login","MDP","nbwins","nbparties","scoremax") VALUES (12,'azdsvsddv','Adrien','amontariol3@gmail.com','oui','14b8f0494c6f1460c3720d0ce692dbca',NULL,NULL,NULL);
INSERT INTO "joueur" ("idJoueur","Nom","Prenom","Mail","Login","MDP","nbwins","nbparties","scoremax") VALUES (13,'Montariol','Adrien','amontariol@gmail.com','nul','40a8712b29ac76182ed0c4f632b7d543',NULL,NULL,NULL);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (1,'Bulbasaur','grass,poison',45,45,49,49,65,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (2,'Ivysaur','grass,poison',60,60,62,63,80,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (3,'Venusaur','grass,poison',80,80,82,83,100,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (4,'Charmander','fire',39,65,52,43,55,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (5,'Charmeleon','fire',58,80,64,58,73,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (6,'Charizard','fire,flying',78,100,84,78,94,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (7,'Squirtle','water',44,43,48,65,57,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (8,'Wartortle','water',59,58,63,80,73,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (9,'Blastoise','water',79,78,83,100,95,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (10,'Caterpie','bug',45,45,30,35,20,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (11,'Metapod','bug',50,30,20,55,25,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (12,'Butterfree','bug,flying',60,70,45,50,58,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (13,'Weedle','bug,poison',40,50,35,30,20,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (14,'Kakuna','bug,poison',45,35,25,50,25,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (15,'Beedril','bug,poison',65,75,90,40,65,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (16,'Pidgey','normal,flying',40,56,45,40,35,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (17,'Pidgeotto','normal,flying',63,71,60,55,50,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (18,'Pidgeot','normal,flying',83,101,80,75,70,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (19,'Rattata','normal',30,72,56,35,30,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (20,'Raticate','normal',55,97,81,60,60,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (21,'Spearow','normal,flying',40,70,60,30,31,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (22,'Fearow','normal,flying',65,100,90,65,61,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (23,'ekans','poison',35,55,60,44,47,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (24,'Arbok','Poison',60,80,95,69,72,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (25,'Pikachu','electric',35,90,55,40,50,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (26,'Raichu','electric',60,110,90,55,85,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (27,'Sandshrew','ground',50,40,75,85,25,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (28,'Sandslash','ground',75,65,100,110,50,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (29,'Nidoran♀','Poison',55,41,47,52,40,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (30,'Nidorina','Poison',70,56,62,67,55,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (31,'Nidoqueen','poison,ground',90,76,92,87,80,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (32,'Nidoran♂','poison',46,50,57,40,40,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (33,'Nidorino','poison',61,65,72,57,55,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (34,'Nidoking','poison,ground',81,85,102,77,80,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (35,'Clefairy','fairy',70,35,45,48,63,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (36,'Clefable','fairy',95,60,70,73,90,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (37,'Vulpix','fire',38,65,41,40,65,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (38,'Ninetailes','fire',73,100,76,75,90,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (39,'Jigglypuff','normal,fairy',115,20,45,20,35,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (40,'Wigglytuff','normal,fairy',140,45,70,45,67,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (41,'Zubat','poison,flying',40,55,45,35,35,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (42,'Golbat','poison,flying',75,90,80,70,70,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (43,'Oddish','grass,poison',45,30,50,55,70,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (44,'Gloom','grass,poison',60,40,65,70,80,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (45,'Vileplume','grass,poison',75,50,80,85,100,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (46,'Paras','bug,grass',35,25,70,55,50,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (47,'parasect','bug,grass',60,30,95,80,70,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (48,'Venonat','bug,poison',60,45,55,50,47,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (49,'Venomoth','bug,poison',70,90,65,60,83,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (50,'Diglett','ground',10,95,55,25,40,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (51,'Dugtrio','ground',35,120,100,50,60,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (52,'Meowth','normal',40,90,45,35,40,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (53,'Persian
','normal',65,115,70,60,65,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (54,'Psyduck','water',50,55,52,48,57,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (55,'Golduck','water',80,85,82,78,87,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (56,'Mankey','fighting',40,70,80,35,40,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (57,'Primeape','fighting',65,95,105,60,65,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (58,'Growlithe','fire',55,60,70,45,60,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (59,'Arcanine','fire',90,95,110,80,90,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (60,'poliwag','water',40,90,80,40,40,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (61,'polywhirl','water',65,90,65,65,50,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (62,'poliwrath','water,fighting',90,70,95,95,80,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (63,'Abra','psychic',25,90,20,15,80,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (64,'Kadabra','psychic',40,105,35,30,90,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (65,'Alakazam','psychic',55,120,50,45,115,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (66,'Machop','fighting',70,35,80,50,35,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (67,'Machoke','fighting',80,45,100,70,55,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (68,'Machamp','fighting',90,55,130,80,75,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (69,'Bellsprout','grass,poison',50,40,75,35,50,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (70,'Weepinbell','grass,poison',65,55,90,50,65,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (71,'Victreebell','grass,poison',80,70,105,65,85,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (72,'Tentacool','water,poison',40,70,40,35,75,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (73,'Tentacruel','water,poison',80,100,70,65,100,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (74,'Geodude','rock,ground',40,20,80,100,30,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (75,'Graveler','rock,ground',55,35,95,115,45,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (76,'Golem','rock,ground',80,45,120,130,60,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (77,'Ponyta','fire',50,90,85,55,65,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (78,'Rapidash','fire',65,105,100,70,80,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (79,'Slowpoke','water,psychic',90,15,65,65,40,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (80,'Slowbro','water,psychic',95,30,75,110,90,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (81,'Magnemite','electric,steel',25,45,35,70,75,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (82,'Magneton','electric,steel',50,70,60,95,120,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (83,'Farfetch''d','normal,flying',52,60,90,55,60,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (84,'Doduo','normal,flying',35,75,85,45,35,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (85,'Dodrio ','normal,flying',60,110,110,70,60,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (86,'Seel','water',65,45,45,55,57,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (87,'Dewgong','water,ice',90,70,70,80,83,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (88,'Grimer','poison',80,25,80,50,45,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (89,'Muk','poison',105,50,105,75,87,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (90,'Shelder','water',30,40,65,100,35,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (91,'Cloyster','water,ice',50,70,95,180,65,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (92,'Gastly','ghost,poison',30,80,35,30,65,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (93,'Haunter','ghost,poison',45,95,50,45,85,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (94,'Gengar','ghost,poison',60,110,65,65,103,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (95,'Onix','rock,ground',35,70,45,160,37,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (96,'Drowzee','psychic',60,42,48,45,83,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (97,'Hypno','psychic',85,67,73,70,90,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (98,'Krabby','water',30,50,105,90,25,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (99,'Kingler','water',55,75,130,115,50,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (100,'Voltorb','electric',40,100,30,50,55,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (101,'Electrode','electric',60,150,50,70,80,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (102,'Exeggcute','grass,psychic',60,40,40,80,52,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (103,'Exeggutor','grass,psychic',95,55,95,85,90,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (104,'Cubone','ground',50,35,50,95,45,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (105,'Marowak','ground',60,45,80,110,65,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (106,'Hitmonlee','fighting',50,87,120,53,77,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (107,'Hitmonchan','fighting',50,76,105,79,77,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (108,'Lickitung','normal',90,30,55,75,67,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (109,'Koffing','poison',40,35,65,95,57,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (110,'Weezing','poison',65,60,90,120,77,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (111,'Rhyhorn','ground,rock',80,25,85,95,30,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (112,'Rhydon','ground,rock',105,40,130,120,45,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (113,'Chansey','normal',250,50,5,5,73,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (114,'Tangela','grass',65,60,55,115,70,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (115,'Kangaskhan','normal',105,90,95,80,60,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (116,'Horsea','water',30,60,40,70,50,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (117,'Seadra','water',55,85,65,95,70,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (118,'Goldeen','water',45,63,67,60,35,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (119,'Seaking','water',80,68,92,65,73,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (120,'Staryu','water',30,85,45,55,63,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (121,'Starmie','water,psychic',60,115,75,85,93,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (122,'Mr. Mime','psychic,fairy',40,90,45,65,110,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (123,'Scyther','bug,flying',70,105,110,80,67,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (124,'Jynx','ice,psychic',65,95,50,35,105,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (125,'Electabuzz','electric',65,105,83,57,90,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (126,'Magmar','fire',65,93,95,57,93,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (127,'Pinsir','bug',65,85,125,100,63,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (128,'Tauros','normal',75,110,100,95,55,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (129,'Magikarp','water',20,80,10,55,17,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (130,'Gyarados','water,flying',95,81,125,79,80,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (131,'Lapras','water,ice',130,60,85,80,90,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (132,'Ditto','normal',48,48,48,48,48,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (133,'Eevee','normal',55,55,55,50,55,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (134,'Vaporeon','water',130,65,65,60,102,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (135,'Jolteon','electric',65,130,65,60,103,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (136,'Flareon','fire',65,65,130,60,103,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (137,'Porygon','normal',65,40,60,70,80,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (138,'Omanyte','rock,water',35,35,40,100,77,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (139,'Omastar','rock,water',70,55,60,125,87,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (140,'Kabuto','rock,water',30,55,80,90,50,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (141,'Kabutops','rock,water',60,80,115,105,67,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (142,'Aerodactyl','rock,flying',80,130,105,65,67,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (143,'Snorlax','normal',160,30,110,65,87,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (144,'Articuno','ice,flying',90,85,85,100,110,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (145,'Zapdos','electric,flying',90,100,90,85,113,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (146,'Moltres','fire,flying',90,90,100,90,105,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (147,'Dratini','dragon',41,50,64,45,50,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (148,'Dragonair','dragon',61,70,84,65,70,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (149,'Dragonite','dragon,flying',91,80,134,95,100,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (150,'Mewtwo','psychic',106,130,110,90,122,0);
INSERT INTO "basepokemon" ("id","Nom","Type","HPMAX","Vitesse","Attaque","Defence","Special","numberofuses") VALUES (151,'Mew','psychic',100,100,100,100,100,0);
CREATE INDEX IF NOT EXISTS "cle_secondaire_sac" ON "personnage" (
	"Sac_idSac"	DESC
);
CREATE INDEX IF NOT EXISTS "Cle_secondaire_notre_equipe" ON "personnage" (
	"Equipe_idEquipe"	DESC
);
CREATE INDEX IF NOT EXISTS "cle_secondaire_attaques" ON "attaquespokemon" (
	"Attaques_idAttaques"	DESC
);
CREATE INDEX IF NOT EXISTS "cle_secondaire_pokemon" ON "attaquespokemon" (
	"appartientpokemon"	DESC
);
CREATE INDEX IF NOT EXISTS "Cle_secondaire_equipe" ON "pokemon" (
	"appartientequipe"	DESC
);
CREATE INDEX IF NOT EXISTS "clesecondaireequipe" ON "pnj" (
	"Equipe_idEquipe"	DESC
);
COMMIT;
