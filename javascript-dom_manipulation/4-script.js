// select the clickable element
const addItem = document.querySelector('#add_item');

// select the <ul> with class "my_list"
const list = document.querySelector('.my_list');

// add click event
addItem.addEventListener('click', function () {
  // create a new <li> element
  const newItem = document.createElement('li');

  // add text content
  newItem.textContent = 'Item';

  // append the new <li> to the <ul>
  list.appendChild(newItem);
});
