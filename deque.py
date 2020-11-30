import collections
DoubleEnded=collections.deque(["Mon","Tue","Wed"])
DoubleEnded.append("Thur")
DoubleEnded.appendleft("Sun")
DoubleEnded.pop()
print(DoubleEnded)
DoubleEnded.popleft()
print(DoubleEnded)