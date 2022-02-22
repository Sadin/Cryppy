from __future__ import annotations


def parse_currency_pair(input_string: str) -> tuple:
    currency_pair = input_string.strip()
    currency_pair = currency_pair.split(' ', maxsplit=2)
    if len(currency_pair) > 2:
        currency_pair.pop()

    return tuple(currency_pair)
