data = {'variable1': [], 'variable2': [], 'variable3': []}

# Version 1: Shortcut
print("version 1")
for var in data:
    print(f"Key: {var}, Type: {type(var)}")

# Version 2: Explicit
print("version 2")
for var in data.keys():
    print(f"Key: {var}, Type: {type(var)}")