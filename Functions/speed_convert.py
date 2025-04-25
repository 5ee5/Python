def potential_energy(m: float, g: float, h: float = 9.8):
    return m*g*h

def kinetic_energy(m: float, v: float):
    return 0.5 * m * v ** 2
def km_h_to_m_sec(kmh: float):
    return kmh * 1000 / 3600

#print(potential_energy(1500, 70))
print(kinetic_energy(1500, km_h_to_m_sec(70)))