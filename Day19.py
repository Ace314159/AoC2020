from collections import deque


def one(lines):
    rules, messages = lines.split('\n\n')
    parsed_rules = {}
    for rule in rules.splitlines():
        num, rule = rule.strip().split(': ')
        num = int(num)
        if '"' in rule:
            parsed_rules[num] = rule[1]
        else:
            rule = rule.split(' | ')
            parsed_rules[num] = [list(map(int, sub_rule.split(' '))) for sub_rule in rule]

    def check_rule(message, rule):
        rule = parsed_rules[rule]
        if type(rule) == str:
            if message.popleft() == rule:
                return [message]
            else:
                return []
        else:
            working_messages = []
            for any_rule in rule:
                temp_working = [message.copy()]
                for sub_rule in any_rule:
                    new_temp_working = []
                    for m in temp_working:
                        possible = check_rule(m, sub_rule)
                        if possible:
                            new_temp_working.extend(possible)
                    temp_working = new_temp_working
                working_messages.extend(temp_working)
            return working_messages

    ans = 0
    for message in messages.splitlines():
        message = deque(message)
        out = check_rule(message, 0)
        if any([len(i) == 0 for i in out]):
            ans += 1
    return ans


def two(lines):
    rules, messages = lines.split('\n\n')
    parsed_rules = {}
    rules = rules.splitlines()
    rules.append('8: 42 | 42 8')
    rules.append('11: 42 31 | 42 11 31')
    for rule in rules:
        num, rule = rule.strip().split(': ')
        num = int(num)
        if '"' in rule:
            parsed_rules[num] = rule[1]
        else:
            rule = rule.split(' | ')
            parsed_rules[num] = [list(map(int, sub_rule.split(' '))) for sub_rule in rule]

    def check_rule(message, rule):
        rule = parsed_rules[rule]
        if type(rule) == str:
            if len(message) > 0 and message.popleft() == rule:
                return [message]
            else:
                return []
        else:
            working_messages = []
            for any_rule in rule:
                temp_working = [message.copy()]
                for sub_rule in any_rule:
                    new_temp_working = []
                    for m in temp_working:
                        possible = check_rule(m, sub_rule)
                        if possible:
                            new_temp_working.extend(possible)
                    temp_working = new_temp_working
                working_messages.extend(temp_working)
            return working_messages

    ans = 0
    for message in messages.splitlines():
        message = deque(message)
        out = check_rule(message, 0)
        if any((len(i) == 0 for i in out)):
            ans += 1
    return ans


if __name__ == '__main__':
    with open('inputs/19.txt') as f:
        lines = f.read()
    print(one(lines))
    print(two(lines))
