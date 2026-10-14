#built-in exception handling
try:
    a = 5 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
else:
    print("Everything was successful")
finally:
    print("Cleanup operations completed")

#assertion
x = 5
assert (x >= 0), "x is not positive"

#Custom Exception Classes
class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(val):
    if val > 100:
        raise ValueTooHighError("Value is too high")
    if val < 5:
        raise ValueTooSmallError("Value is too small", val)

try:
    test_value(1)
except ValueTooSmallError as e:
    print(e.message, e.value)