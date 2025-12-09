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
python eratosthenes.py --count-only
```

Key options:
- `--version / -v`: Show the version number and exit.
- `--count-only / -c`: show just how many primes were found.
- `--format / -f`: pick `plain` (default), `json`, or `csv`. JSON mode routes prompts/errors to stderr so stdout stays machine-friendly; CSV prints comma-separated primes followed by the count.

While in the interactive loop you can adjust options on the fly:
- `/format <plain|json|csv>` or `/f <option>`: switch output format.
- `/count-only <on|off>` or `/c <on|off>`: toggle whether the prime list is shown.
- `/help` or `/h`: display the command summary.

Example output:
```
$ python eratosthenes.py
Enter an integer limit (exclusive): /h
Commands: /format or /f <plain|json|csv>, /count-only or /c <on|off>, /limit or /l <int>
Enter an integer limit (exclusive): /l 33
Primes: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
Total primes: 11
Enter an integer limit (exclusive): 33
Primes: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
Total primes: 11
Enter an integer limit (exclusive): ^C
Are you sure you want to go? (y/n): y
Goodbye!
```
