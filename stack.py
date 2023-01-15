class Stack:
    # CONSTANT -------------
    MARKER_LEN = len('|  |')
    # ----------------------

    # CONSTRUCTOR -----------
    def __init__(self, size):
        self.__stack = []
        self.__size = size
    # -----------------------

    # AUXILIARY METHODS -------------------------
    def is_full(self):
        return (len(self.__stack) == self.__size)

    def is_empty(self):
        return (len(self.__stack) == 0)
    # -------------------------------------------

    # PUSH -------------------------------
    def push(self, item):
        result = ''

        if (not self.is_full()):
            self.__stack.append(item)
            result = self.__get_msg(7, '')
        else:
            result = self.__get_msg(5, '')

        return result
    # ------------------------------------

    # POP ----------------------------------------------------
    def pop(self):
        result = ''

        if (not self.is_empty()):
            pop_item = self.__stack.pop(len(self.__stack) - 1)
            result = self.__get_msg(0, pop_item)
        else:
            result = self.__get_msg(6, '')

        return result
    # --------------------------------------------------------

    # PEEK --------------------------------------------------
    def peek(self):
        result = ''

        if (not self.is_empty()):
            peek_item = self.__stack[(len(self.__stack) - 1)]
            result = self.__get_msg(1, peek_item)
        else:
            result = self.__get_msg(6, '')

        return result
    # -------------------------------------------------------

    # SEARCH -----------------------------------------
    def search(self, item):
        result = ''

        if (not self.is_empty()):
            item_index = ''

            for index in range(len(self.__stack)):
                if (self.__stack[index] == item):
                    item_index = index
                    break

            if (item_index != ''):
                result = self.__get_msg(2, item_index)
            else:
                result = self.__get_msg(6, '')
        else:
            result = self.__get_msg(6, '')

        return result
    # ------------------------------------------------

    # FILL RATE ------------------------------------------------------
    def fill_rate(self):
        fill_rate = '{0} / {1}'.format(len(self.__stack), self.__size)
        return self.__get_msg(3, fill_rate)
    # ----------------------------------------------------------------

    # TO STRING --------------------------------------------
    def __str__(self):
        items = '('

        if (not self.is_empty()):
            for index in range(len(self.__stack)):
                if (index + 1) < len(self.__stack):
                    items += str(self.__stack[index]) + ', '
                else:
                    items += str(self.__stack[index])

        return self.__get_msg(4, (items + ')'))
    # ------------------------------------------------------

    # MSG FORMATTER --------------------------------------------------
    def __get_msg(self, id, item):
        msg = ''

        if (item != ''):
            match (id):
                case 0:
                    msg = '| POP: {0} |'.format(item)
                case 1:
                    msg = '| PEEK: {0} |'.format(item)
                case 2:
                    msg = '| ITEM IS IN INDEX {0} |'.format(item)
                case 3:
                    msg = '| FILL RATE: {0} |'.format(item)
                case 4:
                    msg = '| STACK: {0} |'.format(item)
        else:
            match (id):
                case 5:
                    msg = '| STACK IS FULL! |'
                case 6:
                    msg = '| STACK IS EMPTY! |'
                case 7:
                    msg = '| ITEM SUCCESSFULLY ADDED! |'
                case 8:
                    msg = '| ITEM IS NOT IN STACK! |'

        hyphens = ('-' * (len(msg) - self.MARKER_LEN))
        return ('| {0} |\n{1}\n| {2} |'.format(hyphens, msg, hyphens))
    # ----------------------------------------------------------------
