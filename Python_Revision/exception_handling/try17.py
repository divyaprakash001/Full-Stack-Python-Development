try:
    raise TypeError
except Exception as e:
    e.add_note('add some information')
    e.add_note("add some more information")
    raise