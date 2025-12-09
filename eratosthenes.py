import argparse
import json
from math import isqrt
from typing import Any, Dict, List

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

def print_results(primes: List[int], *, count_only: bool = False, fmt: str = "plain") -> None:
    count = len(primes)

    if fmt == "json":
        payload: Dict[str, Any] = {"count": count}
        if not count_only:
            payload["primes"] = primes
        print(json.dumps(payload))
        return

    if count_only:
        print(f"Total primes: {count}")
    else:
        print(f"Primes: {primes}")
        print(f"Total primes: {count}")

def run_interactive(*, count_only: bool = False, fmt: str = "plain") -> None:
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

            print_results(primes, count_only=count_only, fmt=fmt)

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

    parser.add_argument(
        "-f",
        "--format",
        choices=["plain", "json"],
        default="plain",
        help="Output format: 'plain' for human-readable text, 'json' for JSON output.",
    )

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="eratosthenes 1.0.0",
        help="Show the version number and exit.",
    )
    return parser.parse_args()

def main() -> None:
    args = parse_args()
    if args.limit is None:
        run_interactive(count_only=args.count_only, fmt=args.format)
        return

    try:
        primes = sieve_primes(args.limit)
    except ValueError as exc:
        print(f"Error: {exc}")
        return

    print_results(primes, count_only=args.count_only, fmt=args.format)

if __name__ == "__main__":
    main()


