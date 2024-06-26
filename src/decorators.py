from typing import Any, Callable


def log(filename: Any = None) -> Callable:
    """Декоратор, который логирует вызов функции и ее результат в файл или в консоль"""

    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
                if filename:
                    with open(filename, "a") as log_file:
                        log_file.write(log_message + "\n")
                else:
                    print(log_message)
                return result
            except Exception as e:
                error_message = f"{func.__name__} error: {e}. Inputs:{args}, {kwargs}"
                if filename:
                    with open(filename, "a") as log_file:
                        log_file.write(error_message + "\n")
                else:
                    print(error_message)
                raise

        return wrapper

    return decorator


# @log()
# def my_function(x: int, y: int) -> int:
#     return x + y
#
#
# my_function(1, 2)
