import constants


def calc_func(val1, val2, operation):
    if operation == constants.ADD:
        return val1 + val2
    elif operation == constants.SUB:
        return val1 - val2
    elif operation == constants.MUL:
        return val1 * val2
    elif operation == constants.DIV:
        return val1 / val2
    else:
        raise Exception("Incorrect operation")
