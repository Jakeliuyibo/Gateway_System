

def conv_from_str_to_enum(enum, str):
    """ conv from str to enum  """
    for idx in range(len(enum)):
        if str == enum(int(idx+1)).name:
            return enum(int(idx+1))
    else:
        return enum(1)
