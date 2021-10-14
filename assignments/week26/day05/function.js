var add = document.getElementById('add')
add.classList.add("btn-success")

var remove = document.getElementById('remove')
remove.classList.add("btn-danger")

var App = (function() {
    var number = document.getElementById("number")
    var invalid = document.getElementById("invalid")
    var stack = document.getElementById("stack")

    var array = []

    function push(){
        var input = number.value
        switch (input) {
            case "":
                stack.innerHTML = ""
                invalid.innerHTML = "Please enter something in the input field"
                break;
            
            default:
                var check = parseInt(input) == input
                switch (check) {
                    case true:
                        array.push(input)
                        display()
                        break

                    case false:
                        stack.innerHTML = ""
                        invalid.innerHTML = "Please enter a valid input"
                }
        }
    
    }

    function display() {
        var position = array.length - 1
        var result = array.map(function(item, index) {
            if (index == 0) {
                return `<span style="color:red">` + item + `</span>`
            }
            else if(index == position) {
                return `<span style="color:darkgreen">` + item + `</span>`
            }
            else{
                return `<span>`+ item + `</span>`
            }
        } )
        stack.innerHTML = result

        invalid.innerHTML = ""
        document.getElementById("number").value = ""
    }

    function Pop() {
        var length = array.length

        switch (length) {
            case 0:
                stack.innerHTML = ""
                invalid.innerHTML = "Queue is already empty"
                break
            default:
                array.shift()
                display()
            
        }
    }

    add.addEventListener("click", push)
    remove.addEventListener('click', Pop)

})()