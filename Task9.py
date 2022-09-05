import threading
import time

class clock(threading.Thread):
    def __init__(self,x,interval):
        super().__init__()
        self.interval=interval


    def run(self):
        y=x
        for i in range(10,1,-1):
            print("Поток " + str(y) + ": " + str(i) + "\n")
            time.sleep(self.interval)
        print("Поток " + str(y) + " закончил вывод" + "\n")


for x in range(1,3):
    t = clock(x,1)
    t.start()
t.join()
