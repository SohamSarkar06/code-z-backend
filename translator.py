import re

"""
🔥 Gen-Z Array Helper Usage (Reference)

vibe nums = pullUp([1, 2, 3, 4, 5])

yap(min(nums))     # smallest element
yap(Max(nums))     # largest element
yap(sum(nums))     # sum of elements
yap(avg(nums))     # average
yap(mid(nums))     # middle element
yap(rev(nums))     # reversed array
"""

SYNTAX_MAP = {
    # conditionals
    "lowkeyIf": "if",
    "butAlsoIf": "elif",
    "whateverMan": "else",

    # loops
    "keepLoopingTill": "for",
    "stillStuckIn": "while",

    # functions
    "cook": "def",
    "sendBack": "return",

    # output / input
    "yap(": "print(",
    "yapln(": "print(",
    "flex(": "print(",
    "spillTea(": "print(",
    "sayBro(": "input(",

    # values
    "frfr": "True",
    "cap": "False",
    "ghosted": "None",

    # flow control
    "imOut": "break",
    "nahKeepGoing": "continue",
    "doNothing": "pass",

    # comparisons
    "givingSameVibeAs": "==",
    "notTheSameAs": "!=",
}

# 🔥 Gen-Z Array Helpers (auto-injected into user code)
ARRAY_HELPERS = """
def avg(arr):
    return sum(arr) / len(arr) if arr else 0

def mid(arr):
    n = len(arr)
    return arr[n // 2] if n else None

def rev(arr):
    return arr[::-1]

def pullUp(arr):
    return list(map(int, arr))
"""

def translate(code: str) -> str:
    lines = code.split("\\n")
    translated_lines = []

    for line in lines:
        stripped = line.lstrip()
        indent = line[:len(line) - len(stripped)]

        # vibe → normal variable
        if stripped.startswith("vibe "):
            stripped = stripped.replace("vibe ", "", 1)

        # replace Gen-Z syntax
        for gez, py in SYNTAX_MAP.items():
            stripped = stripped.replace(gez, py)

        translated_lines.append(indent + stripped)

    # 🔥 inject array helpers at the top
    return ARRAY_HELPERS + "\\n\\n" + "\\n".join(translated_lines)
