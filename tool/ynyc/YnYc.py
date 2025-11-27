# Yn Yc: solved with Bisection Method

# Main vars
UnitSys = 'SI' # SI - International, US - Imperial/US
q = 522.1
g = 9.806
b = 130
z1 = 2
z2 = 2
so = 0.0008969
n = 0.035
alpha = 1
y1 = 0.001
y2 = 10
rho = 1000 # ρ: density, kg/m³
steps = 32

# Geometric shape type
def f_shape_type(b, z1, z2):
    if z1 == 0 and z2 == 0:
        shape_type = "RECTANGULAR"
    elif b == 0 and z1 > 0 and z2 > 0 and z1 == z2:
        shape_type = "TRIANGULAR"
    elif b > 0 and z1 > 0 and z2 > 0:
        shape_type = "TRAPEZOIDAL"
    else:
        shape_type = "DITCH"
    return shape_type

# Area
def f_area(b, z1, z2, y):
    area = b * y + ((y ** 2) / 2) * (z1 + z2)
    return area

# Critical depth
def f_yc_calc(q, g, b, z1, z2, y, alpha):
    yc_calc = q - ((g * (f_area(b, z1, z2, y)) ** 3) / (alpha * f_top_width(b, z1, z2, y))) ** 0.5
    return yc_calc

# Normal depth
def f_yn_calc(q, b, z1, z2, y, so, n, c):
    yn_calc = q - ((c / n) * (f_area(b, z1, z2, y)) * (f_hydraulic_ratio(b, z1, z2, y)) ** (2 / 3) * so ** 0.5)
    return yn_calc

# Hydraulic ratio
def f_hydraulic_ratio(b, z1, z2, y):
    hydraulic_ratio = f_area(b, z1, z2, y) / f_wet_perimeter(b, z1, z2, y)
    return hydraulic_ratio

# Wet perimeter
def f_wet_perimeter(b, z1, z2, y):
    wet_perimeter = b + y * ((1 + z1 ** 2) ** 0.5 + (1 + z2 ** 2) ** 0.5)
    return wet_perimeter

# Superficial top width calculation
def f_top_width(b, z1, z2, y):
    top_width = b + y * (z1 + z2)
    return top_width

# Hydraulic depth
def f_hydraulic_depth(b, z1, z2, y):
    hydraulic_depth = f_area(b, z1, z2, y) / f_top_width(b, z1, z2, y)
    return hydraulic_depth

# Froud number
def f_froude_number(v, g, d):
    froude_number = v / (g * d) ** 0.5
    return froude_number

# Profile type
def f_profile_type(s, yn, yc):
    if s == 0:
        fProfileType = 'H, Horizontal'
    else:
        if yn > yc: fProfileType = 'M, Mild' # Moderado
        if yn < yc: fProfileType = 'S, Steeped' # Escarpado
        if yn == yc: fProfileType = 'C, Critical' # Critico
        if s < 0: fProfileType = 'A, Adverse' #Adverso
    return fProfileType

# Critical slope
def f_critic_slope(g, n, pc, tc, c, rc):
    critic_slope = g * n ** 2 * (pc / tc) / (c ** 2 * rc ** (1 / 3))
    return critic_slope

# Shear stress
def f_shear_stress (rho, g, rh, so): # rh = hydraulic ratio
    shear_stress = rho * g * rh * so
    return shear_stress

# Centroidal depth
def f_y_centroid(b, z1, z2, y):
    y_centroid = y ** 2 * ((3 * b / y) + z1 + z2) / (6 * b + 3 * y * (z1 + z2))
    return y_centroid

# Sign of a number
def sgn(num):
  if num > 0:
    return 1
  elif num < 0:
    return -1
  else:
    return 0

# Text separator
def txt_separator(num):
  return '-' * num

# Pre validations
# Units system eval
if UnitSys.upper() == 'SI':
    c = 1
    c_unit_text = "m"
    c_unit_text_shear_stress = 'Pa' # N/m²
    c_unit_text_shear_hydraulic_force = 'N' # Newton
else:
    c = 1.486
    c_unit_text = "ft"
    c_unit_text_shear_stress = 'lbf/ft²' # psf
    c_unit_text_shear_hydraulic_force = 'lb'  # Newton
# alpha validation
if alpha == 0: alpha = 1
# eval y2 > y1
y1a = y1
if y2 < y1:
    y1 = y2
    y2 = Y1a
# eval # step iterations > 0
if steps <= 0: steps = 32
y1a = y1
y2b = y2

# Yc Calculation
for i in range(steps):
    y2a = (y2 + y1) / 2
    q1 = f_yc_calc(q, g, b, z1, z2, y2, alpha)
    q2 = f_yc_calc(q, g, b, z1, z2, y2a, alpha)
    if (sgn(q1) + sgn(q2)) == 0:
        y1 = y2
    y2 = y2a

