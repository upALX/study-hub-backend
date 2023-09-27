
//Use of THIS
const alx = {
    "name": 'alx',
    "age": 14,
    "email": 'alexandreaddres@gmail.com',
    showValues: () => {
        console.log(`name: ${this.name}, age: ${this.age}, email: ${this.email}`)
    }
}

alx.showValues()

