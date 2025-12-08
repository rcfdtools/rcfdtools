# Functions
# Author https://github.com/rcfdtools

# Libraries
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
plt.rcParams['axes.spines.right'] = False
plt.rcParams['axes.spines.top'] = False
plt.rcParams['figure.facecolor'] = '#F4F4F4'

# Prismatic geometric shape type
def shape_type(b, z1, z2):
    if z1 == 0 and z2 == 0:
        shape_type = "Rectangular"
    elif b == 0 and z1 > 0 and z2 > 0 and z1 == z2:
        shape_type = "Triangular"
    elif b > 0 and z1 > 0 and z2 > 0:
        shape_type = "Trapezoidal"
    else:
        shape_type = "Ditch"
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

# Yc Calculation
def yc(steps, q, g, b, z1, z2, y2, y1, alpha):
    for i in range(steps):
        y2a = (y2 + y1) / 2
        q1 = yc_calc(q, g, b, z1, z2, y2, alpha)
        q2 = yc_calc(q, g, b, z1, z2, y2a, alpha)
        if (sgn(q1) + sgn(q2)) == 0:
            y1 = y2
        y2 = y2a
        #print(f'>>>> Step {i}, Yc: {y2}') # Explicit Test
    return y2

# Yn Calculation
def yn(steps, q, b, z1, z2, y2b, y1a, so, n, c):
    if so != 0:
        for i in range(steps):
            y2c = (y2b + y1a) / 2
            q1 = yn_calc(q, b, z1, z2, y2b, so, n, c)
            q2 = yn_calc(q, b, z1, z2, y2c, so, n, c)
            if (sgn(q2) + sgn(q1)) == 0:
                y1a = y2b
            y2b = y2c
            # print(f'>>>> Step {i}, Yn: {y2b}')  # Explicit Test
    else:
        y2b = 999999

    return y2b

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

# Numeric absolute and null validation
def numeric_abs_none(number):
    if number is None or not number:
        number = '0'
    number = float(number)
    if number < 0:
        number *= -1
    return number

# Numeric float and null validation
def numeric_float_none(number):
    if number is None or not number:
        number = '0'
    return float(number)

# Cross-section plot
def cross_section_plot(y2, y2b, b, z1, z2, units, z, l):
    if y2b < y2: # Yn > Yc
        max_elevation = y2
    else:
        max_elevation = y2b
    valley_side_length = 0.25 * (max_elevation * z1 + b + max_elevation * z2) # 20% side length
    ground_x_values = [0, valley_side_length, valley_side_length+(max_elevation * z1), valley_side_length+(max_elevation * z1 + b), valley_side_length+(max_elevation * z1 + b + max_elevation * z2), (valley_side_length*2)+(max_elevation * z1 + b + max_elevation * z2)]
    ground_y_values = [z+max_elevation, z+max_elevation, z, z, z+max_elevation, z+max_elevation]
    yn_y_values = [z+y2b, z+y2b, z+y2b, z+y2b, z+y2b, z+y2b]
    yc_y_values = [z+y2, z+y2, z+y2, z+y2, z+y2, z+y2]
    figure(figsize=(7, 5), dpi=60)
    plt.plot(ground_x_values, ground_y_values, color='black', label='Ground', linewidth=1.5, marker='o', markersize=4)
    plt.plot(ground_x_values, yn_y_values, color='#3A78E6', label='Yn', linewidth=1, linestyle='--')
    plt.plot(ground_x_values, yc_y_values, color='#DD3C2A', label='Yc', linewidth=1, linestyle='--')
    plt.text(0, z+y2b, round(y2b, 6), color='black', ha='left')
    plt.text(0, z+y2, round(y2, 6), color='black', ha='left')
    plt.title(f'{shape_type(b, z1, z2)} cross-section')
    plt.xlabel(f'Station ({units['length']})')
    plt.ylabel(f'Elevation ({units['length']})')
    plt.legend(frameon=False)
    # eval Yn > Yc for water fill
    ground_y_values = [z+y2b, z+y2b, z, z, z+y2b, z+y2b]
    if y2b < y2: # Yn < Yc
        ground_x_values = [valley_side_length+(y2-y2b)*z1, valley_side_length++(y2-y2b)*z1, valley_side_length+(max_elevation * z1),  valley_side_length+(max_elevation * z1 + b), valley_side_length+(max_elevation * z1 + b) + y2b*z2, (valley_side_length*2)+(max_elevation * z1 + b) + y2b*z2]
    plt.fill_between(ground_x_values, ground_y_values, yn_y_values, color='lightblue', alpha=0.5, label='Filled Area')
    plt.rcParams['axes.spines.left'] = True
    plt.rcParams['axes.spines.right'] = False
    plt.rcParams['axes.spines.top'] = False
    plt.rcParams['axes.spines.bottom'] = True
    plt.grid(True, linewidth=0.2, alpha=0.5)
    return plt

