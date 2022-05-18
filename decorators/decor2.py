#We have to use contextlib.contextmanager to decorate a generator function which yields
# exactly once. Everything before yield is considered to be __enter__ section and everything
# after, to be __exit__ section. The generator function should yield the resource.
from contextlib import contextmanager

@contextmanager
def ContextManager():
    # Before yield as the enter method
    print("Enter method called")
    yield

    # After yield as the exit method
    print("Exit method called")


with ContextManager() as manager:
    print('with statement block')
