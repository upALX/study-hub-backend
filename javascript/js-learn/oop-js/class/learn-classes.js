
//Create class
class User {
    constructor(name, age, email){
        this.name = name
        this.age = age 
        this.email = email
    }

    getUserInformation(){
        const objectInfos = {
            name: this.name,
            age: this.age,
            email: this.email
        }
        return objectInfos
    }
}

const alx = new User('Alexandre', 23, 'alexandreaddres@gmail.com')

console.log(alx)
console.log(alx.getUserInformation())

// Use heritage class in JS

class Person extends User{
    constructor(name, age, email, address){
        super(name, age, email)
        this.address = address
    }

    getPersonInformation(){
        console.log(this.name, this.age, this.address)
    }
}

const newPerson = new Person('ALX', 19, 'ALX@ALX.COM', {street: 'Firmina'})

console.log(newPerson.getPersonInformation())