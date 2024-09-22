#!/usr/bin/node
/**
 * Star War API
 */
/*
Promisfy request
*/
const request = require('request');
const util = require('util');
const requestPromise = util.promisify(request);

if (process.argv.length < 3) { process.exit(1); }
const actorId = process.argv[2];
/**
 * getCharacter - print list of actor
 * @param {string} id
 */
async function getCharacter (id) {
  const fullPath = `https://swapi-api.alx-tools.com/api/films/${id}`;
  try {
    const response = await requestPromise({ uri: fullPath });
    const data = await JSON.parse(response.body);
    const characters = data.characters;
    const listOfNames = [];
    for (let i = 0; i < characters.length; i++) {
      try {
        const response = await requestPromise(characters[i]);
        const data = await JSON.parse(response.body);
        listOfNames.push(await data.name);
      } catch (error) {
        console.error(error);
      }
    }
    for (const actor of listOfNames) {
      console.log(actor);
    }
  } catch (error) {
    console.error(error);
  }
}
/* call getCharacter on argv */
getCharacter(actorId);
