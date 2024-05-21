#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// Get the URL and file path from the command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request to the specified URL
request.get(url, (error, response, body) => {
  if (error) {
    // If an error occurred, print the error object
    console.log(error);
  } else {
    // Write the response body to the file with utf-8 encoding
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        // If an error occurred while writing, print the error object
        console.log(err);
      }
    });
  }
});
