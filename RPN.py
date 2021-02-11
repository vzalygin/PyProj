import sys


def is_true(comp1, comp2, action):
    if action == '=' and comp1 == comp2:
        return True
    elif action == '>' and comp1 > comp2:
        return True
    elif action == '<' and comp1 < comp2:
        return True
    elif action == '>=' and comp1 >= comp2:
        return True
    elif action == '<=' and comp1 <= comp2:
        return True
    else:
        return False


def is_num(a):
    try:
        int(a)
        return True
    except:
        return False


def is_condition(a):
    if a == '<' or a == '<=' or a == '=' or a == '>=' or a == '>':
        return True
    else:
        return False


def try_parse_int(a):
    try:
        return int(a)
    except:
        return a


def is_empty(stack):
    try:
        stack[0]
        return False
    except:
        return True


def reverse(stack):
    for i in range(len(stack) - 1, -1, -1):
        stack.append(stack.pop(i))


def main():
    dictionary = {}
    queue = [try_parse_int(x) for x in sys.stdin.read().split()]

    stack_of_commands = []
    stack_of_operands = []
    while not is_empty(queue):
        stack_of_commands.append(queue.pop())

    while not is_empty(stack_of_commands):
        item = stack_of_commands.pop()
        if is_num(item) or is_condition(item):
            stack_of_operands.append(item)
        elif item == '+':
            stack_of_commands.append(stack_of_operands.pop() + stack_of_operands.pop())
        elif item == '-':
            stack_of_commands.append(-stack_of_operands.pop() + stack_of_operands.pop())
        elif item == '*':
            stack_of_commands.append(stack_of_operands.pop() * stack_of_operands.pop())
        elif item == '.':
            print(stack_of_operands.pop(), end=' ')
        elif item == 'dup':
            stack_of_operands.append(stack_of_operands[-1])
        elif item == 'drop':
            stack_of_operands.pop()
        elif item == 'take':
            stack_of_operands.append(stack_of_operands.pop(-stack_of_operands.pop() - 1))
        elif item == '[':
            a = []
            item = stack_of_commands.pop()
            n = 0
            while item != ']' or n != 0:
                if item == '[':
                    n += 1
                if item == ']':
                    n -= 1
                a.append(item)
                item = stack_of_commands.pop()
            stack_of_operands.append(a)
        elif item == '!':
            item = stack_of_operands.pop()
            for n in range(len(item)-1, -1, -1):
                stack_of_commands.append(item[n])
        elif item == '?':
            case_false = stack_of_operands.pop()
            case_true = stack_of_operands.pop()
            condition = stack_of_operands.pop()
            comp2 = stack_of_operands.pop()
            comp1 = stack_of_operands.pop()
            if is_true(comp1, comp2, condition):
                stack_of_operands.append(case_true)
            else:
                stack_of_operands.append(case_false)
            stack_of_commands.append('!')
        elif item[0] == ':':
            if len(item) > 1:
                dictionary[item[1:]] = stack_of_operands.pop()
        elif item in dictionary:
            stack_of_operands.append(dictionary[item])
            stack_of_commands.append('!')
        elif item not in dictionary:
            print('ERROR', item)
            return


main()
