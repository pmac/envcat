#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_envcat
----------------------------------

Tests for `envcat` module.
"""
from textwrap import dedent

import envcat


def test_get_env_vars_list():
    vars = envcat.get_env_vars_list(['tests/dude.env'])
    assert vars == [
        'DUDE=True',
        'METHOD=abiding',
        'PAST_TIME=bowling',
    ]

    vars = envcat.get_env_vars_list(['tests/dude.env', 'tests/donnie.env'])
    assert vars == [
        'DONNIE=True',
        'DUDE=True',
        'METHOD="out of element"',
        'PAST_TIME=bowling',
    ]

    vars = envcat.get_env_vars_list(['tests/walter.env', 'tests/donnie.env', 'tests/dude.env'])
    assert vars == [
        'DONNIE=True',
        'DUDE=True',
        'METHOD=abiding',
        'NAM=True',
        'PACIFISM=dabbled',
        'PAST_TIME=bowling',
        'WALTER=True'
    ]


def test_get_env_vars_formatted():
    vars = [
        'DONNIE=True',
        'DUDE=True',
        'METHOD="out of element"',
        'PAST_TIME=bowling',
    ]
    expected = dedent("""\
        DONNIE=True
        DUDE=True
        METHOD="out of element"
        PAST_TIME=bowling""")
    assert envcat.env_vars_formatted(vars, oneline=False) == expected

    expected = 'DONNIE=True DUDE=True METHOD="out of element" PAST_TIME=bowling'
    assert envcat.env_vars_formatted(vars, oneline=True) == expected
