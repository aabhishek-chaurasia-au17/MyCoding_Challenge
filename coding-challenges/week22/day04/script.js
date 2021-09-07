const locations = document.querySelector('#location');
const text = document.querySelector('#showLocation');
const google = document.querySelector('#goGmap');


function succes(getpositions) {
    console.log('Secces');
    let getloction = 'Latitude is ' + getpositions.coords.latitude + ',' + ' Longitude is ' + getpositions.coords.longitude
    text.innerHTML = getloction;
    google.href = "https://www.google.co.in/maps/@" + getpositions.coords.latitude  + ',' + getpositions.coords.latitude, '15';
}


function error(params) {
    console.log('error');
}


locations.addEventListener('click', function(e) {
    navigator.geolocation.getCurrentPosition( succes, error)
})

