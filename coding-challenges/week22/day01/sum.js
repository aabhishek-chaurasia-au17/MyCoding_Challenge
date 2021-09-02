
const numone = document.getElementById('Num1');
const numtwo = document.getElementById('Num2');
const showElement = document.getElementById('show');
const total = document.getElementById('Submit');


total.addEventListener('click', function(e){

    
    let sum = Number(numone)  + Number(numtwo);
    showElement.innerText = sum
    console.log(sum);
})
