class Counter(object):
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def __iter__(self):
        counter = self.low
        while counter <= self.high:
            yield counter
            counter += 1


gobj = Counter(5, 10)
for num in gobj:
    print(num, end=' ')
print()
print('-------')
for num in gobj:
    print(num, end=' ')
