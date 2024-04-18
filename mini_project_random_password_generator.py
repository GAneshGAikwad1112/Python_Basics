#Random Password Generator

import random
import string

pass_len = 12

charVlaues = string.ascii_letters + string.digits + string.punctuation



#list comprehension (function for i in range(n))

res = "".join([random.choice(charVlaues) for i in range(pass_len)])
print(res)

# password = ""
# for i in range(pass_len):
    
#     password += random.choice(charVlaues)
    
# print("Your random password is: ", password)

