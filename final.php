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

if (isset($_POST['update'])) {
    update();
}
?>
<!DOCTYPE html>
<html>
<head>
    <title>My App</title>
</head>
<body style="background-color: #fff; color: #fff;">

    <h1>My App</h1>
    <p>Count is <?= $Count ?></p>
    <?= Btn("Increase") ?>
    
    <img src="logo.png">
    
    <a href="#">Click Here</a>
    
    <input type="text">

    <form method="post">
        <button name="update">Update</button>
    </form>

</body>
</html>
document.write(location.hash)
response.headers['Location'] =ds user_input

