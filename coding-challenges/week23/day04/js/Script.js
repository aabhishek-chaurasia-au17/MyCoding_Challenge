let loanAmonuts = document.getElementById("loanAmonut");
let interestRates = document.getElementById("interestRate");
let monthtoPay = document.getElementById("MonthtoPay");
let row = document.getElementById("totalrow");

row.addEventListener('click', function(e){
    
    let result = Number(loanAmonuts.value) + (Number(interestRates.value) * Number(monthtoPay.value) / 100);
    
    console.log(result);
    row.innerHTML = Math.floor(result)
})