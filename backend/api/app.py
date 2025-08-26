from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess, json, tempfile, os

app = Flask(__name__)

CORS(app)

IMAGE_MAP = {
    "python": "code-runner-python",
    "cpp": "code-runner-cpp",
    "java": "code-runner-java"
}

def run_in_docker(language, code):
    if language not in IMAGE_MAP:
        return {"error": "Unsupported language"}

    tmpdir = tempfile.mkdtemp()
    try:
        result = subprocess.run(
            [
                "docker", "run", "-i", "--rm",
                "--network", "none",
                "--cpus", "1", "-m", "256m", "--pids-limit", "64",
#                "-v", f"{tmpdir}:/tmp",
                IMAGE_MAP[language]
            ],
            input=json.dumps({"code": code}).encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=10
        )
        return json.loads(result.stdout or "{}")
    except Exception as e:
        return {"error": str(e)}
    finally:
 #       subprocess.run(["rm", "-rf", tmpdir])
        if os.path.exists(tmpdir):
            subprocess.run(["rm", "-rf", tmpdir], check=False)

@app.route("/run/<language>", methods=["POST"])
def run_code(language):
    payload = request.get_json(force=True)
    code = payload.get("code", "")
    return jsonify(run_in_docker(language, code))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

