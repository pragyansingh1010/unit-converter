def km_to_m(km):
    return km * 1000

def m_to_km(m):
    return m / 1000

assert km_to_m(0) == 0
assert km_to_m(1) == 1000
assert m_to_km(1000) == 1
assert m_to_km(0) == 0
print("Length conversion tests passed")
