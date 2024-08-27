import redis from 'redis';

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

// Subscribe to the channel 'holberton school channel'
client.subscribe('holberton school channel');

// Listen for messages
client.on('message', (channel, message) => {
  console.log(message);

  // If the message is 'KILL_SERVER', unsubscribe and quit
  if (message === 'KILL_SERVER') {
    client.unsubscribe();
    client.quit();
  }
});
