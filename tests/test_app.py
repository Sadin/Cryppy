# test cases for Cryppy
from __future__ import annotations

import pytest

import cryppy


@pytest.mark.parametrize(
    ('input_string', 'expected'),
    (
        pytest.param('ETH USD', ('ETH', 'USD'),
                     id='coin to regular currency'),
        pytest.param('USD EUR', ('USD', 'EUR'),
                     id='reg currency to reg currency'),
        pytest.param('ETH USD Additional text for edge case',
                     ('ETH', 'USD'), id='trailing extra text')
    )
)
def test_parse_currency_pair(input_string: str, expected: tuple):
    assert cryppy.parse_currency_pair(input_string) == expected
