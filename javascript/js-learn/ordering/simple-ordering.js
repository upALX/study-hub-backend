// Create an array of int values and return the min value

const valuesList = [4,5,2,50,12,56]

function ascendingOrder(listValues){
    let minorIndexValue = 0 
    var minorValue = 0

    for(let nowIterator = 0; nowIterator < listValues.length; nowIterator++){
        if (listValues[nowIterator] < listValues[minorIndexValue]){
            minorIndexValue = nowIterator  
            console.log(listValues)
        }
        console.log(minorIndexValue)
    }

    minorValue = listValues[minorIndexValue]

    console.log('Minor: ', minorValue, 'list order: ', listValues)

    return minorValue
}

const minorValue = ascendingOrder(valuesList)

console.log(minorValue)