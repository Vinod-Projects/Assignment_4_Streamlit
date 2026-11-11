# Student Grade Manager

A Streamlit app for adding students, assigning grades, and viewing class statistics.
Student data is kept in Streamlit session state so it remains available across app reruns.

## Run locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run grade_app.py
```

Marks are whole numbers from 0 to 100. Grades use the Day 2 scale: A (90–100),
B (80–89), C (70–79), D (60–69), and E (below 60).
