
// var pushbtn = document.getElementById("Push");
// var ans = document.getElementById("result");
// var popbtn = document.getElementById("Pop");
// var arr = []
// pushbtn.addEventListener("click", function(){
//     var input = document.getElementById("enter").value;
//     arr.push(input)
//     ans.innerText=arr
//     console.log(arr)
// })
// popbtn.addEventListener("click", function(){
//     arr.pop()
//     ans.innerText=arr
// })


let push = document.getElementById('Push');
let pop = document.getElementById('Pop');
let res = document.getElementById('result');
var arr = []


push.addEventListener('click', function () {
    let input = document.getElementById('Input').value;
    arr.push(input)
    res.innerText = arr
    console.log(arr);
})

pop.addEventListener("click", function(){
    arr.pop()
    res.innerText=arr
})