//Create an simple object
const alx = {
    "name": 'Alexandre',
    "age": 23,
    "balance": 0,
    "address": [
        {
            "street": 'this',
            "location-number": '23435456',
            "state": 'RS',
            "city": "Porto Alegre"
        }
    ],
    "to-delete": 'delete-me'
}

console.log(alx)

//Delete an argument of object
delete alx["to-delete"]

console.log(alx)

//Change a item of object
alx.age = 22

console.log(alx)

// Insert two items (address rua, cidade, estado) list into the object
alx.address.push(
    {
        "street": 'lol',
        "location-number": '07',
        "state": 'SP',
        "city": 'Alvorada'
    }
)

console.log(alx)

// Filter into the main objects, all items into the address with the city is Porto Alegre
const isPoa = alx.address.filter(
    (object) =>  object.city == "Porto Alegre"
)

console.log(isPoa)

// Insert a function into object that feature has payment function.
const alxx = {
    name: 'Alexandre',
    age: 23,
    balance: 400,
    address: [
        {
            "street": 'this',
            "location-number": '23435456',
            "state": 'RS',
            "city": "Porto Alegre"
        }
    ],
    paymentValidate: function (value) {
        console.log(this.balance)

        if (value > this.balance) {
            console.log('Insuficient balance')
        }else{
            this.balance -= value

            console.log(`The new balance is ${this.balance}`) 
        }
    } 
}
console.log(typeof(alxx.balance))

alxx.paymentValidate(300)
