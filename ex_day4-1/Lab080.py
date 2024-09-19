#Understanding Decorators in Python

def add_extra_secuitry(func):
    # two parts
    # wrappers & call
    def wrapper():
        print("1.Before the function is called.")
        print("2.Add Helmet,Dashcasm,gloves,knee guadrd")
        #drive bike
        func()
        print("3.After the function is called")
        print("4 secure Driving")

    return wrapper()

# definition
# @my_decorator
# def drive_bike():
#     print("I am driving")
@add_extra_secuitry
def drive_scooty():
    print("Normal function")



print("---------------")

# ✅ Understanding Decorators in Python

def add_before_ui_after_ui(custom_function_where_you_want_extra_func):
    # two parts
    # wrapper & call

    def wrappers():
        print("Before the running UI TC")
        print("Start the browsers")
        custom_function_where_you_want_extra_func()
        print("Ending the running UI TC")
        print("Quit the Browser!")
    return wrappers()

@add_before_ui_after_ui
def test_ui():
    print("I will Test the UI")




