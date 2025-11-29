# Yn Yc: solved with Bisection Method
# Developers: github.com/rcfdtools, github.com/frankv13, github.com/juanrodace

# Libraries
from datetime import datetime
import dictionary as dictionary
import functions as funcs 

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
y1 = 0.0001 # Numerical method, low elevation seed
y2 = 10 # Numerical method, high elevation seed
steps = 64 # Numerical method, steps

# Pre validations
dicts = dictionary.dicts
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
