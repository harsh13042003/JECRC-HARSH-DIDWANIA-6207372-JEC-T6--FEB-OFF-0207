# **File is a type of container in whcih we contain or store some data.
# ** By using extension name, we can identify what type of data us there of it
#     Ex -> .py,.mp4,.html

'''
    Before handling any file, taking permission is very important.

    open():
        open('filename.ext'/'absolute_path', mode)

    close():
        var_name.close()

    Here total 3 different modes are present,
        1. write(w)
        2. read(r)
        3. append(a)

    write mode:
    1. only write(w)
    2. write + read(w+)
    3. write binary(wb)
    4. write & read binary( wb+)

    read mode:
    1. only read(r)
    2. read + write(r+)
    3. read binary(rb)
    4. raed & write binary( rb+)

    append mode:
    1. only append (a)
    2. append + read (a+)
    3. append binary(ab)
    4. append & read binary (ab+)

**For write operation,
    1. write(str_data): single line of data.
    2. writelines([ line1, line2, line3 ............., linen]): Multiple line of data.

    Note: 
    1. In this , if the file is not present, it will create one then perform write operation.
    2. If the file is already present, them it will override the prev data with the new one.
'''