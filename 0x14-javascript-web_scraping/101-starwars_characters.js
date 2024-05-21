#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Construct the URL for the Star Wars API
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the specified URL to get movie details
request.get(url, (error, response, body) => {
  if (error) {
    // If an error occurred, print the error object
    console.log(error);
  } else {
    // Parse the response body as JSON
    const filmData = JSON.parse(body);
    const characters = filmData.characters;

    // Function to make a GET request for each character and print the name
    const printCharacterName = (index) => {
      if (index >= characters.length) {
        return;
      }

      request.get(characters[index], (charError, charResponse, charBody) => {
        if (charError) {
          console.log(charError);
        } else {
          // Parse the character details and print the character name
          const characterData = JSON.parse(charBody);
          console.log(characterData.name);
          // Call the function recursively for the next character
          printCharacterName(index + 1);
        }
      });
    };

    // Start the recursive function with the first character
    printCharacterName(0);
  }
});
