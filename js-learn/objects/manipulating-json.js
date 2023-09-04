const json = require("./json-test.json")

console.log(json)

const stringJson = JSON.stringify(json)

console.log(typeof(stringJson))

const jsonObject = JSON.parse(stringJson)

console.log(typeof(jsonObject))