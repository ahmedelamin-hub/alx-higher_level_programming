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
    const todos = JSON.parse(body);
    const completedTasks = {};

    // Iterate over each todo item
    todos.forEach(todo => {
      if (todo.completed) {
        if (!completedTasks[todo.userId]) {
          completedTasks[todo.userId] = 0;
        }
        completedTasks[todo.userId]++;
      }
    });

    // Print the completed tasks by user ID
    console.log(completedTasks);
  }
});
