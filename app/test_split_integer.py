from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(17, 4)) == 17


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result_list = split_integer(16, 4)
    for i in range(len(result_list) - 1):
        assert result_list[i] == result_list[i + 1]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8,1 )[0] == 8


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(32,6) == sorted(split_integer(32,6))


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(3, 5) == [0, 0, 1, 1, 1]
