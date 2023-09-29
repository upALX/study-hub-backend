import User from '../class/private-methods-att.js'

class Person extends User{
    #gender
    constructor(name, age, email, gender){
        super(name, age, email)
        this.#gender = gender
    }

}

const personOne = new Person('ALX', 23, 'ALX@ALX.COM', 'MEN')

console.log(personOne.getInformation())