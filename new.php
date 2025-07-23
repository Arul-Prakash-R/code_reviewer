<?php

include 'unused.php'; // Unused include

// Hardcoded credentials
$adminUser = "admin";
$adminPass = "admin123";

// User login (vulnerable to XSS, no validation, uses GET method)
if (isset($_GET['user']) && isset($_GET['pass'])) {
    $username = $_GET['user'];
    $password = $_GET['pass'];

    if ($username == $adminUser && $password == $adminPass) {
        echo "Welcome, $username"; // XSS vulnerability
    } else {
        echo "Invalid credentials";
    }
}

// SQL Injection vulnerability
$conn = mysqli_connect("localhost", "root", "", "test");
$id = $_GET['id']; // No sanitization
$query = "SELECT * FROM users WHERE id = '$id'"; // Vulnerable
$result = mysqli_query($conn, $query);

// Command injection
if (isset($_GET['ip'])) {
    $ip = $_GET['ip'];
    echo shell_exec("ping -c 1 " . $ip); // Dangerous: unsanitized input
}

// File inclusion vulnerability
if (isset($_GET['page'])) {
    include($_GET['page']); // Path traversal / LFI possible
}

// CSRF: dangerous action with no CSRF token
if (isset($_POST['delete'])) {
    $file = $_POST['file'];
    unlink($file); // Deletes file without auth or CSRF protection
}

// Insecure deserialization
if (isset($_COOKIE['profile'])) {
    $data = unserialize($_COOKIE['profile']); // Dangerous input from user
    echo "Hello " . $data['name'];
}

// Broken authentication: no sessions
// Race condition not simulated, but would occur in concurrent calls

// Code Quality Issues
$Count = 0; // Inconsistent variable casing
$users = [["name" => "Arul"], ["name" => "Bala"]];
$oldUsers = []; // Unused
function Btn($text) {
    $click = "onclick=\"alert('Clicked')\""; // Inline JS
    return "<button $click>$text</button>";
}
function update() {
    global $Count;
    $Count++; // Bad state handling
}
?>
<!DOCTYPE html>
<html>
<head>
    <title>My App</title>
</head>
<body style="background-color: #fff; color: #fff;"> <!-- Poor contrast -->

<h1>Welcome</h1>
<p><?= Btn("Click Me") ?></p>

<img src="logo.png"> <!-- Missing alt -->
<a href="#">Click here</a> <!-- Inaccessible link -->
<input type="text"> <!-- No label -->

<form method="post">
    <input type="text" name="file">
    <button name="delete">Delete File</button>
</form>

</body>
</html>
ggg
jghhg
khhggh
