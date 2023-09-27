const util = require('util')

//Use of THIS
const alx = {
    "name": 'alx',
    "age": 14,
    "email": 'alexandreaddres@gmail.com',
    showValues: function() {
        console.log(`name: ${this.name}, age: ${this.age}, email: ${this.email}`)
    }
}

alx.showValues()

//Creating object with schema of other proto - Heritage
const alxJunior = {
    "name": 'Alexandre',
    "age": 23,
    "email": 'alexandreaddres@gmail.com',
    show: function() {
        console.log('Hello world!')
    }
}

Object.setPrototypeOf(alxJunior, alx)
alxJunior.show()
alxJunior.showValues()

//Creatig objects with javascript  = new vs create

function Person(name, age, email){
    this.name = name
    this.age = age
    this.email = email
}

const a = new Person('Alexandre', 23, 'a@a')

console.log(a)

//Creating object with literal object

const l = {name: 'ALX', age: 17}

const x = Object.create(l)

x.name = 'OLa'
x.age = 18

console.log(l)
console.log(x)