
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
