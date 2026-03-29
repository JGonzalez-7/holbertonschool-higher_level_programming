// select the clickable element
const redHeader = document.querySelector('#red_header');

// select the <header> element
const header = document.querySelector('header');

// add click event
redHeader.addEventListener('click', function () {
// add the class "red" to the header
  header.classList.add('red');
});