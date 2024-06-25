#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 5) {
  console.error('Usage: node 102-concat.js <fileA> <fileB> <destination>');
  process.exit(1);
}

const fileAPath = process.argv[2];
const fileBPath = process.argv[3];
const destinationPath = process.argv[4];

// Read fileA
fs.readFile(fileAPath, 'utf8', (err, dataA) => {
  if (err) {
    console.error(`Error reading file ${fileAPath}:`, err.message);
    process.exit(1);
  }

  // Read fileB
  fs.readFile(fileBPath, 'utf8', (err, dataB) => {
    if (err) {
      console.error(`Error reading file ${fileBPath}:`, err.message);
      process.exit(1);
    }

    // Concatenate contents
    const concatenatedData = dataA + dataB;

    // Write to destination file
    fs.writeFile(destinationPath, concatenatedData, 'utf8', (err) => {
      if (err) {
        console.error(`Error writing to file ${destinationPath}:`, err.message);
        process.exit(1);
      }
    });
  });
});
