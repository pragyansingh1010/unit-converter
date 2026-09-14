def cm_to_m(cm):
    return cm / 100

def m_to_cm(m):
    return m * 100

assert cm_to_m(100) == 1
assert cm_to_m(250) == 2.5
assert m_to_cm(1) == 100
assert m_to_cm(2.5) == 250
print('Length conversion rules passed')
