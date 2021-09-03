

import random
import string

def make_password(count):
    sp_chars = " !\"#$%&*@"
    All_chars = string.ascii_letters + string.digits + sp_chars
    chars_count = len(All_chars)
    pass_list = []
    while count > 0:
        random_number = random.randint(0,chars_count -1 )
        random_char = All_chars[random_number]
        pass_list.append(random_char)
        count -= 1
    print("".join(pass_list))

make_password(10)

