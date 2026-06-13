class RomanConverter:
    def to_roman(self, num):
        values = [1000, 900, 500, 400, 100, 90, 50, 40,
                  10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL",
                   "X", "IX", "V", "IV", "I"]

        roman = ""

        for i in range(len(values)):
            while num >= values[i]:
                roman += symbols[i]
                num -= values[i]

        return roman


# Create object
converter = RomanConverter()

# Take input from user
number = int(input("Enter an integer (1-3999): "))

# Display Roman numeral
print("Roman Numeral:", converter.to_roman(number))