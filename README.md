# Workout Tracker (Nutritionix + Sheety API)

A simple Python automation tool that converts your natural language workout input into structured data and logs it into a Google Sheet.

## Features

- Accepts plain English workout input  
  Example: "Ran 3 km and did 20 minutes yoga"
- Uses Nutritionix API to analyze exercises
- Extracts:
  - Exercise name
  - Duration
  - Calories burned
- Automatically logs data into Google Sheets using Sheety API
- Uses environment variables for secure credential storage

---

## Tech Stack

- Python
- Requests library
- Nutritionix API
- Sheety API
- Datetime module

---

## Setup Instructions

### 1. Clone the repository

git clone https://github.com/your-username/workout-tracker.git

cd workout-tracker


### 2. Install dependencies

pip install requests


### 3. Set Environment Variables

#### Windows (CMD)

setx APP_ID "your_nutritionix_app_id"
setx APP_KEY "your_nutritionix_app_key"
setx SHEETY_ENDPOINT "your_sheety_endpoint"
setx TOKEN "your_sheety_bearer_token"


#### Mac/Linux

export APP_ID="your_nutritionix_app_id"
export APP_KEY="your_nutritionix_app_key"
export SHEETY_ENDPOINT="your_sheety_endpoint"
export TOKEN="your_sheety_bearer_token"


---

## Usage

Run the script:


python main.py


Enter your workout when prompted:


Tell me which exercises you did today:


Example input:

I ran 5 km and cycled for 30 minutes


---

## Output

- Displays extracted workout details in console
- Logs the workout into your Google Sheet automatically

---

## Environment Variables

| Variable         | Description                      |
|----------------|----------------------------------|
| APP_ID         | Nutritionix App ID               |
| APP_KEY        | Nutritionix API Key              |
| SHEETY_ENDPOINT| Sheety API endpoint URL          |
| TOKEN          | Sheety Bearer Token              |

---

## Notes

- Make sure your Sheety API is connected to a Google Sheet
- Ensure correct authorization headers for Sheety
- Nutritionix API requires valid credentials

---

## Future Improvements

- Add support for multiple exercises in loop
- Improve error handling
- Add CLI arguments instead of input()
- Build a frontend dashboard

---
