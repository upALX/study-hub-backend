//create a object with some items 
const alx =  {
    name: "Alexandre",
    age: 23,
    gender: 'male',
    locationNumber: '77777-777' 
}

// create a object with same properties of the object created before.
const alxClone = Object.create(alx)

alxClone.name = 'ALX CLONE'
alxClone.locationNumber = '66666-666'
alxClone.age = 23
alxClone.gender = 'Male'

console.log(alxClone)

// pass over all items of object and show these

Object.keys(alxClone).forEach(keys => {
    console.log(`${keys}: ${alxClone[keys]}`)
});
