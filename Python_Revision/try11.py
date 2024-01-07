try:
    open('database.mysql')
except OSError:
    raise RuntimeError from None