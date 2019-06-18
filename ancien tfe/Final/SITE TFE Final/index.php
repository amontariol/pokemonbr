<?php
session_start();
$logged = FALSE;
$_SESSION['logged']=FALSE;
header ('location:Vue/home.php');
?>