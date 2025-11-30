# Functions
# Author https://github.com/rcfdtools

# Prismatic geometric shape type
def shape_type(b, z1, z2):
    if z1 == 0 and z2 == 0:
        shape_type = "RECTANGULAR"
    elif b == 0 and z1 > 0 and z2 > 0 and z1 == z2:
        shape_type = "TRIANGULAR"
    elif b > 0 and z1 > 0 and z2 > 0:
        shape_type = "TRAPEZOIDAL"
    else:
        shape_type = "DITCH"
    return shape_type

# Section area
def area(b, z1, z2, y):
    area = b * y + ((y ** 2) / 2) * (z1 + z2)
    return area

# Critical depth
def yc_calc(q, g, b, z1, z2, y, alpha):
    yc_calc = q - ((g * (area(b, z1, z2, y)) ** 3) / (alpha * top_width(b, z1, z2, y))) ** 0.5
    return yc_calc

# Normal depth
def yn_calc(q, b, z1, z2, y, so, n, c):
    yn_calc = q - ((c / n) * (area(b, z1, z2, y)) * (hydraulic_ratio(b, z1, z2, y)) ** (2 / 3) * so ** 0.5)
    return yn_calc

# Hydraulic ratio
def hydraulic_ratio(b, z1, z2, y):
    hydraulic_ratio = area(b, z1, z2, y) / wet_perimeter(b, z1, z2, y)
    return hydraulic_ratio

# Wet perimeter
def wet_perimeter(b, z1, z2, y):
    wet_perimeter = b + y * ((1 + z1 ** 2) ** 0.5 + (1 + z2 ** 2) ** 0.5)
    return wet_perimeter

# Superficial top width
def top_width(b, z1, z2, y):
    top_width = b + y * (z1 + z2)
    return top_width

# Hydraulic depth
def hydraulic_depth(b, z1, z2, y):
    hydraulic_depth = area(b, z1, z2, y) / top_width(b, z1, z2, y)
    return hydraulic_depth

# Froude number
def froude_number(v, g, d):
    froude_number = v / (g * d) ** 0.5
    if froude_number == 1:
        regime = 'Regime: Critical\nCritical flow control: Any'
    elif froude_number > 1:
        regime = 'Regime: Supercritical\nCritical flow control: Upstream'
    else:
        regime = 'Regime: Subcritical\nCritical flow control: Downstream'
    return [froude_number, regime]

# Profile type
def profile_type(s, yn, yc):
    if s == 0:
        fProfileType = 'H, Horizontal'
    else:
        if yn > yc: fProfileType = 'M, Mild' # Moderado
        if yn < yc: fProfileType = 'S, Steeped' # Escarpado
        if yn == yc: fProfileType = 'C, Critical' # Critico
        if s < 0: fProfileType = 'A, Adverse' #Adverso
    return fProfileType

# Critical slope
def critic_slope(g, n, pc, tc, c, rc):
    critic_slope = g * n ** 2 * (pc / tc) / (c ** 2 * rc ** (1 / 3))
    return critic_slope

# Shear stress
def shear_stress (rho, g, rh, so): # rh = hydraulic ratio
    shear_stress = rho * g * rh * so
    return shear_stress

# Centroidal depth
def y_centroid(b, z1, z2, y):
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

# Yc Calculation
def yc(steps, q, g, b, z1, z2, y2, y1, alpha):
    for i in range(steps):
        y2a = (y2 + y1) / 2
        q1 = yc_calc(q, g, b, z1, z2, y2, alpha)
        q2 = yc_calc(q, g, b, z1, z2, y2a, alpha)
        if (sgn(q1) + sgn(q2)) == 0:
            y1 = y2
        y2 = y2a
    return y2

# Yn Calculation
def yn(steps, q, b, z1, z2, y2b, y1a, so, n, c):
    for i in range(steps):
        y2c = (y2b + y1a) / 2
        q1 = yn_calc(q, b, z1, z2, y2b, so, n, c)
        q2 = yn_calc(q, b, z1, z2, y2c, so, n, c)
        if (sgn(q2) + sgn(q1)) == 0:
            y1a = y2b
        y2b = y2c
    return y2b

# Numeric absolute and null validation
def numeric_abs_none(number):
    if number is None:
        number = '0.00001'
    if not number:
        number = 0.00001
    if float(number) < 0:
        float(number) *= -1
    return number

# Numeric absolute and null validation
def numeric_float_none(number):
    if number is None:
        number = '0.00001'
    if not number:
        number = 0.00001
    return float(number)


