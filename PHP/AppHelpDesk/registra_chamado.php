<?php
require_once("validador_acesso.php");

$titulo = $_POST['titulo'];
$categoria = $_POST['categoria'];
$descicao = $_POST['descricao'];
$id = $_SESSION['id'];
$texto = "$id#$titulo#$categoria#$descicao". PHP_EOL;
$fp = fopen("arquivo.hd", "a+");
fwrite($fp, $texto);
fclose($fp);
header('Location: home.php');
?>