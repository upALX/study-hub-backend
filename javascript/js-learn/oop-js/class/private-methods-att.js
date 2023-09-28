class User {
    #name
    #age
    #email
    constructor(name, age, email){
        this.#name = name
        this.#age = age
        this.#email = email
    }

    get lol(){
        return this.#name
    }

    get getAge(){
        return this.#age
    }

    get getMail(){
        return this.#email
    }

    set setMail(newMail){
        this.#email = newMail
        
        return this.#email
    }

    showValue(){
        console.log(`Values: ${this.#createObjectUser()} `)
    }

    #createObjectUser(){
        return ({
            name: this.#name,
            age: this.#age,
            email: this.#email
        })
    }
}

const he = new User('Alexandre', 23, 'alexandreaddress@gmail.com')

console.log(he.showValue())

// Getting private att with no sucess
//console.log(he.this.#name)

//Getting private method with no sucess
//he.#createObjectUser

// Acess by accessors methods
console.log(he.lol)
console.log(he.getAge)

//Use methods get set

console.log(he.getMail)

console.log(he.setMail = 'alx@alx.com')

console.log(he.showValue())

console.log(he.getMail)