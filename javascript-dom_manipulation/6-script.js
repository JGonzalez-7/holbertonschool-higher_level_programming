// select the element where the name will be displayed
const characterDiv = document.querySelector('#character');

// fetch data from the API
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(function (response) {
    return response.json(); // convert response to JSON
  })
  .then(function (data) {
    // update the DOM with the character name
    characterDiv.textContent = data.name;
  })
  .catch(function (error) {
    console.error('Error fetching data:', error);
  });
