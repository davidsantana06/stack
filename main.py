from stack import Stack


# MSG FORMATTER ------------------------------------------------------
def __get_msg(index):
    msg = ''

    match(index):
        case 0:
            msg = '| --------------------- |' + \
                '\n|     ..: STACK :..     |' + \
                '\n| Select one operation: |' + \
                '\n| > 1. Push item        |' + \
                '\n| > 2. Pop item         |' + \
                '\n| > 3. Peek item        |' + \
                '\n| > 4. Search item      |' + \
                '\n| > 5. Fill rate        |' + \
                '\n| > 6. Print stack      |' + \
                '\n| > 0. End app.         |' + \
                '\n| --------------------- |'
        case 1:
            msg = '+-+-+-+-+-+-' + \
                '\n+ GOOD BYE -' + \
                '\n+-+-+-+-+-+-'
        case 2:
            msg = '| INVALID INPUT! |'

    if (index < 2):
        return msg
    else:
        hyphens = ('-' * (len(msg) - Stack.MARKER_LEN))
        return ('| {0} |\n{1}\n| {2} |'.format(hyphens, msg, hyphens))
# --------------------------------------------------------------------


def main():
    stack = Stack(10)
    end_app = False

    while not end_app:
        print(__get_msg(0))
        operation = input('_Operation: ')

        result = ''
        match(operation):
            case '0':
                end_app = True
                result = __get_msg(1)
            case '1':
                item = input('_Item: ')
                result = stack.push(item)
            case '2':
                result = stack.pop()
            case '3':
                result = stack.peek()
            case '4':
                item = input('_Item: ')
                result = stack.search(item)
            case '5':
                result = stack.fill_rate()
            case '6':
                result = str(stack)
            case _:
                result = __get_msg(2)

        print('\n{0}\n'.format(result))


main()
