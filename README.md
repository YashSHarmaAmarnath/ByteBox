ByteBox
ByteBox is a lightweight, containerized multi-language online code execution platform.
It lets users write, compile, and run code securely inside isolated Docker sandboxes — all from a modern web UI built with React + Monaco Editor.

✨ Features
🖥️ Frontend: React + Monaco Editor (the same editor behind VS Code)

⚡ Backend: Flask API + Docker sandbox for safe execution

🔤 Languages supported:

Python

C++

Java

🔒 Secure execution:

No network access

CPU, memory, and PID limits

Temporary containers, auto-cleaned after execution

🔧 Extensible: Add more languages easily (Go, Rust, Node.js, etc.)

🛠 How It Works
User writes code in the Monaco Editor (frontend).

Code is sent via API to the backend (/run/<language>).

Backend spins up a temporary Docker container with the appropriate runtime image:

code-runner-python

code-runner-cpp

code-runner-java

Code runs safely inside the sandbox.

Output (stdout, stderr, return code) is returned to the frontend and displayed.

📦 Getting Started
1. Clone the repo
git clone https://github.com/YashSHarmaAmarnath/ByteBox.git
cd ByteBox

2. Build the runner images
# Python runner
cd runners/python
docker build -t code-runner-python .
```bash
# C++ runner
cd ../cpp
docker build -t code-runner-cpp .

```bash
# Java runner
cd ../java
docker build -t code-runner-java .

3. Run the backend
cd backend
pip install -r requirements.txt
python app.py

Backend runs at http://localhost:5000

4. Run the frontend
cd frontend
npm install
npm start

Frontend runs at http://localhost:3000