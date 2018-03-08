# coding=utf-8
import threading
import Queue
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from threading import Thread

queue_tmp = Queue.Queue(10)


class Producer(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        while 1:
            queue_tmp.put(0)
            print("制作者: %s create a 产品" % self.name)
            print("制作者: %s put a 产品 into queue" % self.name)

class Consumer(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        while 1:
            queue_tmp.get()
            print("消费者: %s get a 产品" % self.name)


def test():
    p1 = Producer("制作者-1")
    c1 = Consumer("消费者-1")
    c2 = Consumer("消费者-2")

    p1.start()
    c1.start()
    c2.start()


if __name__ == "__main__":
    test()
