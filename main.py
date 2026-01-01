from fastapi import FastAPI
from pydantic import BaseModel
from translator import translate
import subprocess
import tempfile
import os
import re

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Code(BaseModel):
    code: str


def gez_error_message(stderr: str) -> str:
    if "SyntaxError" in stderr or "IndentationError" in stderr:
        return "nah this syntax ain’t it 💀"
    return "💀 You messed up, chief"


@app.post("/run")
def run_code(data: Code):
    gez_code = data.code
    py_code = translate(gez_code)

    gez_lines = gez_code.splitlines()

    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".py",
        delete=False,
        encoding="utf-8"
    ) as f:
        f.write(py_code)
        filename = f.name

    try:
        result = subprocess.run(
            ["python", filename],
            capture_output=True,
            text=True,
            timeout=3
        )

        error_info = None

        if result.stderr:
            stderr = result.stderr

            # 🔍 Extract python error line number
            match = re.search(r"line (\d+)", stderr)
            py_line = int(match.group(1)) if match else None

            gez_line = py_line if py_line and py_line <= len(gez_lines) else None

            error_info = {
                "message": gez_error_message(stderr),
                "line": gez_line,
                "gez_code": gez_lines[gez_line - 1] if gez_line else None,
                "details": stderr.splitlines()[-1]
            }

        return {
            "output": result.stdout,
            "error": error_info,
            "translated": py_code
        }

    finally:
        os.remove(filename)
