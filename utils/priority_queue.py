import heapq

class PriorityQueue:
    def __init__(self):
        self.list = []
    
    def push(self, element):
        heapq.heappush(self.list, element)

    def pop(self):
        return heapq.heappop(self.list)
    
    def size(self):
        return len(self.list)