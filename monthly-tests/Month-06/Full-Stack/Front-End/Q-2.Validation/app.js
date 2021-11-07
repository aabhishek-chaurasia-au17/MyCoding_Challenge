
const form = document.querySelector('.form');

const username = document.querySelector('#username');

const email = document.querySelector('#email');

const password = document.querySelector('#password');

const passwordTwo = document.querySelector('#passwordTwo');


form.addEventListener('submit', event => {

	event.preventDefault();
	
	checkFormInput();

});

function checkFormInput() {
	

	const usernameValue = username.value.trim();

	const UserEmailValue = email.value.trim();

	const passwordFirstValue = password.value.trim();
	
	const passwordTwoValue = passwordTwo.value.trim();
	
	if(usernameValue === '') {
		forSetError(username, 'Username is blank');
	} else {
		forSuccessSet(username);
	}
	
	if(UserEmailValue === '') {
		forSetError(email, 'Email is blank');

	} else if (!isValidEmail(UserEmailValue)) {

		forSetError(email, 'invalid email');
		
	} else {
		forSuccessSet(email);
	}
	
	if(passwordFirstValue === '') {
		forSetError(password, 'Password is blank');
	} else {
		forSuccessSet(password);
	}
	
	if(passwordTwoValue === '') {
		forSetError(passwordTwo, 'PasswordTwo is blank');

	} else if(passwordFirstValue !== passwordTwoValue) {

		forSetError(passwordTwo, 'Passwords is not matched');

	} else{
		forSuccessSet(passwordTwo);
		const userdata = {
            user: usernameValue,
            email: UserEmailValue
        }
        console.log(userdata);
	}
}

function forSetError(input, message) {

	const userFormControls = input.parentElement;
	const small = userFormControls.querySelector('small');
	userFormControls.className = 'input-div error';
	small.innerText = message;

}

function forSuccessSet(input) {

	const userFormControls = input.parentElement;
	userFormControls.className = 'input-div success';

}
	
function isValidEmail(email) {

	return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email);

}

