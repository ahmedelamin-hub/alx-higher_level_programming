#!/usr/bin/node

const request = require('request');

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

// Make a GET request to the specified URL
request.get(apiUrl, (error, response, body) => {
  if (error) {
    // If an error occurred, print the error object
    console.log(error);
  } else {
    // Parse the response body as JSON
    const data = JSON.parse(body);
    // Initialize a counter for the number of movies with Wedge Antilles
    let count = 0;
    // Iterate over each film
    data.results.forEach(film => {
      // Check if character ID 18 (Wedge Antilles) is in the film's characters array
      if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        count++;
      }
    });
    // Print the count
    console.log(count);
  }
});
