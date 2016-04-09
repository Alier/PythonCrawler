'Collection of reusable data validation utilties'

def validate_percentage(value):
    if not isinstance(value, (int, float)):
        raise TypeError('Expected int or float')
    if value < 0.0 or value > 100.0:
        raise ValueError('Expected 0 to 100')
