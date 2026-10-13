phrase = "Beau" + " is my name"
name = "Beau"
name += " is my name"

# Multi-line strings
multiline = """Beau is
39
years old"""

# String methods
print("beau".upper())    # "BEAU"
print("BEAU".lower())     # "beau"
print("beau person".title()) # "Beau Person"
print("beau".islower())   # True

# Global functions & membership
print(len("Beau"))        
print("au" in "Beau")          # True

# Escaping & newlines
escaped = "He said, \"Hello!\" \nNew line \\ backslash"

# Slicing and indexing
name = "Beau is cool"
print(name[0])      # 'B'
print(name[-1])     # 'l'
print(name[1:3])    # 'ea'
print(name[:4])     # 'Beau'
print(name[5:])     # 'is cool'