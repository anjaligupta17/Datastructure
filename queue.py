class Queue:
    def __init__(self):
        self.queue=list()
    def add(self,data):
        if data not in self.queue:
            self.queue.insert(0,data)
            return True
        else:
            return False
    def size(self):
        return len(self.queue)
    def remove(self):
        if len(self.queue)<=0:
            return ("No element in it")
        else:
            return self.queue.pop()
thequeue=Queue()
thequeue.add("anjali")
thequeue.add("gupta")
print(thequeue.size())
print(thequeue.remove())