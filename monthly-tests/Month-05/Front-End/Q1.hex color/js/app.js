
const body = document.querySelector('body');
const inputhex = document.querySelector('#Inputhex');
const btn = document.querySelector('#submit');
const feedback = document.querySelector('.feedback');

btn.addEventListener('click', function() {
    if(inputhex.value === ''){
        feedback.classList.add('show')
        setTimeout(function(){
        feedback.classList.remove('show')
        }, 2000)
    }else{
    body.style.backgroundColor =  inputhex.value;
    }
})