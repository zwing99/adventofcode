import time
import re

foo = re.compile(r"\.+")
a = "......###....#...####......##.#.##.....###..."

start = time.time()
b = a.strip(".")
for i in range(10_000_000):
    asdf = foo.split(b)
    #print(asdf)
    #break
end = time.time()
print(f"re.split: {end-start}")

start = time.time()
b = a.strip(".")
b = foo.sub(".", a)
for i in range(10_000_000):
    asdf = [x for x in b.split(".") if x]
    #print(asdf)
    #break
end = time.time()
print(f"re.sub: {end-start}")


