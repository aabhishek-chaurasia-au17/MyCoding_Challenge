let totalbill = document.querySelector('.bill-amount');
let tipInpercent = document.querySelector('.tip-percentage');
let amountOfTip = document.querySelector('.tipAmount');
let total = document.querySelector('.total');
let btn = document.querySelector('.calcBtn');

btn.addEventListener('click', function(){
    totalbill = Number(totalbill.value);
    tipInpercent = Number(tipInpercent.value);

    if (isNaN(totalbill) || totalbill <= 0 || totalbill === null){
        alert('Please enter a valid Bill Amount')
    }
    else if (isNaN(tipInpercent) || tipInpercent <= 0 || tipInpercent === null){
        alert('Please enter a valid Tip Percentage')
    }
    else {
        let totalTip =  tipInpercent/100*totalbill;
        amountOfTip.value = '$' + totalTip;

        let allTotal = totalbill + totalTip;
        total.value = '$' + allTotal;
    }
})