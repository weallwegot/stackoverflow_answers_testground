# someone wants to catch any type of exception but then also raise the message
# i dont quite understand the motivation
try:
    # some code that raises an error, like type error
    g = 10 + '11'
except Exception as e:
    raise AssertionError('{}: {}'.format(type(e), e.message))
