# Libraries
from datetime import datetime
import dictionary as dictionary
import functions as funcs 

# Yn Yc: solved with Bisection Method

# Main vars
unit_sys = 'SI' # SI - International, US - Imperial/US
q = 10 # Flow
g = 9.806 # Gravity acceleration
b = 5 # Channel base
z1 = 2 # Left side slope
z2 = 2 # Right side slope
so = 0.0008969 # Channel slope
n = 0.035 # Channel roughness
alpha = 1 # Kinetic correction factor
rho = 1000 # ρ: fluid density
y1 = 0.001 # Numerical method, low elevation seed
y2 = 10 # Numerical method, high elevation seed
steps = 32 # Numerical method, steps
app_version = 'v20251128' # Version control

# Pre validations
# Units system eval
if unit_sys.upper() == 'SI':
    c = 1
    unit_q = "m³/s"
    unit_length = 'm'
    unit_rho = 'kg/m³'
    unit_g = 'm/s²'
    unit_tau = 'Pa, N/m²' # Shear stress
    unit_f = 'N' # Hydraulic force, Newton
else:
    c = 1.486
    unit_q = "ft³/s"
    unit_length = "ft"
    unit_rho = 'lb/ft³'
    unit_g = 'ft/s²'
    unit_tau = 'lbf/ft²' # # Shear stress, psf
    unit_f = 'lb'  # Hydraulic force, lb
# alpha validation
if alpha == 0: alpha = 1
# eval y2 > y1
y1a = y1
if y2 < y1:
    y1 = y2
    y2 = Y1a
# eval # step iterations > 0
if steps <= 0: steps = 32
y1aux = y1
y2aux = y2
y1a = y1
y2b = y2

# Yc Calculation
for i in range(steps):
    y2a = (y2 + y1) / 2
    q1 = funcs.yc_calc(q, g, b, z1, z2, y2, alpha)
    q2 = funcs.yc_calc(q, g, b, z1, z2, y2a, alpha)
    if (funcs.sgn(q1) + funcs.sgn(q2)) == 0:
        y1 = y2
    y2 = y2a

# Yn Calculation
for i in range(steps):
    y2c = (y2b + y1a) / 2
    q1 = funcs.yn_calc(q, b, z1, z2, y2b, so, n, c)
    q2 = funcs.yn_calc(q, b, z1, z2, y2c, so, n, c)
    if (funcs.sgn(q2) + funcs.sgn(q1)) == 0:
        y1a = y2b
    y2b = y2c

# Shape evaluation
shape = funcs.shape_type(b, z1, z2)

# Print input values
results = f'App version: {app_version}\n'
results += f'Run date: {datetime.now()}\n'
results += f'\n{funcs.txt_separator(70)}\n{shape} SHAPE >>> Input values ({dictionary.dict['unit_sys']}: {unit_sys})\n{funcs.txt_separator(70)}\n\n'
results += f'General parameters\n\n'
results += f'{dictionary.dict['Q']}: {q} {unit_q}\n'
results += f'{dictionary.dict['g']}: {g} {unit_g}\n'
results += f'{dictionary.dict['b']}: {b} {unit_length}\n'
results += f'{dictionary.dict['z1']}: {z1} {unit_length}\n'
results += f'{dictionary.dict['z2']}: {z2} {unit_length}\n'
results += f'{dictionary.dict['So']}: {so} {unit_length}/{unit_length}\n'
results += f'{dictionary.dict['n']}: {n}\n'
results += f'{dictionary.dict['alpha']}: {alpha}\n'
results += f'{dictionary.dict['rho']}: {rho} {unit_rho}\n'
results += f'{dictionary.dict['c']}: {c}\n\n'
results += f'Numerical method parameters\n\n'
results += f'{dictionary.dict['y1']}: {y1aux} {unit_length}\n'
results += f'{dictionary.dict['y2']}: {y2aux} {unit_length}\n'
results += f'{dictionary.dict['steps']}: {steps}\n'

