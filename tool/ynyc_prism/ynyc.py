# Yn Yc: solved with Bisection Method
# Author https://github.com/rcfdtools

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
l = 100 # l: channel length for HEC-RAS
z = 2600 # z: ground level for HEC-RAS
rcx = 5000000  # river start coordinate x for HEC-RAS
rcy = 2000000  # river start coordinate y for HEC-RAS
tb = 8 # flow duration in hours for HEC-RAS
ts = 30 # flow time step (minutes) for HEC-RAS
tpp = 37.5 # % time to peak flow discharge for HEC-RAS
cell_size = 0.1 # DEM resolution for 2D perimeter internal buffer
y1 = 0.0001 # Numerical method, low elevation seed
y2 = 5 # Numerical method, high elevation seed
steps = 64 # Numerical method, steps

# Pre validations
dicts = dictionary.dicts
q = funcs.numeric_abs_none(q)
g = funcs.numeric_abs_none(g)
b = funcs.numeric_abs_none(b)
z1 = funcs.numeric_float_none(z1)
z2 = funcs.numeric_float_none(z2)
so = funcs.numeric_float_none(so)
n = funcs.numeric_abs_none(n)
alpha = funcs.numeric_abs_none(alpha)
rho = funcs.numeric_abs_none(rho)
l = funcs.numeric_abs_none(l)
z = funcs.numeric_abs_none(z)
rcx = funcs.numeric_abs_none(rcx)
rcy = funcs.numeric_abs_none(rcy)
tb = funcs.numeric_abs_none(tb)
ts = funcs.numeric_abs_none(ts)
tpp = funcs.numeric_abs_none(tpp)
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
results = funcs.results(dict['app_version'], datetime.now(), q, g, b, z1, z2, so, n, alpha, rho, y1aux, y2aux, steps, y2b, y2, funcs.shape_type(b, z1, z2), unit_sys, dicts, units, z, l, rcx, rcy, tb, ts, tpp, cell_size)
print(results)

# Cross-section plot
plot = funcs.cross_section_plot(y2, y2b, b, z1, z2, units, z, l)
plot.show()
plot.close()

