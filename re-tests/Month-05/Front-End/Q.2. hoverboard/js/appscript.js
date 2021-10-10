const mainDiv = document.querySelector('#main-div');
const colorsArr = ['#db4839', '#9043b0', '#3497d9', '#e07c24', '#2dcf72'];
const tiles = 400;


function colorGenerator() {
    return colorsArr[Math.trunc(Math.random() * colorsArr.length)]
}

function set_color(element) {
   const color = colorGenerator()
   
   element.style.boxShadow = `0 0 3px ${color}, 0 0 9px ${color}`
   element.style.background = color
}

function remove_color(element) {
   element.style.background = '#1d1d1d'
   element.style.boxShadow = '0 0 3px #000'
}


for(let i = 0; i < tiles; i++) {
    const boxs = document.createElement('div')
    boxs.classList.add('tile-box')

    boxs.addEventListener('mouseover', () => set_color(boxs))

    boxs.addEventListener('mouseout', () => remove_color(boxs))

    mainDiv.appendChild(boxs)
}


