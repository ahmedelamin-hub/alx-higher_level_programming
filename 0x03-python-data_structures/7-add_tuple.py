cat > #!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    ew = ()
    ple1 = tuple_a + (0, 0)
    ple2 = tuple_b + (0, 0)
    ew = ple1[0] + ple2[0], ple1[1] + ple2[1]
    return ew
