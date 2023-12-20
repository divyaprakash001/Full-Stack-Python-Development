s1 = '{},{},{} are three friends.'
s1 = s1.format('divya','ritesh','sipu')
print(s1)

s2 = '{2},{1},{0} are three friends.'
s2 = s2.format('divya','ritesh','sipu')
print(s2)


s3 = '{first},{second},{third} are three friends.'
s3 = s3.format(second='divya',first='ritesh',third='sipu')
print(s3)