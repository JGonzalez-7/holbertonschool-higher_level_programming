// select the toggle element
const toggleHeader = document.querySelector('#toggle_header');

// select the header
const header = document.querySelector('header');

// add click event
toggleHeader.addEventListener('click', function () {
  // if header has class 'red'
  if (header.classList.contains('red')) {
    // remove red and add green
    header.classList.remove('red');
    header.classList.add('green');
  } else {
    // otherwise remove green and add red
    header.classList.remove('green');
    header.classList.add('red');
  }
});
