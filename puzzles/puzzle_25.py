import math

SNAFU_BASE = 5

def snafu_to_decimal(snafu):
    
    decimal_value = 0

    for i, snafu_digit in enumerate(reversed(snafu)):

        snafu_digit_value = get_snafu_value(snafu_digit)

        snafu_value = snafu_digit_value * (SNAFU_BASE ** i)

        decimal_value += snafu_value
    
    return decimal_value


class SnafuDigit:
    DIGIT_MINUS_ONE = '-'
    VALUE_MINUS_ONE = -1

    DIGIT_MINUS_TWO = '='
    VALUE_MINUS_TWO = -2

    DIGIT_TWO = '2'

def get_snafu_value(snafu_digit):

    if snafu_digit.isdigit():
        return int(snafu_digit)

    match snafu_digit:
        case SnafuDigit.DIGIT_MINUS_ONE:
            return SnafuDigit.VALUE_MINUS_ONE
        case SnafuDigit.DIGIT_MINUS_TWO:
            return SnafuDigit.VALUE_MINUS_TWO


def decimal_to_snafu(decimal):

    helper_digits = math.ceil( math.log (decimal, SNAFU_BASE))

    helper_snafu = SnafuDigit.DIGIT_TWO * helper_digits

    helper_decimal = snafu_to_decimal(helper_snafu)

    decimal_helper = decimal + helper_decimal

    snafu_helper = decimal_to_base(decimal_helper, SNAFU_BASE)

    snafu = reversed([snafu_minus_two(digit) if i < helper_digits else str(digit) for i, digit in enumerate(reversed(snafu_helper))])

    snafu_str = ''.join(snafu)

    return snafu_str


def decimal_to_base(n, b):
    if n == 0:
        return [0]
    
    digits = []

    while n:
        digits.append(int(n % b))
        n //= b

    return digits[::-1]   


def snafu_minus_two(snafu_digit):

    snafu_minus_two_value = snafu_digit - 2

    match snafu_minus_two_value:

        case -1:
            return SnafuDigit.DIGIT_MINUS_ONE
        case -2:
            return SnafuDigit.DIGIT_MINUS_TWO
    
    return str(snafu_minus_two_value)
























