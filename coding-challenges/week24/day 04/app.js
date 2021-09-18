async function currency() {
    try {
        const response = await fetch("http://api.exchangeratesapi.io/v1/latest?access_key=8dc037f1a62d2a67444273ae72c7f0c7")
        const data = await response.json()
        let array = Object.keys(data.rates)
        let input1 = document.getElementById("input1")
        let input2 = document.getElementById("input2")
        let value1 = document.getElementById("value1")
        let value2 = document.getElementById("value2")
        let swap = document.getElementById("swap")
        swap.addEventListener("click", change)
        value1.addEventListener("keyup", findanswer)
        value1.addEventListener("click", findanswer)

        let allvalues = Object.values(data.rates)
        console.log(data.rates)
        for (const val of array) {
            var option = document.createElement("option");
            option.value = val;
            option.text = val;
            input1.appendChild(option)
        }
        for (const val of array) {
            var option = document.createElement("option");
            option.value = val;
            option.text = val;
            input2.appendChild(option)

        }
        function findanswer() {
            if (value1.value != "") {
                let unit = allvalues[array.indexOf(input2.value)] /  allvalues[array.indexOf(input1.value)]
                document.getElementById("answer").innerText = `1 ${input1.value} = ${unit} ${input2.value}`
                let finalanswer = value1.value * unit
                value2.value = finalanswer
            }
            else {
                value2.value = ""
            }
        }
        
        function change() {
            let input1 = document.getElementById("input1")
            let input2 = document.getElementById("input2")
            let one = input1.value + "1"
            input1.value = input2.value
            input2.value = one.slice(0, -1)
            findanswer()
        
        }
    }catch(error) {
        document.getElementById("answer").innerText = "Sorry the API could not be loaded please check your internet connection"
    }

}
currency()
