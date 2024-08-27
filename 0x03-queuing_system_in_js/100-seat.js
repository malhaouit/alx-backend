import express from 'express';
import redis from 'redis';
import { promisify } from 'util';
import kue from 'kue';

const app = express();
const port = 1245;

// Create Redis client and promisify methods
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Create a Kue queue
const queue = kue.createQueue();

// Initialize available seats and reservation status
let reservationEnabled = true;

// Function to reserve seats
async function reserveSeat(number) {
  await setAsync('available_seats', number);
}

// Function to get the current available seats
async function getCurrentAvailableSeats() {
  const seats = await getAsync('available_seats');
  return seats !== null ? parseInt(seats, 10) : null;
}

// Set initial number of available seats to 50
reserveSeat(50);

// Route to get the number of available seats
app.get('/available_seats', async (req, res) => {
  const availableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: availableSeats });
});

// Route to reserve a seat
app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  const job = queue.create('reserve_seat')
    .save((err) => {
      if (err) {
        return res.json({ status: 'Reservation failed' });
      } else {
        return res.json({ status: 'Reservation in process' });
      }
    });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (errorMessage) => {
    console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
  });
});

// Route to process the queue
app.get('/process', (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    const availableSeats = await getCurrentAvailableSeats();

    if (availableSeats > 0) {
      await reserveSeat(availableSeats - 1);

      if (availableSeats - 1 === 0) {
        reservationEnabled = false;
      }

      done();
    } else {
      done(new Error('Not enough seats available'));
    }
  });
});

// Start the server
app.listen(port, () => {
  console.log(`API available on localhost port ${port}`);
});
