
THREE60 Energy `rushmore-tools`
================================
[![Build Status](https://github.com/THREE60-Energy/rushmore-tools/workflows/release/badge.svg)](https://github.com/THREE60-Energy/rushmore-tools/actions)
[![codecov](https://codecov.io/gh/THREE60-Energy/rushmore-tools/branch/main/graph/badge.svg)](https://codecov.io/gh/THREE60-Energy/rushmore-tools)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

The `rushmore-tools` package is a collection of tools developed for handling Rushmore Performance Review data developed by THREE60 Energy Norway.

Overview
================================
The collection contains utilities:
- RushmoreExtractor


## Development environment

We use [poetry](https://python-poetry.org) to manage dependencies and to administrate virtual environments. To develop
`rushmore-tools`, follow the following steps to set up your local environment:

 1. [Install poetry](https://python-poetry.org/docs/#installation) if you haven't already.

 2. Clone repository:
    ```
    $ git clone git@github.com:THREE60-Energy/rushmore-tools.git
    ```
 3. Move into the newly created local repository:
    ```
    $ cd rushmore-tools
    ```
 4. Create virtual environment and install dependencies:
    ```
    $ poetry install
    ```

### Code requirements

All code must pass [black](https://github.com/ambv/black) and [isort](https://github.com/timothycrosley/isort) style
checks to be merged. It is recommended to install pre-commit hooks to ensure this locally before commiting code:

```
$ poetry run pre-commit install
```

Each public method, class and module should have docstrings. Docstrings are written in the [Google
style](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings).

### Testing

To produce Coverage tests, run the following commands
```
$ poetry run coverage run -m pytest
$ poetry run coverage xml
```