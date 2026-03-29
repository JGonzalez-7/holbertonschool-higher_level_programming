// select the element with id '#red_header'
const redHeader = document.querySelector('#red_header');

// select the <header> element
const header = document.querySelector('header');

// add a click event listener
redHeader.addEventListener('click', function () {
//change the text color to red
  header.style.color = '#FF0000';
});
