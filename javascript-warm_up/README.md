# JavaScript Warm Up

Introductory JavaScript exercises focused on Node.js basics, command-line arguments, loops, functions, recursion, arrays, and objects.

## Files
- `0-javascript_is_amazing.js`: prints `JavaScript is amazing`.
- `1-multi_languages.js`: prints three programming language messages.
- `2-arguments.js`: prints whether no argument, one argument, or multiple arguments were passed.
- `3-value_argument.js`: prints the first argument passed to the script, or `No argument`.
- `4-concat.js`: prints two arguments in the format `<arg1> is <arg2>`.
- `5-to_integer.js`: converts the first argument to an integer and prints either the number or `Not a number`.
- `6-multi_languages_loop.js`: prints three lines from an array using a loop.
- `7-multi_c.js`: prints `C is fun` a given number of times.
- `8-square.js`: prints a square made of `X` characters based on the provided size.
- `9-add.js`: defines an `add(a, b)` function and prints the sum of two integers from the command line.
- `10-factorial.js`: computes and prints the factorial of an integer using recursion.
- `11-second_biggest.js`: prints the second biggest integer from the provided arguments.
- `12-object.js`: updates an object property from `12` to `89` and prints the object before and after.
- `13-add.js`: exports a function named `add` that returns the sum of two integers.

## Running Scripts
```bash
node javascript-warm_up/<script_name>.js
```

Example:
```bash
node javascript-warm_up/8-square.js 4
```

## Notes
- All scripts use Node.js via `#!/usr/bin/node`.
- `13-add.js` is a module export and is meant to be required by another file.
