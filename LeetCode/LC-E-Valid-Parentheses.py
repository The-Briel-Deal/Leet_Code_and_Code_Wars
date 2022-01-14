# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.


# Example 1:

# Input: s = "()"
# Output: true

# Example 2:

# Input: s = "()[]{}"
# Output: true

# Example 3:

# Input: s = "(]"
# Output: false


# Constraints:

#     1 <= s.length <= 104
#     s consists of parentheses only '()[]{}'.


from traceback import print_tb
from sqlalchemy import true


class Solution:
    def isValid(self, s: str) -> bool:
        map = {")": "(", "}": "{", "]": "["}
        queue = list(s)
        stack = []
        for current in queue:
            if current in ["(", "[", "{"]:
                stack.append(current)
            elif stack != []:
                if map[current] != stack.pop():
                    return False
            else:
                return False
        if stack != []:
            return False
        return True


solution = Solution()
print(")(){} is " + f"{solution.isValid(')(){}')}")
# print("(] is " + f"{solution.isValid('(]')}")
# print("()[]{} is " + f"{solution.isValid('()[]{}')}")
