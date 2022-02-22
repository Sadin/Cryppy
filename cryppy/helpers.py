from __future__ import annotations


def parse_currency_pair(input_string: str) -> tuple:
    return tuple(input_string.split(' ', 1))
