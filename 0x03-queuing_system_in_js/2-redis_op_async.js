import redis from 'redis';
import { promisify } from 'util';

// Create a Redis client
const client = redis.createClient();

// Handle connection errors
client.on('error', (err) => {
  console.error('Redis client not connected to the server:', err.message);
});

// Handle successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Function to set a new school
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// Promisify the get method
const getAsync = promisify(client.get).bind(client);

// Async function to display the value of a school
async function displaySchoolValue(schoolName) {
  try {
    const reply = await getAsync(schoolName);
    console.log(reply);
  } catch (err) {
    console.error('Error retrieving value:', err);
  }
}

// Call the functions as required
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
