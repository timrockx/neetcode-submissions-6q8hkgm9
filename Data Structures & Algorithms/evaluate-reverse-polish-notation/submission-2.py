class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for t in tokens:
            if t in ['+', '-', '*', '/']:
                val1 = stack.pop()
                val2 = stack.pop()

                if t == '+':
                    res = val2 + val1
                elif t == '-':
                    res = val2 - val1
                elif t == '*':
                    res = val2 * val1
                else:
                    res = int(val2 / val1)
                    print(val2, val1, res)

                stack.append(res)

            else:
                stack.append(int(t))

        return stack.pop()
        