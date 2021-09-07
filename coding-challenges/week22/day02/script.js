
let push = document.getElementById('Push');
let pop = document.getElementById('Pop');
let res = document.getElementById('result');
var arr = []


push.addEventListener('click', function () {
    let input = document.getElementById('Input').value;
    arr.push(input)
    res.innerText = arr
    console.log(arr);
    res.style.color = 'white'
    
})

pop.addEventListener("click", function(){
    arr.pop()
    res.innerText=arr
})