# Chatbot Guide

This README file explains how to integrate the Flask backend with the React frontend for your chatbot application. It provides step-by-step instructions for setting up the environment and connecting the components.

## Project Overview

This project consists of:

Backend (Flask): Provides the API endpoint to interact with OpenAI’s GPT model.

## Getting Started

### Prerequisites

Ensure you have the following installed:

Python 3.7+

Node.js and npm

React.js

OpenAI API Key

### Backend Setup (Flask)

Clone the Repository
Clone the repository and navigate to the backend directory:

git clone <repository-url>
cd <repository-name>

Install Dependencies
Create a virtual environment and install required Python libraries:

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install requirements.txt

### Configure Environment Variables
Create a .env file in the backend directory with the following content:

API_KEY=your_openai_api_key

### Run the Backend
Start the Flask server:

python app.py

The server will run on http://127.0.0.1:5000.

## Frontend Setup (React)

### Navigate to your Frontend Directory
Navigate to the frontend directory:

cd frontend

### Connecting Frontend to Backend

API URL
Update the React application’s API endpoint in the App.js file:

const res = await axios.post('http://127.0.0.1:5000/predict', { statement: message });

### Start the Frontend
Run the React application:

npm start

The React app will run on http://localhost:3000.

## Test the Chatbot
Open the React application in your browser and interact with the chatbot.

