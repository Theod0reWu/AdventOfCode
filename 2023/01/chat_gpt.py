import re

def extract_calibration_values(line):
    # Regular expression to find all digits (both spelled-out and numerical)
    digits = re.findall(r'\b(?:zero|one|two|three|four|five|six|seven|eight|nine|\d)\b', line)
    
    # Convert spelled-out digits to numerical representation
    numerical_digits = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    numerical_values = [numerical_digits.get(digit, digit) for digit in digits]

    # Combine the first and last digits to form a two-digit number
    calibration_values = [int(numerical_values[0] + numerical_values[-1])]

    return calibration_values

def calculate_sum_of_calibration_values(input_lines):
    total_sum = 0

    for line in input_lines:
        calibration_values = extract_calibration_values(line)
        total_sum += sum(calibration_values)

    return total_sum

# Example usage
calibration_document = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen"
]

result = calculate_sum_of_calibration_values(calibration_document)
print(result)
