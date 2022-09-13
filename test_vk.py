import pytest


class TestsTuple:
    def test_upper_first_char(self):
        words = ('Dog', 'Flask', 'Test', 'Right', 'Left')
        for i in words:
            assert i[0] == i[0].upper(), f'{i} != {i[0].upper() + i[1:]}'

    @pytest.mark.parametrize('tuple_int', [
        (1, 2, 3),
        (2, 0, 4),
        (2, 2, 2),
    ])
    def test_sum_less_then_20(self, tuple_int, skip_if_already_failed):
        sum_numbers = 0
        for i in tuple_int:
            sum_numbers += i
            assert sum_numbers < 10

    def test_index_20(self):
        tuple_number = (1, 2, 3, 4, 5, 6)
        with pytest.raises(IndexError):
            assert tuple_number[10]


class TestSet:
    def test_name_in_set(self):
        set_names = {'Roidon', 'Nikita', 'Alexey'}
        assert 'Nikita' in set_names

    @pytest.mark.parametrize('set_int', [
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    ])
    def test_is_set(self, set_int, skip_if_already_failed):
        assert type(set_int) == set, f'{set_int} is not type set'

    def test_add_element(self):
        set_number = {1, 2, 3, 4}
        with pytest.raises(AttributeError):
            assert set_number.append(5)
