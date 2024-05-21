#!/usr/bin/node

const fs = require('fs');

// Get the file path and string to write from the command line arguments
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

// Write the string to the file using utf-8 encoding
fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
  if (err) {
    // If an error occurred, print the error object
    console.log(err);
  }
});
