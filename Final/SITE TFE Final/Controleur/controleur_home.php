<?php
session_start();
$_SESSION['logged']=FALSE;
header('location:../Vue/home.php');
?>