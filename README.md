# <img src="https://cdn-icons-png.flaticon.com/128/17379/17379046.png" alt="Alt text" width="30" height="30"> ByteBox

## ByteBox is a lightweight, containerized multi-language online code execution platform. It lets users write, compile, and run code securely inside isolated Docker sandboxes — all from a modern web UI built with React + Monaco Editor.

### Features 
-   **Frontend**  :  <img src="https://cdn-icons-png.flaticon.com/128/15484/15484268.png" width="20"> React + Monaco Editor (the same editor behind <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Visual_Studio_Code_1.35_icon.svg/512px-Visual_Studio_Code_1.35_icon.svg.png" width="20"> VS Code)
-  Backend: Flask API + <img src="https://cdn-icons-png.flaticon.com/128/15466/15466088.png" width="20"> Docker sandbox for safe execution

### Languages supported:
- Python <img src="https://cdn-icons-png.flaticon.com/128/5968/5968350.png" width=20>
- Java <img src="https://cdn-icons-png.flaticon.com/128/226/226777.png" width=20>
- C++ <img src="https://cdn-icons-png.flaticon.com/128/6132/6132222.png" width=20>

`[Note: New Language can be added easily]`

### <img src="https://cdn-icons-png.flaticon.com/128/891/891399.png" width=20> Secure execution:
- No network access
- CPU, memory, and PID limits
- Temporary containers, auto-cleaned after execution

🔧 Extensible: Add more languages easily (Go, Rust, Node.js, etc.)

## 🛠 How It Works

1. **User writes code** in the Monaco Editor (frontend).

2. **Code is sent via API** to the backend endpoint:  
   `POST /run/<language>`

3. **Backend spins up a temporary Docker container** with the appropriate runtime image:
   - `code-runner-python`
   - `code-runner-cpp`
   - `code-runner-java`

4. **Code runs safely inside the sandbox.**

5. **Output** (`stdout`, `stderr`, `return code`) is returned to the frontend and displayed.


## 📦 Getting Started
1. Clone the repo
```bash
git clone https://github.com/YashSHarmaAmarnath/ByteBox.git
cd ByteBox
```

### <img src="https://cdn-icons-png.flaticon.com/128/3767/3767084.png" width=20> Project Structure
```
backend
├── api
│   └── app.py
├── cpp
│   ├── Dockerfile
│   └── runner.py
├── java
│   ├── Dockerfile
│   └── runner.py
└── python
    ├── Dockerfile
    └── runner.py
5 directories, 7 files
```

2. Build the runner images
```bash
# Python runner
cd backend
docker build -t code-runner-python ./python
# C++ runner
docker build -t code-runner-cpp  ./cpp
# Java runner
docker build -t code-runner-java   ./java
```

3. Run the backend
```
cd backend
pip install Flask flask-cors
python app.py
```
Backend runs at http://localhost:5000

4. Run the frontend
```
cd frontend
npm install
npm run dev
```
Frontend runs at http://localhost:3000












