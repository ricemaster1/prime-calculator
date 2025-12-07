import argparse
from math import isqrt
from typing import List

def sieve_primes(limit: int) -> List[int]:
    """Return every prime less than ``limit`` using the Sieve of Eratosthenes."""
    if limit < 0:
        raise ValueError("limit must be non-negative")
    if limit < 2:
        return []

    sieve = [True] * limit
    sieve[0] = False
    sieve[1] = False

    for candidate in range(2, isqrt(limit - 1) + 1):
        if sieve[candidate]:
            for multiple in range(candidate * candidate, limit, candidate):
                sieve[multiple] = False

    return [value for value, prime_flag in enumerate(sieve) if prime_flag]

def print_results(primes: List[int], count_only: bool = False) -> None:
    if count_only:
        print(f"Total primes: {len(primes)}")
    else:
        print(f"Primes: {primes}")
        print(f"Total primes: {len(primes)}")

def run_interactive(count_only: bool = False) -> None:
    """Keep prompting the user for a limit until they quit."""
    while True:
        try:
            user_input = input("Enter an integer limit (exclusive): ")
            try:
                limit = int(user_input)
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
                continue

            try:
                primes = sieve_primes(limit)
            except ValueError as exc:
                print(exc)
                continue

            print_results(primes, count_only=count_only)

        except KeyboardInterrupt:
            should_leave = input("\nAre you sure you want to go? (y/n): ").strip().lower()
            if should_leave == "y":
                print("Goodbye!")
                break

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Enumerate primes below the provided limit using the Sieve of Eratosthenes."
    )
    parser.add_argument(
        "-l",
        "--limit",
        type=int,
        help="Upper bound (exclusive) for the primes to enumerate. Defaults to interactive mode when omitted.",
    )
    parser.add_argument(
        "-c",
        "--count-only",
        action="store_true",
        help="Only print the count of primes, omitting the list itself.",
    )
    return parser.parse_args()

def main() -> None:
    args = parse_args()
    if args.limit is None:
        run_interactive(count_only=args.count_only)
        return

    try:
        primes = sieve_primes(args.limit)
    except ValueError as exc:
        print(f"Error: {exc}")
        return

    print_results(primes, count_only=args.count_only)

if __name__ == "__main__":
    main()


