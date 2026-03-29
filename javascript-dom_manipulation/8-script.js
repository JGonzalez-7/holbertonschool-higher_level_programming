// wait until the DOM is fully loaded
document.addEventListener('DOMContentLoaded', function () {
  // select the element
  const helloDiv = document.querySelector('#hello');

  // fetch translation from API
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      // display the translated "hello"
      helloDiv.textContent = data.hello;
    })
    .catch(function (error) {
      console.error('Error fetching translation:', error);
    });
});
