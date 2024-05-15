from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(args, kwargs)
        print ("antes de dllamar a la funcion")
        result = func(*args, **kwargs)
        print(result.upper())
        print("despues de llamar a la funcion")
        return result
    return wrapper

@my_decorator
def greet(name):
    return(f"hola, {name}")

greet("joel")

print(greet.__name__)
print(greet.__doc__)