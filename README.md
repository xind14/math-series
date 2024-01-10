# Lab: Class 2 - Modules and Testing

## Author: Xin Deng, chatGPT

## Links and Resources

- chatGPT on what the docstrings were

## Overview - math-series

The Fibonacci Series is a numeric series starting with the integers 0 and 1. In this series, the next integer is determined by summing the previous two. This gives us:

```
0, 1, 1, 2, 3, 5, 8, 13, ...
```

**Note:** When asking for the nth number in series presume starting at zero.

`fibonacci(0) == 0, fibonacci(1) == 1, fibonacci(2) == 1, etc.`

The Lucas Numbers are a related series of integers that start with the values 2 and 1 rather than 0 and 1. The resulting series looks like this:

```
2, 1, 3, 4, 7, 11, 18, 29, ...
```


## Feature Tasks and Requirements

- Create a local git repo with the root folder named math-series.
- Create a new repository named math-series.
- Link your local and remote repositories.

1. Create a module `series.py`.
2. Add a file `test_series.py` to your repository. Use TDD practices. Write tests first, then implement code. Make small changes with many cycles of Red-Green-Refactor. This is not an overly long assignment, so take the time to do the testing right.
3. Create a function called `fibonacci` in `series.py`.
    - The function should have one parameter `n`.
    - The function should return the nth value in the Fibonacci series.
    - You may implement the function using recursion or iteration.
4. In your `series.py` module, add a new function `lucas` that returns the nth value in the Lucas numbers.
    - Again, you may use recursion or iteration.
5. Add a third function called `sum_series` with one required parameter and two optional parameters.
    - The required parameter will determine which element in the series to print.
    - The two optional parameters will have default values of 0 and 1 and will determine the first two values for the series to be produced.
    - Calling this function with no optional parameters will produce numbers from the Fibonacci series.
    - Calling it with the optional arguments 2 and 1 will produce values from the Lucas numbers. Other values for the optional parameters will produce other series.
    - You may use recursion or iteration.

## Setup

### Creating Project

```bash
mkdir example-lab
cd example-lab
touch README.md
```

### Create virtual environment

```bash
python3 -m venv .venv
```

### Activate virtual environment

#### Mac/Linux

```bash
source .venv/bin/activate
```

### Git

#### On Local System

#### Initialize local Git repository

```bash
git init
touch .gitignore
```

Add `.venv` folder to `.gitignore`

```bash
git add .
git commit -m "first commit"
```

#### On GitHub site

- Create an EMPTY repository `example-lab` on GitHub. 
  - DO NOT initialize with README, license, or gitignore. Those will be added soon.
  - The next screen will have a "Quick Setup" section with a URL available to copy. Copy it ;)

#### On Local System (again)

```bash
git remote add origin the_url_you_copied_that_ends_with_git
git push -u origin main
```

#### Create modules and scripts

- mkdir example_lab

- touch example_lab/example_script.py


#### Install packages

```For example:

pip install favorite-library

Record package dependencies
pip freeze > requirements.txt

Should result in this file tree:

└── example-lab
    ├── README.md
    ├── requirements.txt
    └── example_lab
        └── example_script.py

```      

### Tests

Many labs will require automated testing. If your lab requires it then install `pytest` or `pytest-watch`.

`pip install pytest` # or pytest-watch

`pip freeze > requirements.txt`

`touch tests/__init__.py `(Note: 2 underscores on both sides.)

`touch tests/test_example.py`

Should result in a file tree like this:

```└── example-lab
    ├── README.md
    ├── requirements.txt
    ├── example_lab
    │   └── example_script.py
    └── tests
        ├── __init__.py
        └── test_example.py
```