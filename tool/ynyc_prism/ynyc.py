# Yn Yc: solved with Bisection Method
# Author https://github.com/rcfdtools

# Libraries
from datetime import datetime
import dictionary as dictionary
import functions as funcs
import matplotlib.pyplot as plt

# Main vars
unit_sys = 'SI' # SI - International, US - Imperial/US
q = 10 # Flow
g = 9.806 # Gravity acceleration
b = 1 # Channel base
z1 = 1 # Left side slope
z2 = 1 # Right side slope
so = 0.0008969 # Channel slope
n = 0.035 # Channel roughness
alpha = 1 # Kinetic correction factor
rho = 1000 # ρ: fluid density
y1 = 0.0001 # Numerical method, low elevation seed
y2 = 1000 # Numerical method, high elevation seed
steps = 128 # Numerical method, steps

# Pre validations
dicts = dictionary.dicts
q = funcs.numeric_abs_none(q)
g = funcs.numeric_abs_none(g)
b = funcs.numeric_abs_none(b)
z1 = funcs.numeric_float_none(z1)
z2 = funcs.numeric_float_none(z2)
so = funcs.numeric_abs_none(so)
n = funcs.numeric_abs_none(n)
alpha = funcs.numeric_abs_none(alpha)
rho = funcs.numeric_abs_none(rho)
y1 = funcs.numeric_abs_none(y1)
y2 = funcs.numeric_abs_none(y2)
steps = int(funcs.numeric_abs_none(steps))
if unit_sys.upper() == 'SI': # Units system eval
    units = dictionary.units_si
else:
    units = dictionary.units_us
if alpha == 0: alpha = 1 # alpha validation
y1aux, y2aux = y1, y2
y1a = y1
if y2 < y1: # eval y2 > y1
    y1, y2 = y2, y1a
if steps <= 0: steps = 64 # eval # step iterations > 0
y1a, y2b = y1, y2

# Yc Calculation
y2 = funcs.yc(steps, q, g, b, z1, z2, y2, y1, alpha)

# Yn Calculation
y2b = funcs.yn(steps, q, b, z1, z2, y2b, y1a, so, n, units['c'])

# Print results in console
results = funcs.results(dict['app_version'], datetime.now(), q, g, b, z1, z2, so, n, alpha, rho, y1aux, y2aux, steps, y2b, y2, funcs.shape_type(b, z1, z2), unit_sys, dicts, units)
print(results)

# Cross section, station vs elevation
if y2 > y2b:
    max_elevation = y2
else:
    max_elevation = y2b
x_values = [0, max_elevation*z1, max_elevation*z1+b, max_elevation*z1+b+max_elevation*z2]
ground_x_values = x_values
ground_y_values = [max_elevation,0,0,max_elevation]
yn_x_values = x_values
yn_y_values = [y2b, y2b, y2b, y2b]
yc_x_values = x_values
yc_y_values = [y2, y2, y2, y2]
plt.plot(ground_x_values, ground_y_values, color='#2B9D4D', label='Ground', linewidth=1.5, marker='o', markersize=4)
plt.plot(yn_x_values, yn_y_values, color='#3A78E6', label='Yn', linewidth=1,  linestyle='--')
plt.plot(yc_x_values, yc_y_values, color='#DD3C2A', label='Yc', linewidth=1,  linestyle='--')
plt.text(max_elevation*z1+b/2, y2b, round(y2b, 6), color='#3A78E6', ha='center')
plt.text(max_elevation*z1+b/2, y2, round(y2, 6), color='#DD3C2A', ha='center')
plt.title(f'{funcs.shape_type(b, z1, z2)} cross section geometry')
plt.xlabel(f'Station ({units['length']})')
plt.ylabel(f'Elevation ({units['length']})')
plt.legend(frameon=False)
plt.fill_between(ground_x_values, ground_y_values, yn_y_values, color='lightblue', alpha=0.5, label='Filled Area')
# plt.axis('off')
plt.rcParams['axes.spines.left'] = True
plt.rcParams['axes.spines.right'] = False
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.bottom'] = True
plt.grid(True, linewidth=0.2, alpha=0.5)
plt.show()



