<?php 	
	require('data.php');

	function test_input($donnees) //fonction permettant de blinder les données encodées par l'utilisateur
	{
	  $donnees = trim($donnees);
	  $donnees = stripslashes($donnees);
	  $donnees = htmlspecialchars($donnees);
	  return $donnees;
	}



	class User //Classe permettant d'instancier des objets permettant l'interaction avec la db
	{
		private $_bdd;
		private $_reponse;

		function __construct()//Metchode constructrice de la classe permettant de contruire et d'initialiser les attributs
		{
			try //si possible, faire...
			{
				
				$this->_bdd = new PDO('mysql:host=' . HOSTNAME . ';dbname=' . DBNAME . ';charset=utf8', USERNAME, PASSWORD);//tentative de connexion a la db
			}
			catch (Exception $e)//si une exception est trouvée, faire...
			{
				
				die("Can't Connect ".$e->getMessage());
			}
		}
		
		function __destruct()  //methode destructrice de la classe 
		{
			$this->_bdd = null;
			$this->_reponse = null;
		}
		
		function recupmembre() //methode permettant de récupérer un certain champ de la db
		{
			$mydb = $this->_bdd; //appel de la db
			$my_query1 = "SELECT * FROM joueur";//creation de la requete
			$resultats1 = $mydb->query($my_query1);//execution de la requete

			return $resultats1;//renvoi des resultats
		}
		function recupmembre2() //methode permettant de récupérer un certain champ de la db
		{
			$mydb = $this->_bdd;//appel de la db
			$my_query1 = "SELECT * FROM joueur WHERE joueur.nbwins>0";//creation de la requete
			$resultats1 = $mydb->query($my_query1);//execution de la requete

			return $resultats1;//renvoi des resultats
		}
		function recuppokemon() //methode permettant de récupérer un certain champ de la db
		{
			$mydb = $this->_bdd;//appel de la db
			$my_query1 = "SELECT * FROM basepokemon WHERE basepokemon.numberofuses>0";//creation de la requete
			$resultats1 = $mydb->query($my_query1);//execution de la requete

			return $resultats1;//renvoi des resultats
		}
		function inserermembre($nameForm,$firstnameForm,$emailForm,$pseudoForm,$passwordForm) //methode permettant d'inserer un membre à la db
		{
			$mydb = $this->_bdd;//appel de la db
			$mydb->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);//rapport d'erreurs avec une methode "throw"
			try {//si possible, faire...
				$mydb->beginTransaction();//commencer l'interaction avec la db
				$mydb->exec("INSERT INTO Joueur(Nom, Prenom, Mail, Login, MDP) 
							VALUES ('" . $nameForm . "','" . $firstnameForm . "','" . $emailForm . "','" . $pseudoForm . "','" . $passwordForm . "')"
							);//execution de la requete
				$mydb->commit();//enregistrement de la requete

			}
			catch(Exception $e)//si exception, faire...
			{
				$mydb->rollBack();//anuler requete
			}
		}

	}

?>