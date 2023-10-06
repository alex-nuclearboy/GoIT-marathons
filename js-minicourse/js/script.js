"use strict";

let a = 5;
let b = 51013;

console.log("a = ", a);
console.log("b = ", b);
console.log("result = ", a * b + b);
console.log("JavaScript is awesome".length);
console.log("JavaScript is awesome".toUpperCase());

let username;
console.log(typeof username); // "undefined"

let inputValue = null;
console.log(typeof inputValue); // "object"

const quantity = 17;
console.log(typeof quantity); // "number"

const message = "JavaScript is awesome!";
console.log(typeof message); // "string"

const isSidebarOpen = false;
console.log(typeof isSidebarOpen); // "boolean"

const isComing = confirm("Please confirm hotel reservation");
console.log(isComing);

const hotelName = prompt("Please enter desired hotel name");
console.log(hotelName);

console.log(Number.parseInt("5px")); // 5
console.log(Number.parseInt("12qwe74")); // 12
console.log(Number.parseInt("12.46qwe79")); // 12
console.log(Number.parseInt("qweqwe")); // NaN

console.log(Number.parseFloat("5px")); // 5
console.log(Number.parseFloat("12qwe74")); // 12
console.log(Number.parseFloat("12.46qwe79")); // 12.46
console.log(Number.parseFloat("qweqwe")); // NaN

const guestName = "Манго";
const roomNumber = 207;
const greeting = `Welcome ${guestName}, your room number is ${roomNumber}!`;
console.log(greeting); // "Welcome Mango, your room number is 207!"

let counter = 0;

let clientCounter = 18;
const maxClients = 25;

while (clientCounter <= maxClients) {
  console.log(clientCounter);
  clientCounter += 1;
}

let password = "";

do {
  password = prompt("Введіть пароль довший 4-х символів", "");
} while (password.length < 5);

console.log("Ввели пароль: ", password);

const max = 10;
for (let i = 0; i < max; i += 1) {
  console.log(`${max} % ${i} = `, max % i);
}

const number = 10;

for (let i = 0; i < number; i += 1) {
  if (i % 2 !== 0) {
    continue;
  }

  console.log("Парне i: ", i); // 0, 2, 4, 6, 8
}