import pytest

from _etl_a9number_v4 import test_count_occurrences_in_text, test_profile

@pytest.mark.benchmark(min_rounds=100)
def test_benchmark_occurrences(benchmark):
    def occurences_runner():
        test_count_occurrences_in_text()  # Runs the test function
        return "Done"  # Ensure something is returned

    result = benchmark(occurences_runner)
    assert result == "Done"  # Validate execution

@pytest.mark.benchmark(min_rounds=100)
def test_benchmark_profile(benchmark):
    def profile_runner():
        test_profile()  # Runs the test function
        return "Done"

    result = benchmark(profile_runner)
    assert result == "Done"