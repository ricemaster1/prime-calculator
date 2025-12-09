# Python Prime Tools

This folder contains two small command-line utilities for listing primes below a number you choose.

## Requirements
- Python 3.8+ (only standard library modules)

## `prime.py` (minimal interactive tool)
- Trial-division checker suitable for quick exploration
- Prompts repeatedly until you confirm exit with `Ctrl+C` followed by `y`

Run it from this directory:
```bash
python prime.py
```

Sample session:
```
Enter an integer: 20
Primes: [2, 3, 5, 7, 11, 13, 17, 19]
Total primes: 8
Enter an integer: ^C
Are you sure you want to go? (y/n): y
Goodbye!
```

## `eratosthenes.py` (faster CLI with flags)
- Uses the Sieve of Eratosthenes for better performance on large limits
- Supports non-interactive mode plus an optional interactive loop

Basic usage:
```bash
# Interactive mode
python eratosthenes.py

# Direct run with flags
python eratosthenes.py --limit 1000 --count-only
```

Key options:
- `--version / -v`: Show the version number and exit.
- `--limit / -l`: upper bound (exclusive). Omit it to stay in the prompt.
- `--count-only / -c`: show just how many primes were found.
- `--format / -f`: pick `plain` (default) or `json`. Interactive prompts/errors move to stderr automatically in JSON mode so stdout remains machine-friendly.

While in the interactive loop you can switch formats without restarting by typing `/format plain` or `/format json` at any prompt.

Example output:
```
$ python eratosthenes.py --limit 20
Primes: [2, 3, 5, 7, 11, 13, 17, 19]
Total primes: 8

$ python eratosthenes.py --limit 1_000 --count-only
Total primes: 168

$ python eratosthenes.py
Enter an integer limit (exclusive): 50
Primes: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
Total primes: 15
Enter an integer limit (exclusive): ^C
Are you sure you want to go? (y/n): y
Goodbye!
```
