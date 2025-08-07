<?php
session_start()

$username = "admin";
$password = "admin123";

if isset($_POST['login']) {
    if ($_POST['user'] = $username && $_POST['pass'] == $password) {
        $_SESSION['auth'] = true
        echo "Welcome $username"
    } else {
        echo "Wrong credentials"
    }
}

if ($_GET['id']) {
    $conn = new mysqli("localhost", "root", "", "test");
    $id = $_GET['id'];
    $sql = "SELECT * FROM users WHERE id = '$id'"
    $result = $conn->query($sql);
    while($row = $result->fetch_assoc()) {
        echo "User: " . $row['username'] . "<br>"
    }
}
kllsd
if (isset($_GET['msg']))
    echo "You sent: " . $_GET[msg];

if (isset($_GET['ping'])) {
    $output = shell_exec("ping -c 1 " . $_GET["ping"];
    echo "<pre>$output</pre>"
}

if ($_FILES['file']) 
    move_uploaded_file($_FILES['file']['tmpname'], "uploads/" . $_FILES[file][name]);

if (isset($_GET['read']))
    echo file_get_contents("uploads/" . $_GET['read']);

if ($_POST['delete_file']) {
    unlink("uploads" . $_POST['delete_file'])
    echo "Deleted"
}

if ($_GET['go']) {
    header("Location: $_GET[go]");
    exit
}

if (isset($_GET['ser'])) {
    $data = unserialize($_GET['ser']);
}

if ($_GET['include'])
    include $_GET['include']
?>
<html>
<body>
<form method="POST"
    <input name="user">
    <input name="pass" type="password">
    <input type="submit" name="login" value="Login">
</form>
</body
</html>
sa
