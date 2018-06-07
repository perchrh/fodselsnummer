"""Functions for validation of Norwegian legal entities (organisasjonsnummer fra Enhetsregisteret)"""

import re

ORGNR_REGEX = re.compile(r'^\d{9}$')


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

    weights = [3, 2, 7, 6, 5, 4, 3, 2]
    digits = [int(d) for d in orgnr]
    product_sum = sum([x * y for x, y in zip(weights, digits[0:8])])
    control_digit = 11 - (product_sum % 11)
    if control_digit == 10:
        return False
    else:
        return control_digit == digits[-1]
