<?php
// csrf_vulnerable.php

session_start();

// Simulate a user login
if (!isset($_SESSION['balance'])) {
    $_SESSION['balance'] = 1000;
}

// Transfer money (vulnerable to CSRF)
if (isset($_POST['amount']) && isset($_POST['to'])) {
    $amount = intval($_POST['amount']);
    $to = $_POST['to'];

    $_SESSION['balance'] -= $amount;
    echo "Transferred $$amount to $to. Current balance: $" . $_SESSION['balance'];
    exit;
}
?>

<h2>Transfer Money</h2>
<form method="POST" action="csrf_vulnerable.php">
    To: <input type="text" name="to"><br>
    Amount: <input type="number" name="amount"><br>
    <input type="submit" value="Send Money">
</form>