# Cross-section table for HEC-RAS
def cross_section_table(y2, y2b, b, z1, z2, units, z, l, so, rcx, rcy):
    # coss-section
    river_name = 'River1'
    reach_name = 'Reach1'
    z_less = l * so
    rounding = 6
    if y2b < y2: # Yn > Yc
        max_elevation = y2
    else:
        max_elevation = y2b
    valley_side_length = 0.25 * (max_elevation * z1 + b + max_elevation * z2)  # 20% side length
    ground_x_values = [0, valley_side_length, valley_side_length+max_elevation * z1, valley_side_length+max_elevation * z1 + b, valley_side_length+max_elevation * z1 + b + max_elevation * z2, (valley_side_length*2)+max_elevation * z1 + b + max_elevation * z2]
    ground_y_values = [z + max_elevation, z + max_elevation, z, z, z + max_elevation, z + max_elevation]
    xs_table = f'{txt_separator(70)}\nHEC-RAS 1D cross-sections & river\n{txt_separator(70)}\n\n● Coss-section values\nSave the following table as a .txt or .csv file.\nFile / Import Geometry Data: CSV (Comma Separate Value) Format.\n\n'
    xs_table += f'River, Reach, RS, Station, Elevation\n'
    for i in range(len(ground_x_values)):
        xs_table += f'{river_name}, {reach_name}, 0, {round(ground_x_values[i],rounding)}, {round(ground_y_values[i], rounding)}\n'
    for i in range(len(ground_x_values)):
        xs_table += f'{river_name}, {reach_name}, {l}, {round(ground_x_values[i],rounding)}, {round(ground_y_values[i],rounding)+z_less}\n'
    # river axe
    xs_table += f'\n● River coordinates\nCopy and paste the following values.\nGIS Tools / Reach Invert Lines Table...\n\n'
    xs_table += f'Schematic X, Schematic Y\n'
    xs_table += f'{rcx+l}, {rcy}\n'
    xs_table += f'{rcx}, {rcy}\n'
    return xs_table

# Distributed flow with a triangular unitary hydrograph (UH) for HEC-RAS
def distributed_flow(q, tb, ts, tpp, units):
    rounding = 6
    tp = tb*(tpp/100) # time to peak in hours
    steps = int(tb/(ts/60)) # time steps
    hydrograph_slope_left = q/tp
    hydrograph_slope_right = q/(tb-tp)
    hydrograph_table = f'\n● Distributed flow with a triangular unitary hydrograph (UH)\n'
    hydrograph_table += f'Time to peak (hr): {tp}\n\n'
    hydrograph_table += f'Step, Time (hr), Flow ({units['q']})\n'
    for i in range (steps+1):
        tsa = ts*i/60 # progressive time step
        if tsa <= tp:
            qt = ts*i/60 * hydrograph_slope_left
        else:
            qt = q - (tsa - tp) * hydrograph_slope_right
        hydrograph_table += f'{i+1}, {round(tsa, rounding)}, {round(qt, rounding)}\n'
    return  hydrograph_table

