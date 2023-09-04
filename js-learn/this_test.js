//Practice for each with arrow function
const names = ['a', 'b', 'c']

const values = names.forEach((value) => {
    console.log('This is for each, no mapping 3')
})


//Practice mapping function
const mapping = names.map((index, value) => {
    let values = ['b', 'c', 'd']

    value += values[index] 

    console.log(values[index])
})

// reduce practice function
const grades = [43, 50, 65, 12]

const nums = grades.reduce(
    (acc, note) => acc += note, 0 
)

console.log(nums)

//Using and practice spread operator
const valueCopy = [1,2,3,4]

const copied = [...valueCopy]

console.log('COPY: ', typeof(copied))
console.log('COPY: ', copied[3])

//remove duplicates of array

const namesValue = ['alx', 'alx', 'breno', 'jorel']

const dontRepeatNames = [...new Set(namesValue)]

console.log(dontRepeatNames)