from collections import deque
import queue

queue = deque(maxlen=3)
queue.append(1)
print(queue)


customQueue = queue.Queue(maxsize= 3)
customQueue.put(1)
customQueue.put(1)