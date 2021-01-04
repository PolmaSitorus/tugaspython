
def KMP_String(pattern, text):
    a = len(text)
    b = len(pattern)

    prefix_arr = get_prefix_arr(pattern, b)

    initial_point = []

    m = 0
    n = 0

    while m != a:

        if text[m] == pattern[n]:
            m += 1
            n += 1

        else:
            n = prefix_arr[n-1]

        if n == b:
            initial_point.append(m-n)
            n = prefix_arr[n-1]
        elif n == 0:
            m += 1

    return initial_point


def get_prefix_arr(pattern, b):
    prefix_arr = [0] * b
    n = 0
    m = 1

    while m != b:
        if pattern[m] == pattern[n]:
            n += 1
            prefix_arr[m] = n
            m += 1
        elif n != 0:
            n = prefix_arr[n-1]
        else:
            prefix_arr[m] = 0
            m += 1

    return prefix_arr


string = "ATASBAWAHKIRIKANAN"
pat = "WAHKI"

initial_index = KMP_String(pat, string)

for i in initial_index:
    print('Pola text ', pat, ' ditemukan pada index', i)


string = "ATASBAWAHKIRIKANAN"
pat = "ASBAW"

initial_index = KMP_String(pat, string)

for i in initial_index:
    print('Pola text ', pat, ' ditemukan pada index', i)
