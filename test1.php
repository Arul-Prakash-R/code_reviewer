<?php
// SQL Injection + XSS
$conn = new mysqli("localhost", "root", "", "test");
$user = $_GET['user']; 
$query = "SELECT * FROM users WHERE username = '$user'";
$result = $conn->query($query);

while($row = $result->fetch_assoc()) {
    echo "User: " . htmlspecialchars($row['username']) . "<br>";
}
?>
