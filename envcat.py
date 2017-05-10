#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals, print_function

import argparse
import os.path
import re


__version__ = '0.1.0'
ENV_KEY_RE = re.compile(r'^[a-z][a-z0-9_]*$', flags=re.IGNORECASE)


# borrowed from https://github.com/willkg/everett/
def parse_env_file(envfile):
    """Parse the content of an iterable of lines as .env
    Return a dict of config variables.
    >>> parse_env_file(['DUDE=Abides'])
    {'DUDE': 'Abides'}
    """
    data = {}
    for line_no, line in enumerate(envfile):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if '=' not in line:
            raise RuntimeError('Env file line missing = operator (line %s)' % (line_no + 1))
        k, v = line.split('=', 1)
        k = k.strip()
        if not ENV_KEY_RE.match(k):
            raise RuntimeError(
                'Invalid variable name "%s" in env file (line %s)' % (k, (line_no + 1))
            )
        v = v.strip()
        data[k] = v

    return data


def get_env_vars(filename):
    if os.path.isfile(filename):
        with open(filename) as envfile:
            return parse_env_file(envfile)
    else:
        return {}


def get_unique_vars(filenames):
    data = {}
    for fn in filenames:
        data.update(get_env_vars(fn))

    return data


def get_env_vars_list(filenames):
    return ['%s=%s' % pair for pair in sorted(get_unique_vars(filenames).items())]


def env_vars_formatted(all_vars, oneline=False):
    sep = ' ' if oneline else '\n'
    return sep.join(all_vars)


def print_env_vars(all_vars, oneline=False):
    end = '' if oneline else '\n'
    print(env_vars_formatted(all_vars, oneline), end=end)


def main():
    parser = argparse.ArgumentParser(description='Merge env file values')
    parser.add_argument('files', metavar='FILE', nargs='+',
                        help='env file paths')
    parser.add_argument('--oneline', action='store_true', default=False,
                        help='Output the env variables on one line')
    args = parser.parse_args()
    print_env_vars(get_env_vars_list(args.files), args.oneline)


if __name__ == '__main__':
    main()
