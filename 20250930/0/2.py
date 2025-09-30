def req(n):
    return req(n - 1)*2 if n > 0 else 1
