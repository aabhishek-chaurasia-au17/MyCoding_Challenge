var loan_input = document.getElementById("loan")
var interest_input = document.getElementById("interest")
var months_input = document.getElementById("months")
var output = document.getElementById("output")



loan_input.addEventListener("input",function(){
    console.log((loan_input.value*(interest_input.value/100)+Number(loan_input.value))/months_input.value)
    output.innerText = `Monthly Payment = ${(loan_input.value*(interest_input.value/100)+Number(loan_input.value))/months_input.value}`
})

interest_input.addEventListener("input",function(){
    console.log((loan_input.value*(interest_input.value/100)+Number(loan_input.value))/months_input.value)
    output.innerText = `Monthly Payment = ${(loan_input.value*(interest_input.value/100)+Number(loan_input.value))/months_input.value}`
})

months_input.addEventListener("input",function(){
    console.log((loan_input.value*(interest_input.value/100)+Number(loan_input.value))/months_input.value)
    output.innerText = `Monthly Payment = ${(loan_input.value*(interest_input.value/100)+Number(loan_input.value))/months_input.value}`
})