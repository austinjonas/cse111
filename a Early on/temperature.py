from tempfile import tempdir


def f_to_c(f):
    temp = f - 50
    return temp

f_to_c(32)

print(tempdir)