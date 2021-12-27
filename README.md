<div align="center">

[![pypi](https://img.shields.io/pypi/v/argparse-range)](https://pypi.org/project/argparse-range/)
[![github](https://img.shields.io/static/v1?label=&message=github&color=grey&logo=github)](https://github.com/aatifsyed/argparse-range)

</div>

# `argparse-range`
Easily check that an argument is within a range for argparse

Use it like this:
```python
>>> from argparse import ArgumentParser, ArgumentTypeError
>>> from argparse_range import range_action
>>> parser = ArgumentParser()
>>> _ = parser.add_argument("rangedarg", action=range_action(0, 10), help="An argument")
>>> args = parser.parse_args(["0"])
>>> args.rangedarg
0
>>> parser.parse_args(["20"])
Traceback (most recent call last):
    ....
argparse.ArgumentTypeError: Invalid choice: 20 (must be in range 0..=10)

```

## Features
### Helptext is added transparently
```text
foo.py --help

usage: foo.py [-h] rangedarg

positional arguments:
  rangedarg   An argument (must be in range 0..=10)

optional arguments:
  -h, --help  show this help message and exit
```

### Infers type by default
```python
>>> from argparse import ArgumentParser
>>> from argparse_range import range_action
>>> parser = ArgumentParser()
>>> _ = parser.add_argument("intarg", action=range_action(0, 10))
>>> _ = parser.add_argument("floatarg", action=range_action(25.0, 40.0))
>>> _ = parser.add_argument("explicit", action=range_action(25.0, 40.0), type=int)
>>> args = parser.parse_args(["5", "30", "30"])
>>> assert isinstance(args.intarg, int)
>>> assert isinstance(args.floatarg, float)
>>> assert isinstance(args.explicit, int)

```

### Handles optional arguments and defaults just like normal parsing
```python
>>> from argparse import ArgumentParser
>>> from argparse_range import range_action
>>> parser = ArgumentParser()
>>> _ = parser.add_argument("--maybe", action=range_action(0, 10), nargs="?")
>>> parser.parse_args([])
Namespace(maybe=None)
>>> parser.parse_args(["--maybe"])
Namespace(maybe=None)
>>> parser.parse_args(["--maybe", "5"])
Namespace(maybe=5)
>>> parser.parse_args(["--maybe", "20"])
Traceback (most recent call last):
    ....
argparse.ArgumentTypeError: Invalid choice: 20 (must be in range 0..=10)

```

### Handles multiple arguments just like normal parsing
```python
>>> from argparse import ArgumentParser
>>> from argparse_range import range_action
>>> parser = ArgumentParser()
>>> _ = parser.add_argument("many", action=range_action(0, 10), nargs="*")
>>> parser.parse_args([])
Namespace(many=[])
>>> parser.parse_args(["5"])
Namespace(many=[5])
>>> parser.parse_args(["1", "2", "3", "4"])
Namespace(many=[1, 2, 3, 4])

```
