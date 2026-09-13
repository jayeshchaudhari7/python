#🔥 Python Unpacking & Mapping Cheat Sheet
#1. Basic Unpacking
a, b, c = [1, 2, 3]        # List
x, y, z = (10, 20, 30)     # Tuple
p, q, r = "ABC"            # String

print(a, b, c)  # 1 2 3

#2. Extended Unpacking with *
nums = [1, 2, 3, 4, 5]

first, *middle, last = nums
print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5

#3. Nested Unpacking
data = ("jay", (43, 23, 65))
name, (m1, m2, m3) = data

print(name)   # jay
print(m1, m2, m3)  # 43 23 65

#4. Dictionary Unpacking
student = {"name": "jay", "age": 20}

# Iterating keys and values
for k, v in student.items():
    print(k, v)

# Merge two dicts
d1 = {"x": 1, "y": 2}
d2 = {"y": 3, "z": 4}
merged = {**d1, **d2}
print(merged)  # {'x': 1, 'y': 3, 'z': 4}

#5. Using map() for Type Conversion
nums = ["1", "2", "3"]

ints = list(map(int, nums))       # [1, 2, 3]
floats = list(map(float, nums))   # [1.0, 2.0, 3.0]

names = ["jay", "jjj"]
upper = list(map(str.upper, names))  # ['JAY', 'JJJ']

#6. Unpacking into Functions
def add(a, b, c):
    return a + b + c

nums = [1, 2, 3]
print(add(*nums))   # 6   (*list → args)

person = {"name": "jay", "age": 20}
def info(name, age):
    print(f"{name} is {age} years old")

info(**person)   # jay is 20 years old (**dict → kwargs)

#7. Iterable Unpacking with *
nums = [1, 2, 3]
print(*nums)  # 1 2 3

combined = [*range(3), *"ab"]
print(combined)  # [0, 1, 2, 'a', 'b']

#8. Safe Dictionary Access
student_marks = {"jay": [43, 23, 65]}

# Normal access
scores = student_marks["jay"]

# Safe access (no error if key missing)
scores = student_marks.get("abc", [])
print(scores)  # []