# Results in console
def results(app_version, now, q, g, b, z1, z2, so, n, alpha, rho, y1aux, y2aux, steps, y2b, y2, shape, unit_sys, dicts, units):
    # Input values
    results = f'App version: {dicts['app_version']}\n'
    results += f'Runtime: {now}\n'
    results += f'\n{txt_separator(70)}\n{shape} SHAPE >>> Input values ({dicts['unit_sys']}: {unit_sys})\n{txt_separator(70)}\n\n'
    results += f'General parameters\n\n'
    results += f'{dicts['Q']}: {q} {units['q']}\n'
    results += f'{dicts['g']}: {g} {units['g']}\n'
    results += f'{dicts['b']}: {b} {units['length']}\n'
    results += f'{dicts['z1']}: {z1} {units['length']}\n'
    results += f'{dicts['z2']}: {z2} {units['length']}\n'
    results += f'{dicts['So']}: {so} {units['length']}/{units['length']}\n'
    results += f'{dicts['n']}: {n}\n'
    results += f'{dicts['alpha']}: {alpha}\n'
    results += f'{dicts['rho']}: {rho} {units['rho']}\n'
    results += f'{dicts['c']}: {units['c']}\n\n'
    results += f'Numerical method parameters\n\n'
    results += f'{dicts['y1']}: {y1aux} {units['length']}\n'
    results += f'{dicts['y2']}: {y2aux} {units['length']}\n'
    results += f'{dicts['steps']}: {steps}\n'
    # Results
    results += f'\n{txt_separator(70)}\nResults for Normal (n) an Critical (c) flow\n{txt_separator(70)}\n'
    results += f'\n● {dicts['Yn']}\n\n'
    results += f'Yn: {y2b} {units['length']}\n'
    results += f'\n● {dicts['Yc']}\n\n'
    results += f'Yc: {y2} {units['length']}\n'
    results += f'\n● {dicts['A']}\n\n'
    results += f'An: {area(b, z1, z2, y2b)} {units['length']}²\n'
    results += f'Ac: {area(b, z1, z2, y2)} {units['length']}²\n'
    results += f'\n● {dicts['P']}\n\n'
    results += f'Pn: {wet_perimeter(b, z1, z2, y2b)} {units['length']}\n'
    results += f'Pc: {wet_perimeter(b, z1, z2, y2)} {units['length']}\n'
    results += f'\n● {dicts['T']}\n\n'
    results += f'Tn: {top_width(b, z1, z2, y2b)} {units['length']}\n'
    results += f'Tc: {top_width(b, z1, z2, y2)} {units['length']}\n'
    results += f'\n● {dicts['R']}\n\nR = A / P\n'
    results += f'Rn: {hydraulic_ratio(b, z1, z2, y2b)} {units['length']}\n'
    results += f'Rc: {hydraulic_ratio(b, z1, z2, y2)} {units['length']}\n'
    results += f'\n● {dicts['D']}\n\nD = A / T\n'
    results += f'Dn: {hydraulic_depth(b, z1, z2, y2b)} {units['length']}\n'
    results += f'Dc: {hydraulic_depth(b, z1, z2, y2)} {units['length']}\n'
    results += f'\n● {dicts['V']}\n\nV = Q / A\n'
    results += f'Vn: {q / area(b, z1, z2, y2b)} {units['length']}/s\n'
    results += f'Vc: {q / area(b, z1, z2, y2)} {units['length']}/s\n'
    results += f'\n● {dicts['Fr']}\n\nFr = V / (g * D) ^ 0.5\n'
    results += f'Frn: {froude_number(q / area(b, z1, z2, y2b), g, hydraulic_depth(b, z1, z2, y2b))[0]}\n{froude_number(q / area(b, z1, z2, y2b), g, hydraulic_depth(b, z1, z2, y2b))[1]}\n'
    results += f'Frc: {froude_number(q / area(b, z1, z2, y2), g, hydraulic_depth(b, z1, z2, y2))[0]}\n'
    results += f'\n● {dicts['τօ']}\n\nτօ = ρ * g * R * so\n'
    results += f'τn: {shear_stress(rho, g, hydraulic_ratio(b, z1, z2, y2b), so)} {units['tau']}\n'
    results += f'τc: {shear_stress(rho, g, hydraulic_ratio(b, z1, z2, y2), so)} {units['tau']}\n'
    results += f'\n● {dicts['F']}\n\nF = (Ycentroid * ρ * g) * A\n'
    results += f'Yn centroid: {y_centroid(b, z1, z2, y2b)} {units['length']}\n'
    results += f'Yc centroid: {y_centroid(b, z1, z2, y2)} {units['length']}\n'
    results += f'Fn: {y_centroid(b, z1, z2, y2b) * g * rho * area(b, z1, z2, y2b)} {units['f']}\n'
    results += f'Fc: {y_centroid(b, z1, z2, y2) * g * rho * area(b, z1, z2, y2)} {units['f']}\n'
    results += f'\n● {dicts['Sc']}\n\nSc = g * n ^ 2 * (Pc / Tc) / (c ^ 2 * Rc ^ (1 / 3))\n'
    results += f'Sc: {critic_slope(g, n, wet_perimeter(b, z1, z2, y2), top_width(b, z1, z2, y2), units['c'], hydraulic_ratio(b, z1, z2, y2))} {units['length']}/{units['length']}\n'
    results += f'Slope type: {profile_type(so, y2b, y2)}\n'
    return results