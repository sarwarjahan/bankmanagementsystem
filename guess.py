def start_end_decorator(func):
    def wrapper():
        print("Sarwar")
        func()
        print("Rafi")
    return wrapper
    
def print_name():
    print("Alex")
    
print_name = start_end_decorator(print_name)
print_name()