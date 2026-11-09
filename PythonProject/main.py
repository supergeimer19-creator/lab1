# main.py
import time
from decorators import time_it


@time_it
def heavy_calculation(n):
    """Simulates a heavy calculation loop."""
    total = 0
    for i in range(n):
        total += i ** 2
    return total


if __name__ == "__main__":
    print("Starting program...")

    # Executing the decorated function
    result = heavy_calculation(1_000_000)
    print(f"Calculation result: {result}")