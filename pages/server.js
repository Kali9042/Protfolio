// server.js
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

const app = express();

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/contact-me', { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Connected to MongoDB'))
  .catch((err) => {
    console.error('Error connecting to MongoDB:', err);
    process.exit(1);
  });

// Define the schema for the contact form data
const contactSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
    trim: true,
    validate: (value) => value.length > 0
  },
  email: {
    type: String,
    required: true,
    trim: true,
    validate: (value) => value.length > 0
  },
  phone: {
    type: String,
    required: true,
    trim: true,
    validate: (value) => value.length > 0
  },
  subject: {
    type: String,
    required: true,
    trim: true,
    validate: (value) => value.length > 0
  },
  message: {
    type: String,
    required: true,
    trim: true,
    validate: (value) => value.length > 0
  }
});

// Create a model for the contact form data
const Contact = mongoose.model('Contact', contactSchema);

// Use body-parser to parse the request body
app.use(bodyParser.urlencoded({ extended: true }));

// Serve the HTML file
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

// Handle the form submission
app.post('/submit', (req, res) => {
  const contact = new Contact(req.body);
  contact.save((err) => {
    if (err) {
      console.error('Error saving contact form data:', err);
      res.status(500).send('Error saving contact form data');
    } else {
      console.log('Contact form data saved successfully');
      res.send('Contact form data saved successfully');
    }
  });
});

// Start the server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
}).on('error', (err) => {
  console.error('Error starting server:', err);
  process.exit(1);
});