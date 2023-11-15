"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    
    >>> print(serial)
    SerialGenerator(start=100, current=100)
    """
    def __init__(self,start):
        self.start = start
        self.current = start - 1
    
    def generate(self):
        self.current += 1
        return self.current
    
    def reset(self):
        self.current = self.start -1
    
    def __repr__(self):
        return f"SerialGenerator(start={self.start}, current={self.current})"

serial = SerialGenerator(100)
print(serial)

