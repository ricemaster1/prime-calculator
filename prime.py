import math

def is_prime(n):
    if n < 2:
        return False

    limit = int(math.sqrt(n))
    for i in range(2, limit + 1):
        if n % i == 0:
            return False
    
    return True

while True:
    try: 
        user_input = input("Enter an integer: ")
        try:
            _primes = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue
        primes = [n for n in range(_primes) if is_prime(n)]
        print(f"Primes: {primes}")
        print(f"Total primes: {len(primes)}")

    except KeyboardInterrupt:
        _leave = input("\nAre you sure you want to go? (y/n): ").strip().lower()
        if _leave == 'y':
            print("Goodbye!")
            break
        else:
            continue


