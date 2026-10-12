# Nutrition Recommendation for Cancer Patients (Spanish)

A Flask web app that gives cancer patients stage-specific nutrition recommendations in Spanish. Users register, log in, choose a cancer category and a stage, and the app shows the matching recommendation from a curated CSV dataset.

> **Medical disclaimer:** This project is for educational and research purposes only. It does not replace advice from an oncologist, dietitian, or other qualified healthcare professional. Nutritional needs during cancer treatment vary widely, so always consult a clinician before changing a diet.

## Features

- User registration and login
- Choose a category (one per folder in `train/`) and a stage
- Recommendation shown from the matching CSV row
- Spanish-language content

## How It Works

1. A new user registers on `/user_register`. Details are stored in a `user_details` database table.
2. After logging in at `/login`, the user lands on `/user_home`, which lists every sub-folder of `train/` as a selectable category.
3. The user picks a category and a stage. The app opens `train/<category>/<category>.csv`, finds the row whose `Stages` column matches, and displays it.

The recommendations are a lookup from curated data, not a machine-learning model.

## Tech Stack

- Python, Flask
- Jinja2 HTML templates
- MySQL database (`python_spinach_nutritional_strategy`) accessed through the custom `ar_master` helper module
- CSV files for the recommendation data

## Project Structure

```
nutrition_recommendation/
├── app.py                 # Flask routes (name may differ)
├── ar_master.py           # database helper (master_flask_code)
├── templates/             # index, student (login), student_register, user_home
├── train/
│   └── <Category>/
│       └── <Category>.csv # must include a "Stages" column
└── Personalized_spinach_nutritional_strategy/
```

## Getting Started

### Prerequisites

- Python 3.x
- A running MySQL server

### Installation

```bash
git clone https://github.com/Akash250902/nutrition_recommendation.git
cd nutrition_recommendation
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install flask               # plus any database driver ar_master needs
```

### Database

Create the database and the `user_details` table:

```sql
CREATE DATABASE python_spinach_nutritional_strategy;
USE python_spinach_nutritional_strategy;

CREATE TABLE user_details (
    id       INT PRIMARY KEY,
    name     VARCHAR(100) NOT NULL,
    contact  VARCHAR(100),
    email    VARCHAR(100),
    address  VARCHAR(100),
    password VARCHAR(255) NOT NULL
);
```

Then set the connection details (host, user, password) in `ar_master.py`, ideally through environment variables rather than hard-coded values.

### Run

```bash
python app.py
```

Then open http://127.0.0.1:5000.

## Known Limitations

- Not clinically validated
- Passwords are currently stored in plain text
- Database queries are built by string concatenation, which is vulnerable to SQL injection
- The secret key is hard-coded and the app runs with `debug=True`

These should be fixed before any real-world use: hash passwords, use parameterized queries, load the secret key from an environment variable, and turn debug off.

## Author

**Akash** ([@Akash250902](https://github.com/Akash250902))

