<?php 
session_start();
if(!(isset($_SESSION['autenticado'])) or $_SESSION['autenticado']!= "SIM"){
  header('Location: index.php?login=erro');
}
?>