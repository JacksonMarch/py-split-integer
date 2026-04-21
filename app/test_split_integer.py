from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 17
    parts = split_integer(value, 4)
    assert sum(parts) == value, (
        f"Sum of parts {parts} must be equal to value {value}"
    )


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 12
    number_of_parts = 3
    expected = [4, 4, 4]
    assert split_integer(value, number_of_parts) == expected, (
        f"If {value} is divisible by {number_of_parts} then it should be equal"
    )


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 8
    assert split_integer(value, 1) == [value], (
        "If quantity of parts - 1, result should be list with only one element"
    )


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 32
    number_of_parts = 6
    parts = split_integer(value, number_of_parts)
    assert parts == sorted(parts), (
        f"Parts {parts} should be sorted in ascending order"
    )
    assert max(parts) - min(parts) <= 1, (
        "Different between min and max of parts should not be more than 1"
    )


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 3
    number_of_parts = 5
    expected = [0, 0, 1, 1, 1]
    result = split_integer(value, number_of_parts)
    assert result == expected, (
        f"For value={value} and parts={number_of_parts}"
        f" expected {expected} but got {result} "
    )
    assert len(result) == number_of_parts, (
        "Quantity of parts should be equal to number of parts"
    )