# Yn Calculation
for i in range(steps):
    y2c = (y2b + y1a) / 2
    q1 = f_yn_calc(q, b, z1, z2, y2b, so, n, c)
    q2 = f_yn_calc(q, b, z1, z2, y2c, so, n, c)
    if (sgn(q2) + sgn(q1)) == 0:
        y1a = y2b
    y2b = y2c

# Shape
shape = f_shape_type(b, z1, z2)

# Print results
results = f'\n{txt_separator(60)}\n{shape} >>> Results for Normal (n) an Critical (c) flow\n{txt_separator(60)}\n'
results += f'\nDepth (Y)\n'
results += f'    Yn ({c_unit_text}): {y2b}\n'
results += f'    Yc ({c_unit_text}): {y2}\n'
results += f'\nArea (A)\n'
results += f'    An ({c_unit_text}²): {f_area(b, z1, z2, y2b)}\n'
results += f'    Ac ({c_unit_text}²): {f_area(b, z1, z2, y2)}\n'
results += f'\nWet perimeter (P)\n'
results += f'    Pn ({c_unit_text}): {f_wet_perimeter(b, z1, z2, y2b)}\n'
results += f'    Pc ({c_unit_text}): {f_wet_perimeter(b, z1, z2, y2)}\n'
results += f'\nTop width (T)\n'
results += f'    Tn ({c_unit_text}): {f_top_width(b, z1, z2, y2b)}\n'
results += f'    Tc ({c_unit_text}): {f_top_width(b, z1, z2, y2)}\n'
results += f'\nHydraulic ratio\n    R = A / P\n'
results += f'    Rn ({c_unit_text}): {f_hydraulic_ratio(b, z1, z2, y2b)}\n'
results += f'    Rc ({c_unit_text}): {f_hydraulic_ratio(b, z1, z2, y2)}\n'
results += f'\nHydraulic depth\n    D = A / T\n'
results += f'    Dn ({c_unit_text}): {f_hydraulic_depth(b, z1, z2, y2b)}\n'
results += f'    Dc ({c_unit_text}): {f_hydraulic_depth(b, z1, z2, y2)}\n'
results += f'\nVelocity\n    V = Q / A\n'
results += f'    Vn ({c_unit_text}/s): {q / f_area(b, z1, z2, y2b)}\n'
results += f'    Vc ({c_unit_text}/s): {q / f_area(b, z1, z2, y2)}\n'
results += f'\nFroude Number\n    F = V / (g * D) ^ 0.5\n'
results += f'    Fn ({c_unit_text}): {f_froude_number(q / f_area(b, z1, z2, y2b), g, f_hydraulic_depth(b, z1, z2, y2b))}\n'
results += f'    Fc ({c_unit_text}): {f_froude_number(q / f_area(b, z1, z2, y2), g, f_hydraulic_depth(b, z1, z2, y2))}\n'
results += f'\nShear stress\n    τօ = ρ * g * rh * so\n'
results += f'    τn ({c_unit_text_shear_stress}): {f_shear_stress(rho, g, f_hydraulic_ratio(b, z1, z2, y2b), so)}\n'
results += f'    τc ({c_unit_text_shear_stress}): {f_shear_stress(rho, g, f_hydraulic_ratio(b, z1, z2, y2), so)}\n'
results += f'\nShape centroid & Hydraulic force\n    Fh = (Ycentroid * ρ * g) * A\n'
results += f'    Yn centroid ({c_unit_text}): {f_y_centroid(b, z1, z2, y2b)}\n'
results += f'    Yc centroid ({c_unit_text}): {f_y_centroid(b, z1, z2, y2)}\n'
results += f'    Fhn ({c_unit_text_shear_hydraulic_force}): {f_y_centroid(b, z1, z2, y2b) * g * rho * f_area(b, z1, z2, y2b)}\n'
results += f'    Fhc ({c_unit_text_shear_hydraulic_force}): {f_y_centroid(b, z1, z2, y2) * g * rho * f_area(b, z1, z2, y2)}\n'
results += f'\nProfile type & Critical slope\n    Sc = g * n ^ 2 * (Pc / Tc) / (c ^ 2 * Rc ^ (1 / 3))\n'
results += f'    Slope type: {f_profile_type(so, y2b, y2)}\n'
results += f'    Sc ({c_unit_text}/{c_unit_text}): {f_critic_slope(g, n, f_wet_perimeter(b, z1, z2, y2), f_top_width(b, z1, z2, y2), c, f_hydraulic_ratio(b, z1, z2, y2))}\n'
print(results)


# Developers
# r.cfdtools@gmail.com
# frank.velasco@escuelaing.edu.co
# juan.rodriguez@escuelaing.edu.co