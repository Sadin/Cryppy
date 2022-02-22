# test cases for Cryppy
from __future__ import annotations

import pytest

from app.py import parse_currency_pair


@pytest.mark.parametrize(
    ('input_string', 'expected'),
    (
        ('ETH USD', ('ETH', 'USD'))
    )
)
def test_parse_currency_pair(input_string: str, expected: tuple):
    assert parse_currency_pair(input_string) == expected
