# Solving with Bisection Method


# Area
def f_area(b, z1, z2, y):
    area = b * y + ((y ** 2) / 2) * (z1 + z2)
    return area

# Critical depth
def f_yc_calc(q, g, b, z1, z2, y, alpha):
    yc_calc = q - ((g * (f_area(b, z1, z2, y)) ** 3) / (alpha * f_top_width(b, z1, z2, y))) ** 0.5
    return yc_calc

# Normal depth
def f_yn_calc(q, b, z1, z2, y, sf, n, c):
    yn_calc = q - ((c / n) * (f_area(b, z1, z2, y)) * (f_hydraulic_ratio(b, z1, z2, y)) ** (2 / 3) * sf ** 0.5)
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

# Main vars
UnitSys = 'SI' # SI - International, US - Imperial/US
q = 1.5
g = 9.806
b = 1
z1 = 1
z2 = 1
sf = 0.0008969
n = 0.018
alpha = 1
y1 = 0.001
y2 = 10
steps = 32

# Pre validations
# Units system eval
if UnitSys == 'SI':
    c = 1
    c_unit_text = "m"
else:
    c = 1.486
    c_unit_text = "ft"
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
    q1 = f_yn_calc(q, b, z1, z2, y2b, sf, n, c)
    q2 = f_yn_calc(q, b, z1, z2, y2c, sf, n, c)
    if (sgn(q2) + sgn(q1)) == 0:
        y1a = y2b
    y2b = y2c

# Print results
results = f'\n{txt_separator(43)}\nResults for Normal (n) an Critical (c) Flow\n{txt_separator(43)}\n'
results += f'\nDepth (Y)\n'
results += f'    Yn({c_unit_text}): {y2b}\n'
results += f'    Yc({c_unit_text}): {y2}\n'
results += f'\nFlow area (A)\n'
results += f'    An({c_unit_text}²): {f_area(b, z1, z2, y2b)}\n'
results += f'    Ac({c_unit_text}²): {f_area(b, z1, z2, y2)}\n'
results += f'\nWet perimeter (P)\n'
results += f'    Pn({c_unit_text}): {f_wet_perimeter(b, z1, z2, y2b)}\n'
results += f'    Pc({c_unit_text}): {f_wet_perimeter(b, z1, z2, y2)}\n'
results += f'\nTop width (T)\n'
results += f'    Tn({c_unit_text}): {f_top_width(b, z1, z2, y2b)}\n'
results += f'    Tc({c_unit_text}): {f_top_width(b, z1, z2, y2)}\n'
results += f'\nHydraulic ratio (R = A / P)\n'
results += f'    Rn({c_unit_text}): {f_hydraulic_ratio(b, z1, z2, y2b)}\n'
results += f'    Rc({c_unit_text}): {f_hydraulic_ratio(b, z1, z2, y2)}\n'
results += f'\nHydraulic depth (D = A / T)\n'
results += f'    Dn({c_unit_text}): {f_hydraulic_depth(b, z1, z2, y2b)}\n'
results += f'    Dc({c_unit_text}): {f_hydraulic_depth(b, z1, z2, y2)}\n'
results += f'\nVelocity (V = Q / A)\n'
results += f'    Vn({c_unit_text}/s): {q / f_area(b, z1, z2, y2b)}\n'
results += f'    Vc({c_unit_text}/s): {q / f_area(b, z1, z2, y2)}\n'
results += f'\nFroude Number (F = V / (g * D) ^ 0.5)\n'
results += f'    Fn({c_unit_text}): {f_froude_number(q / f_area(b, z1, z2, y2b), g, f_hydraulic_depth(b, z1, z2, y2b))}\n'
results += f'    Fc({c_unit_text}): {f_froude_number(q / f_area(b, z1, z2, y2), g, f_hydraulic_depth(b, z1, z2, y2))}\n'
print(results)
