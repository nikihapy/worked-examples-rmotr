def user_input_until_exit():
    try:
        _input = raw_input
    except NameError:
        _input = input
    while _input("Enter a string (type 'exit' to quit): ") != 'exit':
        pass
