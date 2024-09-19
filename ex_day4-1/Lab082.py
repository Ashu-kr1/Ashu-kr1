# ✅ Understanding Decorators in Python
import time
def start():
    print("Before the running UI TC")
    print("Start the Browser")

def end():
    print("End the running UI TC")
    print("Quit the Browser")

def test_ui():
    print("I will test the UI")

start()
test_ui()
end()

def time_decorator(func):
    def wrapper():
        start_time = time.time()
        print(start_time)
        func()
        end_time = time.time()
        print(end_time)
        print(f"time take by function{end_time-start_time}")
    return wrapper()

@time_decorator
def test_ui_1():
    print("Add a function,time taken by this function")
    time.sleep(10)

@time_decorator
def test_ui_2():
    print("Add a function,time taken by this function")
    time.sleep(60)

