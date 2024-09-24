async function findMax(arr: Array<number>): Promise<number> {
    var max_value = 0

    const urlDataStock: string = 'https://something.com'   

    const data_stock = fetch(urlDataStock).then(
        response => {
            if (!response.ok){
                throw new Error('Some error') 
            }
        } 
        
    )

    for (let value of arr){
        var x = 0
        if (value > max_value){
            max_value = value 
        }
        console.log(`Max value: ${max_value}`)
    } 

    return max_value
}

const arr: Array<number> = [1,2,5,6,78,45,32]

const result = findMax(arr)

console.log(result)