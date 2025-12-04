global_var = 22

def modify_glob():
    global global_var
    global_var = 32
    print("Inside f: ", global_var)

modify_glob()
print("outside f:", global_var)

