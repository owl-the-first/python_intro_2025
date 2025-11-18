import pickle

s = {1, 2, 3, 4, 5}
print(f"{pickle.dumps(s) = }")

t = pickle.dumps(s)
del s

new_s = pickle.loads(t)
print(f"{new_s = } ")
print(f"{id(new_s) = }")

s = {1, 2, 3, 4, 5}
t = pickle.dumps(s, protocol=0)

print(f"{t = }")
