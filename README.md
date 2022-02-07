# MBI

# Run Backend on Local Machine (localhost:5000)
  - Run "python app.py"

# Run front-end on Local Machine (localhost:3000)

First Step:
  - Make sure Backend API is running on http://localhost:5000 (Steps to run in MBI-API)
Second Step:
  - Go to package.json and add this line below
    - "proxy": "http://localhost:5000",
Third Step:
  - Run npm run "npm start"
