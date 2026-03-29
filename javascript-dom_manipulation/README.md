# JavaScript DOM Manipulation

Browser-side JavaScript exercises focused on selecting DOM elements, reacting to user events, updating page content, and consuming small external APIs with `fetch`.

## Files
- `0-script.js`: selects the `<header>` element and changes its text color to red.
- `1-script.js`: changes the `<header>` text color to red when the user clicks the element with id `red_header`.
- `2-script.js`: adds the class `red` to the `<header>` when the user clicks `#red_header`.
- `3-script.js`: toggles the `<header>` class between `red` and `green` when the user clicks `#toggle_header`.
- `4-script.js`: appends a new `<li>` with the text `Item` to `.my_list` when the user clicks `#add_item`.
- `5-script.js`: updates the `<header>` text to `New Header!!!` when the user clicks `#update_header`.
- `6-script.js`: fetches the Star Wars character from `https://swapi-api.hbtn.io/api/people/5/?format=json` and displays the character name inside `#character`.
- `7-script.js`: fetches Star Wars films from `https://swapi-api.hbtn.io/api/films/?format=json` and appends each movie title to `#list_movies`.
- `8-script.js`: waits for `DOMContentLoaded`, fetches the French translation of hello from `https://hellosalut.stefanbohacek.com/?lang=fr`, and displays it inside `#hello`.

## Concepts Practiced
- `document.querySelector()`
- `addEventListener()`
- `classList.add()` / `classList.remove()` / `classList.contains()`
- `createElement()` and `appendChild()`
- `textContent` and inline style updates
- `fetch()` with promise chaining
- Waiting for the DOM to load before querying elements

## Running The Tasks
These scripts are meant to be loaded by their corresponding HTML task files in a browser environment. Open the relevant HTML page and check the rendered page behavior or the browser console.

Example script tag:

```html
<script src="0-script.js"></script>
```

## Notes
- `6-script.js`, `7-script.js`, and `8-script.js` require internet access because they call public APIs.
- The scripts use modern browser JavaScript and are not intended to be run directly with Node.js.
