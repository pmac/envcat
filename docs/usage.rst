.. highlight:: shell

=====
Usage
=====

envcat is a CLI tool for mixing the content of one or more env files::

    $ envcat base.env local.env > mix.env

In this example values would be read from `base.env` and `local.env` in that order. Order is
important since the same key in `local.env` would override one from `base.env` in this order.
If any of the specified files do not exist they are silently ignored, making this a good tool
for searching an optionally including values from files that may exist.

The default output format is that of an `env file <https://ddollar.github.io/foreman/#ENVIRONMENT>`_ (like foreman uses), but you can also have it
output the values space separated on a single line using the `--oneline` flag::

    $ envcat --help
    usage: envcat.py [-h] [--oneline] [FILE [FILE ...]]

    Merge env file values

    positional arguments:
      FILE        env file paths

    optional arguments:
      -h, --help  show this help message and exit
      --oneline   Output the env variables on one line
      --version   Output the version and exit

This tool can be particularly useful when passing values to other CLI tools::

    #!/bin/bash

    ENV_VALUES=( $(envcat base.env ${REGION}.env local.env) )
    # add a value from the script
    ENV_VALUES+=( "OTHER_VALUE=$OTHER_ENV_VAR" )
    heroku config:set -a my-app "${ENV_VALUES[@]}"

Docker
------

You can also easily use this tool via docker if you don't want to install it locally. Just add the following
to your project as a script called `envcat` and it'll work just like the tool itself::

    #!/bin/bash

    docker run --rm -v $(pwd):/envcat mozmeao/envcat:latest "$@"

Then you can use it like normal::

    $ ./envcat --version
    0.1.0
