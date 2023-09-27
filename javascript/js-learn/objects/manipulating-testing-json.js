const jsonContent = require("./json-testing.json")

// search a parameter into object by key
function search(list, key, value){
    return list.find((element) => element[key] === value)
}

const finded = search(jsonContent, "nome", "Izaak")

console.log(finded)

// Filter a object to find all person without complement into apartament address

function findAllWithoutComplement(list){
    
    return list.filter((item) => {
        return item.endereco.apartamento && !item.endereco.hasOwnProperty("complemento") 
    })
}

const filtred = findAllWithoutComplement(jsonContent)

console.log(filtred)

//order a object by parameter