# Print results
results += f'\n{funcs.txt_separator(70)}\nResults for Normal (n) an Critical (c) flow\n{funcs.txt_separator(70)}\n'
results += f'\n● {dictionary.dict['Yn']}\n\n'
results += f'Yn: {y2b} {unit_length}\n'
results += f'\n● {dictionary.dict['Yc']}\n\n'
results += f'Yc: {y2} {unit_length}\n'
results += f'\n● {dictionary.dict['A']}\n\n'
results += f'An: {funcs.area(b, z1, z2, y2b)} {unit_length}²\n'
results += f'Ac: {funcs.area(b, z1, z2, y2)} {unit_length}²\n'
results += f'\n● {dictionary.dict['P']}\n\n'
results += f'Pn: {funcs.wet_perimeter(b, z1, z2, y2b)} {unit_length}\n'
results += f'Pc: {funcs.wet_perimeter(b, z1, z2, y2)} {unit_length}\n'
results += f'\n● {dictionary.dict['T']}\n\n'
results += f'Tn: {funcs.top_width(b, z1, z2, y2b)} {unit_length}\n'
results += f'Tc: {funcs.top_width(b, z1, z2, y2)} {unit_length}\n'
results += f'\n● {dictionary.dict['R']}\n\nR = A / P\n'
results += f'Rn: {funcs.hydraulic_ratio(b, z1, z2, y2b)} {unit_length}\n'
results += f'Rc: {funcs.hydraulic_ratio(b, z1, z2, y2)} {unit_length}\n'
results += f'\n● {dictionary.dict['D']}\n\nD = A / T\n'
results += f'Dn: {funcs.hydraulic_depth(b, z1, z2, y2b)} {unit_length}\n'
results += f'Dc: {funcs.hydraulic_depth(b, z1, z2, y2)} {unit_length}\n'
results += f'\n● {dictionary.dict['V']}\n\nV = Q / A\n'
results += f'Vn: {q / funcs.area(b, z1, z2, y2b)} {unit_length}/s\n'
results += f'Vc: {q / funcs.area(b, z1, z2, y2)} {unit_length}/s\n'
results += f'\n● {dictionary.dict['Fr']}\n\nFr = V / (g * D) ^ 0.5\n'
results += f'Frn: {funcs.froude_number(q / funcs.area(b, z1, z2, y2b), g, funcs.hydraulic_depth(b, z1, z2, y2b))[0]}\n{funcs.froude_number(q / funcs.area(b, z1, z2, y2b), g, funcs.hydraulic_depth(b, z1, z2, y2b))[1]}\n'
results += f'Frc: {funcs.froude_number(q / funcs.area(b, z1, z2, y2), g, funcs.hydraulic_depth(b, z1, z2, y2))[0]}\n'
results += f'\n● {dictionary.dict['τօ']}\n\nτօ = ρ * g * R * so\n'
results += f'τn: {funcs.shear_stress(rho, g, funcs.hydraulic_ratio(b, z1, z2, y2b), so)} {unit_tau}\n'
results += f'τc: {funcs.shear_stress(rho, g, funcs.hydraulic_ratio(b, z1, z2, y2), so)} {unit_tau}\n'
results += f'\n● {dictionary.dict['F']}\n\nF = (Ycentroid * ρ * g) * A\n'
results += f'Yn centroid: {funcs.y_centroid(b, z1, z2, y2b)} {unit_length}\n'
results += f'Yc centroid: {funcs.y_centroid(b, z1, z2, y2)} {unit_length}\n'
results += f'Fn: {funcs.y_centroid(b, z1, z2, y2b) * g * rho * funcs.area(b, z1, z2, y2b)} {unit_f}\n'
results += f'Fc: {funcs.y_centroid(b, z1, z2, y2) * g * rho * funcs.area(b, z1, z2, y2)} {unit_f}\n'
results += f'\n● {dictionary.dict['Sc']}\n\nSc = g * n ^ 2 * (Pc / Tc) / (c ^ 2 * Rc ^ (1 / 3))\n'
results += f'Sc: {funcs.critic_slope(g, n, funcs.wet_perimeter(b, z1, z2, y2), funcs.top_width(b, z1, z2, y2), c, funcs.hydraulic_ratio(b, z1, z2, y2))} {unit_length}/{unit_length}\n'
results += f'Slope type: {funcs.profile_type(so, y2b, y2)}\n'
print(results)

# Developers
# github.com/rcfdtools
# github.com/frankv13
# github.com/juanrodace