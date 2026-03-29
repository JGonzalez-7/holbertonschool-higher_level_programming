// select the clickable element
const updateHeader = document.querySelector('#update_header');

// select the <header> element
const header = document.querySelector('header');

// add click event
updateHeader.addEventListener('click', function () {
  // update the text content
  header.textContent = 'New Header!!!';
});
