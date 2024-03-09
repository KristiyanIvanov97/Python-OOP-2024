from functools import reduce


class Calculator:

    def add(*nums) -> int:
        return reduce(lambda x, y: x + y, nums)

    def multiply(*nums) -> int:
        return reduce(lambda x, y: x * y, nums)

    def divide(*nums) -> float:
        return reduce(lambda x, y: x / y, nums)

    def subtract(*nums) -> int:
        return reduce(lambda x, y: x - y, nums)
