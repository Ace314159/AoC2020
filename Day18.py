from collections import deque
import operator


ops = {'+': operator.add, '*': operator.mul}


def one(lines):
    def eval_paren(expr):
        token = expr.popleft()
        count = token.count('(')
        levels_deep = count
        sub_expr = deque([token[1:]])
        while levels_deep > 0:
            token = expr.popleft()
            if '(' in token:
                count = token.count('(')
                levels_deep += count
            elif ')' in token:
                count = token.count(')')
                levels_deep -= count
                if levels_deep == 0:
                    token = token[:-1]
            sub_expr.append(token)
        return int(evaluate(sub_expr))

    def evaluate(expr):
        if len(expr) == 1:
            return expr.pop()

        if '(' in expr[0]:
            first_val = eval_paren(expr)
        else:
            first_val = int(expr.popleft())

        op = ops[expr.popleft()]

        if '(' in expr[0]:
            second_val = eval_paren(expr)
        else:
            second_val = int(expr.popleft())
        expr.appendleft(str(op(first_val, second_val)))
        return evaluate(expr)

    ans = 0
    for line in lines:
        ans += int(evaluate(deque(line.split(' '))))

    return ans


def two(lines):
    def eval_paren(expr):
        token = expr.popleft()
        count = token.count('(')
        levels_deep = count
        sub_expr = deque([token[1:]])
        while levels_deep > 0:
            token = expr.popleft()
            if '(' in token:
                count = token.count('(')
                levels_deep += count
            elif ')' in token:
                count = token.count(')')
                levels_deep -= count
                if levels_deep == 0:
                    token = token[:-1]
            sub_expr.append(token)
        return int(evaluate(sub_expr))

    def evaluate(expr):
        if len(expr) == 1:
            return expr.pop()

        if '(' in expr[0]:
            first_val = eval_paren(expr)
        else:
            first_val = int(expr.popleft())

        if len(expr) == 0:
            return first_val
        op = expr.popleft()

        if op == '*':
            second_val = int(evaluate(expr))
        elif '(' in expr[0]:
            second_val = eval_paren(expr)
        else:
            second_val = int(expr.popleft())

        op = ops[op]
        expr.appendleft(str(op(first_val, second_val)))
        return evaluate(expr)

    ans = 0
    for line in lines:
        ans += int(evaluate(deque(line.split(' '))))

    return ans


if __name__ == '__main__':
    with open('inputs/18.txt') as f:
        lines = f.read().splitlines()
    print(one(lines))
    print(two(lines))
