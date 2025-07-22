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
hfgh
ghghsdd
