def removeKdigits(num: str, k: int) -> str:
    stack = []
    
    for digit in num:
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    
    # If still need to remove
    while k > 0 and stack:
        stack.pop()
        k -= 1
    
    # Build result
    result = "".join(stack).lstrip("0")
    
    return result if result else "0"


# Example Run
print(removeKdigits("1432219", 3))  # Output: "1219"
