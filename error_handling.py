# rise a custom exeption that checks for positive numbers using a custom exception

class NotPositiveError(Exception):
    def __init__(self, number):
        super().__init__(f"The number {number} is not positive.")

def check_positive(number):
    if number <= 0:
        raise NotPositiveError(number)
    else:
        print(f"{number} is a positive number.")

try:
    check_positive(-5)
except NotPositiveError as e:
    print(e)



