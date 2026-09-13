def kg_to_g(kg):
    return kg * 1000

def g_to_kg(g):
    return g / 1000

assert kg_to_g(0) == 0
assert kg_to_g(2) == 2000
assert g_to_kg(1000) == 1
assert g_to_kg(0) == 0
print('Weight conversion tests passed')
