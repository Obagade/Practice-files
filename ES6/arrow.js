// writing this in es5
function circleArea1(r){
    var PI = 3.14;
    return PI * r * r;
}

// to write using arrow function

let circleArea2 = (r) => {
   const PI = 3.14;
   return PI * r * r;
}

//you can alternative write it this way 

let circleArea3 = r => 3.14 * r * r;

console.log(circleArea1(2));
console.log(circleArea2(2));
console.log(circleArea3(2));