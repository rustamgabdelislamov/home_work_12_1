import time


def log(filename=""):
    def my_decorator(func):
        def inner(*args, **kwargs):
            time_1 = time.time()
            print(f'Function {func.__name__} started at {time_1}')
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"

                if filename:
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(log_message + '\n')
                else:
                    print(log_message)
                return result
            except Exception as e:
                error_message = f"{func.__name__} error: {e}. Inputs: {args, kwargs}"
                if filename:
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(error_message + '\n')
                else:
                    print(error_message)
                raise
        return inner

    return my_decorator