# Results in console
def results(app_version, now, q, g, b, z1, z2, so, n, alpha, rho, y1aux, y2aux, steps, y2b, y2, shape, unit_sys, dicts, units, z, l, rcx, rcy, tb, ts, tpp):
    # Input values
    results = f'App version: {dicts['app_version']}\n'
    results += f'Runtime: {now}\n\n'
    results += f'{txt_separator(70)}\nInput values ({dicts['unit_sys']}: {unit_sys})\n{txt_separator(70)}\n'
    results += f'(input parameters can be adjusted during the validation process)\n\n'
    results += f'● General parameters\n'
    results += f'Shape: {shape}\n'
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
    results += f'● HEC-RAS parameters\n'
    results += f'{dicts['l']}: {l} {units['length']}\n'
    results += f'{dicts['z']}: {z} {units['length']}\n'
    results += f'{dicts['rcx']}: {rcx} {units['length']}\n'
    results += f'{dicts['rcy']}: {rcy} {units['length']}\n'
    results += f'{dicts['tb']}: {tb}\n'
    results += f'{dicts['ts']}: {ts}\n'
    results += f'{dicts['tpp']}: {tpp}\n\n'
    results += f'● Numerical method parameters\n'
    results += f'{dicts['y1']}: {y1aux} {units['length']}\n'
    results += f'{dicts['y2']}: {y2aux} {units['length']}\n'
    results += f'{dicts['steps']}: {steps}\n'
    # Results
    results += f'\n{txt_separator(70)}\nResults for Normal (n) an Critical (c) flow\n{txt_separator(70)}\n'
    results += f'\n● {dicts['Yn']}\n'
    results += f'Yn: {y2b} {units['length']}\n'
    results += f'\n● {dicts['Yc']}\n'
    results += f'Yc: {y2} {units['length']}\n'
    results += f'\n● {dicts['A']}\n'
    results += f'An: {area(b, z1, z2, y2b)} {units['length']}²\n'
    results += f'Ac: {area(b, z1, z2, y2)} {units['length']}²\n'
    results += f'\n● {dicts['P']}\n'
    results += f'Pn: {wet_perimeter(b, z1, z2, y2b)} {units['length']}\n'
    results += f'Pc: {wet_perimeter(b, z1, z2, y2)} {units['length']}\n'
    results += f'\n● {dicts['T']}\n'
    results += f'Tn: {top_width(b, z1, z2, y2b)} {units['length']}\n'
    results += f'Tc: {top_width(b, z1, z2, y2)} {units['length']}\n'
    results += f'\n● {dicts['R']}\nR = A / P\n'
    results += f'Rn: {hydraulic_ratio(b, z1, z2, y2b)} {units['length']}\n'
    results += f'Rc: {hydraulic_ratio(b, z1, z2, y2)} {units['length']}\n'
    results += f'\n● {dicts['D']}\nD = A / T\n'
    results += f'Dn: {hydraulic_depth(b, z1, z2, y2b)} {units['length']}\n'
    results += f'Dc: {hydraulic_depth(b, z1, z2, y2)} {units['length']}\n'
    results += f'\n● {dicts['v']}\nv = Q / A\n'
    results += f'vn: {q / area(b, z1, z2, y2b)} {units['length']}/s\n'
    results += f'vc: {q / area(b, z1, z2, y2)} {units['length']}/s\n'
    results += f'\n● {dicts['Fr']}\nFr = v / √(g * D)\n'
    results += f'Frn: {froude_number(q / area(b, z1, z2, y2b), g, hydraulic_depth(b, z1, z2, y2b))[0]}\n{froude_number(q / area(b, z1, z2, y2b), g, hydraulic_depth(b, z1, z2, y2b))[1]}\n'
    results += f'Frc: {froude_number(q / area(b, z1, z2, y2), g, hydraulic_depth(b, z1, z2, y2))[0]}\n'
    results += f'\n● {dicts['τօ']}\nτօ = ρ * g * R * so\n'
    results += f'τn: {shear_stress(rho, g, hydraulic_ratio(b, z1, z2, y2b), so)} {units['tau']}\n'
    results += f'τc: {shear_stress(rho, g, hydraulic_ratio(b, z1, z2, y2), so)} {units['tau']}\n'
    results += f'\n● {dicts['F']}\nF = (Ycentroid * ρ * g) * A\n'
    results += f'Yn centroid: {y_centroid(b, z1, z2, y2b)} {units['length']}\n'
    results += f'Yc centroid: {y_centroid(b, z1, z2, y2)} {units['length']}\n'
    results += f'Fn: {y_centroid(b, z1, z2, y2b) * g * rho * area(b, z1, z2, y2b)} {units['f']}\n'
    results += f'Fc: {y_centroid(b, z1, z2, y2) * g * rho * area(b, z1, z2, y2)} {units['f']}\n'
    results += f'\n● {dicts['Sc']}\nSc = g * n ^ 2 * (Pc / Tc) / (c ^ 2 * Rc ^ (1 / 3))\n'
    results += f'Sc: {critic_slope(g, n, wet_perimeter(b, z1, z2, y2), top_width(b, z1, z2, y2), units['c'], hydraulic_ratio(b, z1, z2, y2))} {units['length']}/{units['length']}\n'
    results += f'Slope type: {profile_type(so, y2b, y2)}\n'
    results += f'\n{cross_section_table(y2, y2b, b, z1, z2, units, z, l, so, rcx, rcy)}'
    results += distributed_flow(q, tb, ts, tpp, units)
    return results