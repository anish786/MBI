Run on Local Machine
- First Step:
  - Make sure Backend API is running on http://localhost:5000 (Steps to run in MBI-API)
- Second Step:
  - Go to package.json and add this line below
    - "proxy": "http://localhost:5000",
- Third Step:
  - Run npm run "npm start"
