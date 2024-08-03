# -*- coding: utf-8 -*-
'''
Created on Mon Jul 22 13:20:11 2024

@author: Paul Baxter
'''


# split a number into groups of 3
def number_split(number: int) -> list:
    groups: list = []
    str_num: str = format(number)
    str_len: int = len(str_num)

    # split numbers into groups of 3
    while str_len >= 3:
        group = str_num[str_len - 3: str_len]
        groups.insert(0, group)
        str_num = str_num[0:-3]
        str_len -= 3
    if str_len > 0:
        groups.insert(0, str_num[0: str_len])
    return groups


# format a number with commas
def format_number(number: int) -> str:
    out: str = ''
    groups: list = number_split(number)

    for group in range(len(groups) - 1):
        out += groups[group] + ','

    out += groups[len(groups) - 1]
    return out


# format a number to words
def number_to_words(number: int) -> str:
    ONES = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    TEENS = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    TENS = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    GROUP_NAMES = ['Hundred', 'Thousand', 'Million', 'Billion', 'Trillion', 'Quadrillion', 'Quintillion', 'Sextillion', 'Septillion', 'Octillion', 'Nonillion', 'Decillion', 'Undecillion', 'Duodecillion', 'Tredecillion', 'Quattuordecillion', 'Quindecillion', 'Sexdecillion', 'Septendecillion', 'Octodecillion', 'Novemdecillion', 'Vigintillion']

    ORD_ZERO: int = ord('0')

    out: str = ''
    groups: list = number_split(number)

    # get index for group name (hundreds thousands etc)
    group_name_index: int = len(groups) - 1

    group: str
    sp: str = ''

    # iterate each group
    for group in groups:
        group_len: int = len(group)
        out_start: str = out
        include_ones: bool = True

        # hundreds
        if group_len > 2:
            hundred_index = ord(group[0]) - ORD_ZERO
            if hundred_index > 0:
                if len(out) > 0:
                    sp = ' '
                out += sp + ONES[hundred_index] + ' ' + GROUP_NAMES[0]

        # tens
        if group_len > 1:
            adjust: int = 3 - group_len
            ten_index: int = ord(group[1 - adjust]) - ORD_ZERO

            if ten_index != 0:
                if len(out) > 0:
                    sp = ' '

                # check for teens
                if ten_index == 1:
                    ten_index = ord(group[2 - adjust]) - ORD_ZERO
                    out += sp + TEENS[ten_index]
                    include_ones = False
                else:
                    out += sp + TENS[ten_index]

        # ones
        if include_ones:
            one_index = ord(group[group_len - 1]) - ORD_ZERO
            if one_index != 0 or len(out) == 0:
                if len(out) > 0:
                    sp = ' '
                out += sp + ONES[one_index]

        # name of group
        if len(out) > 0 and out_start != out and group_name_index != 0:
            out += ' ' + GROUP_NAMES[group_name_index]

        group_name_index -= 1

    return out


def main() -> None:
    num = 87696123456123456456786789
    print(format_number(num))
    print(number_to_words(num))


# call main
if __name__ == '__main__':
    main()
