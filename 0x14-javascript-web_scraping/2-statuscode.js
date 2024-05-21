#!/usr/bin/node

const request = require('request');

// Get the URL from the command line arguments
const url = process.argv[2];

// Make a GET request to the specified URL
request.get(url, (error, response) => {
  if (error) {
    // If an error occurred, print the error object
    console.log(error);
  } else {
    // Print the status code
    console.log(`code: ${response.statusCode}`);
  }
});
