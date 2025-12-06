# Python Prime Enumerator

Simple interactive CLI that enumerates every prime below an integer you provide. It uses a square-root bounded trial division (`is_prime`) defined in `prime.py`, so it stays easy to understand and portable.

## Requirements
- Python 3.8+ (only uses stdlib `math`)

## Running the script
```bash
cd deploy/python
python prime.py
```

You will be prompted for an integer upper bound. The script prints the list of all primes less than that number and the total count. Non-integer input triggers a friendly validation message. Press `Ctrl+C` to exit; you will be asked to confirm before quitting.

### Example session
```
Enter an integer: 20
Primes: [2, 3, 5, 7, 11, 13, 17, 19]
Total primes: 8
Enter an integer: ^C
Are you sure you want to go? (y/n): y
Goodbye!
```

## Implementation Notes
- `is_prime(n)` short-circuits for numbers < 2 and only tests divisors up to `sqrt(n)`.
- The generator comprehension `[n for n in range(_primes) if is_prime(n)]` keeps the script compact; swap in a sieve if you need better performance for large upper bounds.
