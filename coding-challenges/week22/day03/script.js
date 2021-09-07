
let push = document.getElementById('add');
let pop = document.getElementById('remove');
let res = document.getElementById('result');
var arr = []


push.addEventListener('click', function() {
    let input = document.getElementById('inputtext').value;
    arr.push(input)
    res.innerText = arr
    console.log(arr);

})

pop.addEventListener("click", function(){
    arr.shift()
    res.innerText=arr
})