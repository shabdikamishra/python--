from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

# Counter
a = "aaaaabbbbcc"
my_counter = Counter(a)
print(my_counter.most_common(1))  # [('a', 5)]

# namedtuple
Point = namedtuple("Point", "x, y")
pt = Point(1, -4)
print(pt.x, pt.y)

# defaultdict (returns default type value when key is missing)
d = defaultdict(int)
d["a"] = 1
print(d["b"])  # 0 (does not raise KeyError)

# deque
d_queue = deque()
d_queue.append(1)
d_queue.appendleft(2)
d_queue.pop()
d_queue.popleft()
d_queue.rotate(1)   # Rotates elements right by 1