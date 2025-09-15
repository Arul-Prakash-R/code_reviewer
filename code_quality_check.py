import math   # Unused import (F)
import os     # Unused import (F)

def BadFunction(userName):   # Inconsistent naming conventions (F)
    count=0  # Poor formatting: missing spaces (F)

    TempValue = 42  # Unused variable (F)

    # Inefficient loop (F) - nested loop with O(n^2) for no reason
    for i in range(10):
        for j in range(10):
            print(i+j)

    # Bug before runtime (possible TypeError if userName is not str)
    print("Hello " + userName)   # ❌ No type safety

    # Dead code (F): function never used
    def helper_function():
        return "not used"

    return count


# Accessibility-like issues (simulated for Python CLI context)
def render_ui():
    print("<img src='image.png'>")   # Missing alt text (F)
    print("<a style='color:#ccc'>Low contrast link</a>")  # Contrast issue (F)
    print("<input>")  # Missing keyboard accessibility attributes (F)


# Unnecessary re-render (simulated) (F)
def calculate():
    for i in range(5):
        result = [x*2 for x in range(1000000)]  # Big list recreated unnecessarily
        print(sum(result))


# Dead code (F) - function never called
def unused_function():
    return "I am never used"


# Linting errors (F): badly indented, inconsistent spacing
def badIndent():
 print("bad indent")  # <- wrong indentation


# Test coverage issue (F): No test provided for this function
def critical_logic(a, b):
    if a > b:
        return a - b
    else:
        return b - a


# Potential large bundle / bloat simulation (F)
big_data = ["x" * 1000 for _ in range(10000)]  # memory bloat
jh
