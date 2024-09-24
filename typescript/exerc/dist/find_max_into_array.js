function findMax(arr) {
    var max_value = 0;
    for (var _i = 0, arr_1 = arr; _i < arr_1.length; _i++) {
        var value = arr_1[_i];
        if (value > max_value) {
            max_value = value;
        }
        console.log("Max value: ".concat(max_value));
    }
    return max_value;
}
var arr = [1, 2, 5, 6, 78, 45, 32];
var result = findMax(arr);
console.log(result);
