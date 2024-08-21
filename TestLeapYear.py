import LeapYearChecker


class TestAYearIsALeapYear:
    checker = LeapYearChecker

    def test_if_it_is_divisible_by_4_but_not_by_100(self):
        assert TestAYearIsALeapYear.checker.is_leap_year(1996) == True

    def test_if_it_is_divisible_by_400(self):
        assert TestAYearIsALeapYear.checker.is_leap_year(1600) == True


class TestALeapYearIsNotALeapYear:
    checker = LeapYearChecker

    def test_if_it_is_not_divisible_by_4(self):
        assert TestAYearIsALeapYear.checker.is_leap_year(1995) == False

    def test_if_it_is_divisible_by_100_but_not_by_400(self):
        assert TestAYearIsALeapYear.checker.is_leap_year(1900) == False
