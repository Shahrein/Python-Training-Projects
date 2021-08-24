def is_a_triangle(a, b, c):
    if a + b <= c or b + c <= a or a + c <= b:
        return False
    return True

print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))