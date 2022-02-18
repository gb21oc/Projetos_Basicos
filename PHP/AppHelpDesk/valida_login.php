<?php
session_start();
$userLogado = false;
$usuario_id = null;
$usuario_perfil_id = null;
$perfis = array(1 => 'Administrativo', 2 => 'Usuario');
$usuarios_app = array(
    array('id' => 1, 'email' => 'adm@teste.com.br', 'senha' => '1', 'perfil_id' => 1),
    array('id' => 2, 'email' => 'user@teste.com.br', 'senha' => '1', 'perfil_id' => 2),
);

$email = $_POST['email'];
$senha = $_POST['senha'];

foreach($usuarios_app as $user){
    if($user['email'] == trim($email) && $user['senha'] == trim($senha)){
        $userLogado = true;
        $usuario_id = $user['id'];
        $usuario_perfil_id = $user['perfil_id'];
    }
}
if($userLogado){
    $_SESSION['autenticado'] = 'SIM';
    $_SESSION['id'] = $usuario_id;
    $_SESSION['perfil_id'] = $usuario_perfil_id;
    header('Location: http://127.0.0.1/home.php');
}else{
    $_SESSION['autenticado'] = 'NAO';
    header('Location: index.php?login=erro');
}
?>