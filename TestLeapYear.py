import pytest

import LeapYearChecker


class TestAYearIsALeapYear:
    checker = LeapYearChecker

    @pytest.mark.parametrize("year", [2020, 2016, 1984, 4])
    def test_if_it_is_divisible_by_4_but_not_by_100(self, year):
        assert TestAYearIsALeapYear.checker.is_leap_year(year) == True

    @pytest.mark.parametrize("year", [400, 1600, 4000])
    def test_if_it_is_divisible_by_400(self, year):
        assert TestAYearIsALeapYear.checker.is_leap_year(year) == True


class TestALeapYearIsNotALeapYear:
    checker = LeapYearChecker

    @pytest.mark.parametrize("year", [2022, 2019, 1999, 1])
    def test_if_it_is_not_divisible_by_4(self, year):
        assert TestAYearIsALeapYear.checker.is_leap_year(year) == False

    @pytest.mark.parametrize("year", [2100, 1900, 100])
    def test_if_it_is_divisible_by_100_but_not_by_400(self, year):
        assert TestAYearIsALeapYear.checker.is_leap_year(year) == False
