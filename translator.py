import re

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


def translate(code: str) -> str:
    lines = code.split("\n")
    translated_lines = []

    for line in lines:
        stripped = line.lstrip()
        indent = line[:len(line) - len(stripped)]

        # ✅ Handle vibe variable declaration
        if stripped.startswith("vibe "):
            stripped = stripped.replace("vibe ", "", 1)

        # Replace meme keywords
        for gez, py in SYNTAX_MAP.items():
            stripped = stripped.replace(gez, py)

        translated_lines.append(indent + stripped)

    return "\n".join(translated_lines)
