# Quiz Master – Web-Based Quiz Application

**Quiz Master** is a simple and interactive quiz game built with HTML, CSS (Tailwind), and JavaScript for the frontend. It is supported by Python (`app.py`) logic that simulates backend operations like handling questions, checking answers, and calculating the final score.

---

## Overview

This project offers a lightweight quiz experience directly in the browser. The frontend displays multiple-choice questions and provides immediate feedback, while the Python script demonstrates how quiz logic can be handled programmatically in the backend.

---

## Features

* Multiple-choice quiz interface
* Real-time correct/incorrect feedback
* Final score display after the quiz
* Option to restart the quiz
* Simple, responsive layout using Tailwind CSS
* Python logic for question handling and scoring

---

## Frontend (HTML, CSS, JavaScript)

All frontend code is contained in a single `index.html` file. Styling is handled with Tailwind CSS via CDN, and interactivity is managed with vanilla JavaScript.

### How to Run

1. Save the code as `index.html`.
2. Open it in any modern web browser.
3. No server or additional setup is required.

---

## Backend Logic (Python – `app.py`)

The backend logic is written in Python and demonstrates how quiz data is stored, answers are checked, and scores are calculated.

### How to Use

1. Save the code as `app.py`.
2. Open your terminal or command prompt.
3. Navigate to the folder containing `app.py`.
4. Run the script using:

   ```bash
   python app.py
   ```

The sample code will simulate how questions are managed and scored in a typical backend.

---

## Project Structure

```
.
├── index.html      # Frontend – Quiz UI with HTML/CSS/JS
└── app.py          # Python logic – Questions, answer validation, scoring
```

---

## Technologies Used

* **Frontend:**

  * HTML5
  * Tailwind CSS (via CDN)
  * JavaScript

* **Backend (logic only):**

  * Python 3

---

## Future Enhancements

* Add more question formats (e.g., true/false)
* Introduce difficulty levels
* Include a timer for each question or the entire quiz
* Improve UI with smoother animations
* Expand question set for variety

---

Feel free to explore, modify, or extend this project to fit your needs.
Enjoy building and playing Quiz Master! 🎉
