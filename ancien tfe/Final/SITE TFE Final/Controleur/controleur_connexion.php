<?php 
	session_start();
	require_once('../Model/model.php');//demander l'appel de model.php
	$login = test_input($_POST['login']);//recuperation de login	
	$mdp = test_input($_POST['password']);//recuperation de mdp

	if ($_SERVER["REQUEST_METHOD"] == "POST") //si l'envoie du formulaire est avec la methode post
	{
		$mon_objet = new User;//instanciation d'un nouvel objet

		$Tab_users = $mon_objet->recupmembre();//recuperation des membres

		if(isset($login) && isset($mdp))//verification si variable n'est pas nulle
		{
			$loginForm = $login;
			$passwordForm_hache = md5($mdp);//cryptage du mdp

			foreach($Tab_users as $ligne)//parcourir le renvoi de la db
			{
				if ($loginForm === $ligne['Login'] && $passwordForm_hache === $ligne['MDP']) //test si login et mdp correspondent 
				{

					$_SESSION['login'] = $loginForm;
					$_SESSION['pwd'] = $passwordForm_hache; 
					$flag = True;
					$_SESSION['logged']=TRUE;
				}
			}
			if ($flag == True)//si login et mdp correspondent, aller à...
			{
				header('location:../Vue/home.php');
			}
			else//sinon, aller à...
			{
				$mon_objet = null;
				header('location:../Controleur/controleur_home');
			}
			
		}
		else//sinon, aller à...
		{
			$mon_objet = null;
			header('location:../Controleur/controleur_home');
		}

		$mon_objet = null;
	}
	else//sinon, aller à...
	{
		header('location:../Controleur/controleur_home');
	}

	$mon_objet = null; //annulation de l'objet
