def f():
    raise OSError('operation failed')

excs=[]

for i in range(3):
    try:
        f()
    except Exception as e:
        e.add_note(f'happened in iteration {i+1}')
        excs.append(e)
raise ExceptionGroup('We have some problem',excs)