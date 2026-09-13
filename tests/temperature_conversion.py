def km_to_m(km):
    return km * 1000

def m_to_km(m):
    return m / 1000

assert km_to_m(0) == 0
assert km_to_m(1) == 1000
assert m_to_km(2500) == 2.5
print('Unit conversion tests passed')
