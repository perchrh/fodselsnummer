"""Functions for validation of Norwegian legal entities (organisasjonsnummer fra Enhetsregisteret)"""

import re

ORGNR_REGEX = re.compile(r'^[8-9]\d{8}$')


def check_orgnr(orgnr):
    """
    Check if a number is a valid organisasjonsnummer.

    Only checks the control digits and the format (9 digits)

    Args:
        orgnr: A string containing the organisasjonsnummer to check
    Returns:
        True if it is a valid organisasjonsnummer, False otherwise.

    Ref https://web.archive.org/web/20171204223816/https://www.brreg.no/om-oss-nn/oppgavene-vare/registera-vare/om-einingsregisteret/organisasjonsnummeret/
    """
    if not ORGNR_REGEX.match(orgnr):
        return False

    digits = [int(d) for d in orgnr]
    control_digit = calculate_checksum_digit(digits[0:8])
    if control_digit == 10:
        return False
    else:
        return control_digit == digits[-1]


def calculate_checksum_digit(digits_without_checksum):
    weights = [3, 2, 7, 6, 5, 4, 3, 2]
    product_sum = sum([x * y for x, y in zip(weights, digits_without_checksum)])
    control_digit = 11 - (product_sum % 11)
    if control_digit == 11:
        control_digit = 0
    return control_digit


from random import randint


def generate_random_orgnr():
    while True:  # retry in case we get an illegal control digit (==10)
        random_number = randint(8 * 10 ** 7, (10 ** 8) - 1)
        random_number_string = '{:08}'.format(random_number)
        digits = [int(d) for d in random_number_string]

        control_digit = calculate_checksum_digit(digits)
        if control_digit == 10:
            continue

        return random_number_string + str(control_digit)
