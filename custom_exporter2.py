from prometheus_client import start_http_server, Counter 
import random
import time

c = Counter('keyboard_counter', 'Keyboard counter')

def increment():
    c.inc()

if __name__ == '__main__':
        start_http_server(8001)
        while True:
            input()
            increment()
