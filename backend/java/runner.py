import sys, json, subprocess, tempfile, os, shutil

def run_code(code: str):
    classname = "Main"
    javafile = f"/tmp/{classname}.java"
    with open(javafile, "w") as f:
        f.write(code)
    try:
        # compile
        comp = subprocess.run(
            ["javac", javafile],
            capture_output= True,
            text= True,
            timeout= 5,
            check= True,
        )
        # Run 
        result = subprocess.run(
            ["java","-cp","/tmp",classname],
            capture_output= True,
            text= True,
            timeout= 5
        )
        return {"stdout": result.stdout, "stderr": result.stderr, "returncode": result.returncode}
    except subprocess.TimeoutExpired:
        return {"error": "Execution timed out"}
    except subprocess.CalledProcessError as e:
        return {"error":"Compilation failed", "stderr":e.stderr or e.stdout}
    finally:
        for p in [javafile, f"/tmp/{classname}.class"]:
            try: os.remove(p)
            except: pass

if __name__ == "__main__":
    event = json.loads(sys.stdin.read() or "{}")
    print(json.dumps(run_code(event.get("code", ""))))
