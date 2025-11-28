# Yn Yc: solved with Bisection Method

# Main vars
UnitSys = 'SI' # SI - International, US - Imperial/US
q = 10 # Flow
g = 9.806 # Gravity acceleration
b = 5 # Channel base
z1 = 2 # Left side slope
z2 = 2 # Right side slope
so = 0.0008969 # Channel slope
n = 0.035 # Channel roughness
alpha = 1 # Kinetic correction factor
rho = 1000 # ρ: fluid density, kg/m³, lb/ft³
y1 = 0.001 # Numerical method, low elevation seed
y2 = 10 # Numerical method, high elevation seed
steps = 32 # Numerical method, steps

# Dictionary definitions
dictionary = {
    'Q': '(Q)  Flow',
    'g': '(g)  Gravity acceleration',
    'b': '(b)  Channel base',
    'z1': '(z1) Left side slope',
    'z2': '(z2) Right side slope',
    'So': '(So) Channel slope',
    'n': '(n) Channel roughness',
    'alpha': '(α) Kinetic correction factor, aplha',
    'rho': '(ρ) Kinetic correction factor, rho',
    'y1': '(Y1) Numerical method, low elevation seed',
    'y2': '(Y2) Numerical method, high elevation seed',
    'steps': '(Steps) Numerical method, step times',

    'D': 'Hydraulic depth (D) is the ratio of the cross-sectional area of flow A to the top width T of the water surface, expressed as D=A/T. It is a key parameter in open channel hydraulics, particularly useful for calculating things like the Froude number and energy relationships, while hydraulic radius is used for frictional losses. In a rectangular channel, the hydraulic depth is simply equal to the vertical depth of the flow.',

    'P': 'Wet perimeter (P) is the length of the channel boundary that is in contact with the fluid flowing through it. This includes the bottom and sides of the channel or pipe, but not the free surface of the water. It is a key factor in fluid mechanics for calculating a channel hydraulic radius and understanding friction losses in open channel and pipe flow.',

    'T': 'Top width (T) is the horizontal width at the waters surface. It is a critical measurement used in hydraulics to calculate other channel properties like the flow area and hydraulic depth. For a simple rectangular channel, the top width is the same as the bottom width, but for a trapezoidal channel, it is calculated by adding twice the horizontal run of the side slopes to the bottom width.',

    'R': 'Hydraulic ratio (R) is the ratio of the cross-sectional area of the flow to the wetted perimeter. It is calculated as R=A/P, where A is the flow area and P is the wetted perimeter. This value indicates the efficiency of a channel in transporting water, with a higher hydraulic radius leading to increased flow velocity and capacity.',

    'Yn': 'Normal depth (Yn) is the constant depth of water in an open channel where the flow is steady and uniform, meaning the water surface slope, channel bottom slope, and energy grade line slope are all equal. This occurs when the forces of gravity and friction are balanced, and the flow velocity is not accelerating or decelerating. It is a crucial concept for engineers designing drainage systems and other hydraulic structures, and it is typically calculated using Mannings equation.',

    'Yc': 'Critical depth (Yc) is the flow depth in an open channel where specific energy is at a minimum for a given discharge. It is the transition point between subcritical flow (where the depth is greater than critical depth) and supercritical flow (where the depth is less than critical depth). Understanding critical depth is vital for designing channels and predicting how water will flow through hydraulic structures.',

    'V': 'Velocity is the speed of the fluid, which varies across the cross-section, being zero at the boundaries and increasing towards the free surface. It is calculated using formulas like the Mannings equation, which considers the channels hydraulic radius, slope, and roughness. The mean velocity is often used for design and can be estimated by averaging velocities at specific depths, such as 0.2 and 0.8 of the total depth, or by taking the velocity at 0.6 of the depth from the surface.',

    'Fr': 'Froude number (Fr) in open channels is a dimensionless value that compares inertial forces to gravitational forces to determine the flow regime: subcritical Fr<1, critical F=1, or supercritical Fr>1. It is calculated as the ratio of the flow velocity to the wave velocity, with velocity being the flow speed V and wave velocity being √gD, where g is the acceleration due to gravity and D is the hydraulic depth A/T.',

    'A': 'The geometric area (A) of a channel is the cross-sectional area of the flow, which represents the space occupied by the fluid as it moves through the channel. It is a crucial parameter for understanding how much water can pass through a channel at any given time.',

    'τօ': 'Shear stress (τօ) in channels is the force exerted by a fluid flowing over a surface, acting parallel to that surface and causing a drag or friction force. It is calculated as the force per unit area and is a measure of the fluids resistance to flow, which can erode the channel bed or be a factor in sediment transport. The stress is also present between layers of the fluid itself and is influenced by factors like fluid viscosity, flow depth, channel slope, and turbulence.',

    'F': 'Hydraulic force (F) in open channels, hydraulic force is the force exerted by the flowing water, which is driven primarily by gravity and influenced by pressure and shear stress. This force is essential for understanding and designing channels, as it can be used to measure discharge, control water levels, and dissipate energy through structures like hydraulic jumps.',

    'Sc': 'Critical slope (Sc) in open channels is the specific bed slope at which the normal depth of flow Yn is equal to the critical depth Yc. At this slope, the flow is uniform and critical, with a Froude number of 1. It serves as a boundary to classify a channels slope as "mild" So<Sc, where normal depth is greater than critical depth Yn>Yc, or "steep" So>Sc, where normal depth is less than critical depth Yn<Yc.'
}

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
    if froude_number == 1:
        regime = 'Critical'
    elif froude_number > 1:
        regime = 'Supercritical'
    else:
        regime = 'Subcritical'
    return [froude_number, regime]

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
results = f'\n{txt_separator(80)}\n{shape} >>> Results for Normal (n) an Critical (c) flow\n{txt_separator(80)}\n'
results += f'\n● Normal and critical depth (Y)\n\n{dictionary['Yn']}\n\n{dictionary['Yc']}\n\n'
results += f'    Yn ({c_unit_text}): {y2b}\n'
results += f'    Yc ({c_unit_text}): {y2}\n'
results += f'\n● Area (A)\n\n{dictionary['A']}\n\n'
results += f'    An ({c_unit_text}²): {f_area(b, z1, z2, y2b)}\n'
results += f'    Ac ({c_unit_text}²): {f_area(b, z1, z2, y2)}\n'
results += f'\n● Wet perimeter (P)\n\n{dictionary['P']}\n\n'
results += f'    Pn ({c_unit_text}): {f_wet_perimeter(b, z1, z2, y2b)}\n'
results += f'    Pc ({c_unit_text}): {f_wet_perimeter(b, z1, z2, y2)}\n'
results += f'\n● Top width (T)\n\n{dictionary['T']}\n\n'
results += f'    Tn ({c_unit_text}): {f_top_width(b, z1, z2, y2b)}\n'
results += f'    Tc ({c_unit_text}): {f_top_width(b, z1, z2, y2)}\n'
results += f'\n● Hydraulic ratio (R)\n\n{dictionary['R']}\n\n    R = A / P\n'
results += f'    Rn ({c_unit_text}): {f_hydraulic_ratio(b, z1, z2, y2b)}\n'
results += f'    Rc ({c_unit_text}): {f_hydraulic_ratio(b, z1, z2, y2)}\n'
results += f'\n● Hydraulic depth (D)\n\n{dictionary['D']}\n\n    D = A / T\n'
results += f'    Dn ({c_unit_text}): {f_hydraulic_depth(b, z1, z2, y2b)}\n'
results += f'    Dc ({c_unit_text}): {f_hydraulic_depth(b, z1, z2, y2)}\n'
results += f'\n● Velocity (V)\n\n{dictionary['V']}\n\n    V = Q / A\n'
results += f'    Vn ({c_unit_text}/s): {q / f_area(b, z1, z2, y2b)}\n'
results += f'    Vc ({c_unit_text}/s): {q / f_area(b, z1, z2, y2)}\n'
results += f'\n● Froude Number (Fr)\n\n{dictionary['Fr']}\n\n    Fr = V / (g * D) ^ 0.5\n'
results += f'    Frn: {f_froude_number(q / f_area(b, z1, z2, y2b), g, f_hydraulic_depth(b, z1, z2, y2b))[0]} {f_froude_number(q / f_area(b, z1, z2, y2b), g, f_hydraulic_depth(b, z1, z2, y2b))[1]}\n'
results += f'    Frc: {f_froude_number(q / f_area(b, z1, z2, y2), g, f_hydraulic_depth(b, z1, z2, y2))[0]} {f_froude_number(q / f_area(b, z1, z2, y2), g, f_hydraulic_depth(b, z1, z2, y2))[1]}\n'
results += f'\n● Shear stress (τօ)\n\n{dictionary['τօ']}\n\n    τօ = ρ * g * R * so\n'
results += f'    τn ({c_unit_text_shear_stress}): {f_shear_stress(rho, g, f_hydraulic_ratio(b, z1, z2, y2b), so)}\n'
results += f'    τc ({c_unit_text_shear_stress}): {f_shear_stress(rho, g, f_hydraulic_ratio(b, z1, z2, y2), so)}\n'
results += f'\n● Geometry vertical centroid & Hydraulic force (F)\n\n{dictionary['F']}\n\n    F = (Ycentroid * ρ * g) * A\n'
results += f'    Yn centroid ({c_unit_text}): {f_y_centroid(b, z1, z2, y2b)}\n'
results += f'    Yc centroid ({c_unit_text}): {f_y_centroid(b, z1, z2, y2)}\n'
results += f'    Fn ({c_unit_text_shear_hydraulic_force}): {f_y_centroid(b, z1, z2, y2b) * g * rho * f_area(b, z1, z2, y2b)}\n'
results += f'    Fc ({c_unit_text_shear_hydraulic_force}): {f_y_centroid(b, z1, z2, y2) * g * rho * f_area(b, z1, z2, y2)}\n'
results += f'\n● Profile type & Critical slope (Sc)\n\n{dictionary['Sc']}\n\n    Sc = g * n ^ 2 * (Pc / Tc) / (c ^ 2 * Rc ^ (1 / 3))\n'
results += f'    Sc ({c_unit_text}/{c_unit_text}): {f_critic_slope(g, n, f_wet_perimeter(b, z1, z2, y2), f_top_width(b, z1, z2, y2), c, f_hydraulic_ratio(b, z1, z2, y2))}\n'
results += f'    Slope type: {f_profile_type(so, y2b, y2)}\n'
print(results)


# Developers
# github.com/rcfdtools
# github.com/frankv13
# github.com/juanrodace