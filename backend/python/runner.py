import sys, json, subprocess, tempfile, os

def run_code(code:str):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as tmp:
        tmp.write(code.encode("utf-8"))
        tmp.flush()
        filename = tmp.name
    try:
        result = subprocess.run(
                ["python3",filename],
                capture_output=True,
                text=True,
                timeout=5
             )
        return {"stdout":result.stdout,"stderr":result.stderr,"returncode":result.returncode}
    except subprocess.TimeoutExpired:
        return {"error":"Execution timre out"}
    finally:
        try: os.remove(filename)
        except: pass

if __name__ == "__main__":
    event = json.loads(sys.stdin.read() or "{}")
    print(json.dumps(run_code(event.get("code",""))))
