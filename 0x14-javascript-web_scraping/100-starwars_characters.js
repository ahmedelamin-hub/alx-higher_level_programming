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

    // Iterate over each character URL
    characters.forEach(characterUrl => {
      // Make a GET request to get character details
      request.get(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.log(charError);
        } else {
          // Parse the character details and print the character name
          const characterData = JSON.parse(charBody);
          console.log(characterData.name);
        }
      });
    });
  }
});
