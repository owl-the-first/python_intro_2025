from string import ascii_lowercase

gl = set("aouie")
sogl = set(ascii_lowercase) - wov
s = set(input())
print("Гласных:", len(s & gl))
print("Согласных:", len(s & sogl))
