import subprocess

# Function to run your program and get output
def run_test(board, move):
    process = subprocess.Popen(
        ["python", "Analysis-Algorithms\labs\lab1\lab1_assignment\sub1.py"], 
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    out, err = process.communicate(f"{board}\n{move}\n")
    return out.strip(), err.strip()

# Test cases: (board, move, expected)
# Expected is None if we just want to see what your code does
tests = [
    # Provided examples
    ("1857#3462", "LEFT",  "185#73462"),
    ("18573#462", "UP",    "18#735462"),
    ("78651#432", "DOWN",  "78651243#"),

    # Valid moves — blank in corners
    ("#12345678", "RIGHT", "1#2345678"),   # top-left corner
    ("#12345678", "DOWN",  "4123#5678"),   # top-left corner
    ("1234#5678", "UP",    "1#3425678"),   # middle top row
    ("1234#5678", "LEFT",  "12#435678"),   # middle top row
    ("12345678#", "LEFT",  "1234567#8"),   # bottom-right corner
    ("12345678#", "UP",    "1234567#8"),   # bottom-right -> up is invalid? depends on logic

    # Valid moves — blank in center
    ("123456#78", "LEFT",  "12345#678"),   # center moving left
    ("123456#78", "RIGHT", "1234567#8"),   # center moving right
    ("123456#78", "UP",    "1234#6578"),   # center moving up
    ("123456#78", "DOWN",  "12345786#"),   # center moving down

    # Valid moves — blank in edges (not corners)
    ("12#345678", "LEFT",  "1#2345678"),   # top edge
    ("12#345678", "RIGHT", "123#45678"),   # top edge
    ("12534#678", "UP",    "125#43678"),   # middle edge
    ("12534#678", "DOWN",  "1253476#8"),   # middle edge

    # Invalid moves — tries to move off the board
    ("#12345678", "LEFT",  None),  # already at left edge
    ("#12345678", "UP",    None),  # already at top edge
    ("123#45678", "UP",    None),  # at top edge
    ("1234567#8", "RIGHT", None),  # at right edge
    ("12345678#", "DOWN",  None),

    # Edge cases — blank in top-left, trying UP or LEFT (should handle invalid move)
    ("#12345678", "UP",   None),
    ("#12345678", "LEFT", None),

    # Blank in top-right, trying RIGHT
    ("123#45678", "RIGHT", None),

    # Blank in bottom-left, trying DOWN or LEFT
    ("1234567#8", "DOWN", None),
    ("1234567#8", "LEFT", None),

    # Blank in bottom-right, trying RIGHT or DOWN
    ("12345678#", "RIGHT", None),
    ("12345678#", "DOWN", None),

    # Middle positions moving in all directions
    ("1234#5678", "UP",   None),
    ("1234#5678", "DOWN", None),
    ("1234#5678", "LEFT", None),
    ("1234#5678", "RIGHT", None),
]

# Run all tests
for board, move, expected in tests:
    result, err = run_test(board, move)
    print(f"Board: {board}, Move: {move}")
    if err:
        print(f"  Error: {err}")
    else:
        print(f"  Output: {result}")
        if expected is not None:
            print(f"  Expected: {expected} -> {'PASS' if result == expected else 'FAIL'}")
    print()
