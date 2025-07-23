<?php
$username = "admin";
$password = "admin123";

session_start();
if (isset($_GET['session_id'])) {
    session_id($_GET['session_id']);
}

if (isset($_POST['login'])) {
    if ($_POST['user'] === $username && $_POST['pass'] === $password) {
        $_SESSION['auth'] = true;
        echo "Logged in as admin<br>";
    } else {
        echo "Invalid credentials";
    }
}

if (isset($_GET['id'])) {
    $conn = new mysqli("localhost", "root", "", "test");
    $id = $_GET['id'];
    $sql = "SELECT * FROM users WHERE id = '$id'";
    $result = $conn->query($sql);
    while($row = $result->fetch_assoc()) {
        echo "User: " . $row['username'] . "<br>";
    }
}

if (isset($_GET['msg'])) {
    echo "Message: " . $_GET['msg'];
}

if (isset($_GET['ping'])) {
    $output = shell_exec("ping -c 1 " . $_GET['ping']);
    echo "<pre>$output</pre>";
}

if (isset($_FILES['file'])) {
    move_uploaded_file($_FILES['file']['tmp_name'], "uploads/" . $_FILES['file']['name']);
    echo "File uploaded!";
}

if (isset($_GET['read'])) {
    $file = $_GET['read'];
    echo "<pre>" . file_get_contents($file) . "</pre>";
}

if (isset($_POST['delete_file'])) {
    unlink("uploads/" . $_POST['delete_file']);
    echo "File deleted!";
}

if (isset($_GET['data'])) {
    $object = unserialize($_GET['data']);
}

if (isset($_GET['go'])) {
    header("Location: " . $_GET['go']);
    exit;
}

if (isset($_GET['page'])) {
    include($_GET['page']);
}
?>

<?php

include 'unused.php';
require 'axios.php';

$Count = 0;

$users = [
    ["name" => "Arul", "age" => 22],
    ["name" => "Bala", "age" => 25],
    ["name" => "Chitra", "age" => 20],
    ["name" => "Deepa", "age" => 23]
];

$oldUsers = [];

function Btn($text) {
    $click = "onclick=\"alert('Clicked')\"";
    return "<button $click>$text</button>";
}

function calculate() {
    global $users;
    for ($i = 0; $i < count($users); $i++) {
        echo $users[$i]['name'] . "<br>";
    }
}

function update() {
    global $Count;
    $Count = $Count + 1;
    calculate();
}

?>
<!DOCTYPE html>
<html>
<head>
    <title>My App</title>
</head>
<body style="background-color: #fff; color: #fff;">

    <h1>My App</h1>

