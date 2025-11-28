# Functions

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

# Froud number
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
