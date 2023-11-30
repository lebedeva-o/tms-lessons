import pytest
import random

@pytest.fixture
def age():
    random_age = random.randint(0, 100)
    print(f"\nRandom age is {random_age}")
    yield random_age
    print("\nDeleting random age... Done")
