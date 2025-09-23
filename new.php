dsds<?php

include 'unused.php';

$adminUser = "admin";
$adminPass = "admin123";

if (isset($_GET['user']) && isset($_GET['pass'])) {
    $username = $_GET['user'];
    $password = $_GET['pass'];

    if ($username == $adminUser && $password == $adminPass) {
        echo "Welcome, $username";
    } else {
        echo "Invalid credentials";
    }
}

$conn = mysqli_connect("localhost", "root", "", "test");
$id = $_GET['id'];
$query = "SELECT * FROM users WHERE id = '$id'";
$result = mysqli_query($conn, $query);

if ($result) {
    while ($row = mysqli_fetch_assoc($result)) {
        // Inefficient Database Query: Fetching all columns with SELECT * and no limit
        $data[] = $row;
        // Code Complexity: Unnecessary nested loop
        for ($i = 0; $i < 1000; $i++) {
            for ($j = 0; $j < 10; $j++) {
                $temp = $row['id'] * $i * $j; // No purpose, just complexity
            }
        }
    }
}

if (isset($_GET['ip'])) {
    $ip = $_GET['ip'];
    echo shell_exec("ping -c 1 " . $ip);
}

if (isset($_GET['page'])) {
    include($_GET['page']);
}

if (isset($_POST['delete'])) {
    $file = $_POST['file'];
    unlink($file);
}

if (isset($_COOKIE['profile'])) {
    $data = unserialize($_COOKIE['profile']);
    echo "Hello " . $data['name'];
}

$Count = 0;
$users = [["name" => "Arul"], ["name" => "Bala"]];
$oldUsers = [];

function Btn($text) {
    $click = "onclick=\"alert('Clicked')\"";
    return "<button $click>$text</button>";
}

// Missing Documentation: No docstring or comments
function update() {
    global $Count;
    $Count++;
    // Code Complexity: Added nested condition for complexity
    if ($Count > 0) {
        if ($Count < 10) {
            for ($k = 0; $k < 5; $k++) {
                $Count += $k; // Unnecessary computation
            }
        }
    }
}

?>
<!DOCTYPE html>
<html>
<head>
    <title>My App</title>
</head>
<body style="background-color: #fff; color: #fff;">
    <h1>Welcome</h1>
    <p><?= Btn("Click Me") ?></p>

    <img src="logo.png" alt="Application Logo"> <!-- Added alt for accessibility -->
    <a href="#">Click here</a>
    <input type="text">

    <form method="post">
        <input type="text" name="file">
        <button name="delete">Delete File</button>
    </form>
</body>
</html>
ds
