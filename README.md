# Yearly Calendar Web App

A web application that generates a yearly calendar view split into four quadrants, with month names displayed vertically on the right side of each month's calendar.

## Features

- Select any start month/year to generate a yearly calendar view
- Calendar is split into four quadrants
- Month names are displayed vertically (first three letters) on the right side
- Week numbers are displayed
- Modern, clean interface

## Installation

1. Make sure you have Python 3.7+ installed
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

1. Navigate to the project directory
2. Run the Flask application:
   ```
   python app.py
   ```
3. Open your web browser and go to `http://localhost:5000`

## Usage

1. Select a start month/year using the date picker at the top of the page
2. Click "Generate Calendar" to update the view
3. The calendar will automatically display 12 months starting from your selected date

## Default Behavior

The calendar defaults to starting from January of the next year when first loaded.
