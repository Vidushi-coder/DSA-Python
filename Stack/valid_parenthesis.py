stack = []

s = input("Enter the parentheses: ")
print(s)


def push(element):
    stack.append(element)


def pop():
    if isEmpty():
        return None
    return stack.pop()


def peek():
    if isEmpty():
        return None
    return stack[-1]


def isEmpty():
    return len(stack) == 0


pairs = {
    ')': '(',
    '}': '{',
    ']': '['
}

valid = True

for i in s:

    if i in "({[":
        push(i)

    elif i in ")}]":

        if isEmpty():
            valid = False
            break

        elif peek() == pairs[i]:
            pop()

        else:
            valid = False
            break


if not isEmpty():
    valid = False


if valid:
    print("Valid Parentheses")
else:
    print("Invalid Parentheses")
