#   Raising exceptions
    #   Permitem que o programador force a ocorrência de uma determinada exception

    try:
        raise NameError('HiThere')
    except NameError:
        print('An exception flew by!')
        raise