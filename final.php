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

<

import React, { useState, useEffect } from 'react'; // Unused import: useEffect
import axios from 'axios'; // Unused import
import moment from 'moment'; // Dead import

// commented out legacy code
// function fetchOldData() { return null; }

const Btn = (props) => { // inconsistent naming (Btn vs Button)
let click = () => {alert("Clicked")} // bad formatting, spacing, no semicolon

    return <button onClick={click}>{props.text}</button> // Missing alt text if it were image-based
}

const App = () => {
const [Count, setCount] = useState(0); // inconsistent naming (Count)

const users = [
{name: "Arul", age: 22},
{name: "Bala", age: 25},
{name: "Chitra", age: 20},
{name: "Deepa", age: 23}
];

const oldUsers = [] // unused variable

const calculate = () => {
  for (let i = 0; i < users.length; i++) {
    console.log(users[i].name)
  }
}

// unnecessary rerender on every click
const update = () => {
  setCount(Count + 1)
  calculate()
}

return (
<div style={{ backgroundColor: '#fff', color: '#fff' }}> {/* poor contrast */}
  <h1>My App</h1>
  <p>Count is {Count}</p>
  <Btn text="Increase" />
  <img src="logo.png" /> {/* Missing alt text */}
  <a href="#">Click Here</a> {/* Inaccessible link */}
  <input type="text" /> {/* No label */}
  <button onClick={update}>Update</button>
</div>
)
}

// test coverage for this component is missing
// linting errors are ignored
// test("renders correctly", () => {}) <-- commented-out test

export default App;

