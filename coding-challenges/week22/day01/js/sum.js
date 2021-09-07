const submit = document.getElementById('submit');


submit.addEventListener('click',function() {
    let firstnum = document.getElementById('num1').value;
    let twonum = document.getElementById('num2').value;
    const shownum = document.getElementById('show');
    const sum = Number(firstnum) + Number(twonum);
    
    shownum.innerText = sum;
    console.log(sum);
    
})

