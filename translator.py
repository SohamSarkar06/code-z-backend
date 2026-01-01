import re

"""
🔥 Gen-Z Array Helper Usage (Reference)

vibe nums = pullUp([5, 2, 9, 1])

yap(min(nums))
yap(Max(nums))
yap(sum(nums))
yap(avg(nums))
yap(mid(nums))
yap(rev(nums))

yap(sort.asc(nums))   # ascending
yap(sort.desc(nums))  # descending
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

    # 🔥 array built-ins
    "Max(": "max(",

    # values
    "frfr": "True",
    "cap": "False",
    "ghosted": "None",

    # flow
    "imOut": "break",
    "nahKeepGoing": "continue",
    "doNothing": "pass",

    # comparisons
    "givingSameVibeAs": "==",
    "notTheSameAs": "!=",
}

# 🔥 Array helpers (stable & backward compatible)
ARRAY_HELPERS = (
    "def avg(arr):\n"
    "    return sum(arr) / len(arr) if arr else 0\n\n"

    "def mid(arr):\n"
    "    n = len(arr)\n"
    "    return arr[n // 2] if n else None\n\n"

    "def rev(arr):\n"
    "    return arr[::-1]\n\n"

    "def pullUp(arr):\n"
    "    return list(map(int, arr))\n\n"

    "# 🔥 Gen-Z sort namespace\n"
    "class sort:\n"
    "    @staticmethod\n"
    "    def asc(arr):\n"
    "        return sorted(arr)\n\n"
    "    @staticmethod\n"
    "    def desc(arr):\n"
    "        return sorted(arr, reverse=True)\n"
)

def translate(code: str) -> str:
    lines = code.split("\n")
    translated_lines = []

    for line in lines:
        stripped = line.lstrip()
        indent = line[:len(line) - len(stripped)]

        if stripped.startswith("vibe "):
            stripped = stripped.replace("vibe ", "", 1)

        for gez, py in SYNTAX_MAP.items():
            stripped = stripped.replace(gez, py)

        translated_lines.append(indent + stripped)

    user_code = "\n".join(translated_lines).strip()

    return ARRAY_HELPERS + "\n\n" + user_code
