// select the <ul> where movies will be displayed
const listMovies = document.querySelector('#list_movies');

// fetch data from the API
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(function (response) {
    return response.json(); // convert to JSON
  })
  .then(function (data) {
    // loop through each movie
    data.results.forEach(function (movie) {
      // create a new <li>
      const li = document.createElement('li');

      // set movie title
      li.textContent = movie.title;

      // append to the <ul>
      listMovies.appendChild(li);
    });
  })
  .catch(function (error) {
    console.error('Error fetching movies:', error);
  });
