<?php 
	session_start ();

	require_once('../Model/model.php');//demander l'appel de model.php


	if ($_SERVER["REQUEST_METHOD"] == "POST") //si methode d'envoi du formulaire est post, faire...
	{
		$nom = test_input($_POST['Lastname']);//attributon des differentes variables
		$prenom = test_input($_POST['Firstname']);
		$login = test_input($_POST['login']);
		$email = test_input($_POST['emailadress']);
		$mdp = test_input($_POST['password']);

		$mon_objet = new User;//creation d'un nouvel objet

		$Tab_users = $mon_objet->recupmembre();//appel de la fonction pour recuperer champs dans db
		if (substr_count( $email, '@' ,0,strlen($email))===1 )//verification de la presence d'un '@'
		{
			if(isset($login) and isset($email))//verification de l'existance de login et d'email
			{
				$exist = False;
				$loginForm = $login;
				$mailForm = $email;
				foreach($Tab_users as $ligne)//parcourir renvoi de fonction
				{
					if ($loginForm === $ligne['Login'] or $mailForm === $ligne['Mail']) //verifier presence de login et de mail dans la db
					{
						$_SESSION['login'] = $loginForm;
						$_SESSION['mail']=$mailForm;
						$exist = True;
					}
				}
			}

			if ($exist == False)//si existance est fausse, faire...
			{
				$MDP_Crypt = md5($mdp);//cryptage du mdp
				$mon_objet->inserermembre($nom,$prenom,$email,$login,$MDP_Crypt);//insertion dans la db
				$loginForm = $login;
				$Tab_users = $mon_objet->recupmembre();

				foreach($Tab_users as $ligne)//parcourir renvoi de fonction
				{
					if ($loginForm === $ligne['Login'] && $MDP_Crypt === $ligne['MDP']) //verifier presence de login et de mdp dans la db
					{

						$_SESSION['login'] = $loginForm;
						$_SESSION['pwd'] = $passwordForm_hache; 
						$flag = True;
						$_SESSION['logged']=TRUE;
					}
				}
				if ($flag == True)//si presence dans la db, aller à...
				{
					header('location:../Vue/home.php');
				}
				else //sinon, aller à...
				{
					$mon_objet = null;
					header('location:../Controleur/controleur_home.php');
				}
			}
			else//sinon, aller à...
			{
				header('location:../Controleur/controleur_home.php');
			}	
		}
		else//sinon, aller à...
		{
			header('location:../Controleur/controleur_home.php');
		}
	}
	else //sinon, aller à...
	{
		header('location:../Controleur/controleur_home.php');
	}