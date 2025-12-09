# Yn Yc: solved with Bisection Method
# Author https://github.com/rcfdtools

# Libraries
from datetime import datetime
import dictionary as dictionary
import functions as funcs
from pyscript import document
from pyscript import display


def run(event):

    # read fields from html page
    input_unit_sys = document.querySelector("#unit_sys")
    input_q = document.querySelector("#q") # q total, not unitary value
    input_g = document.querySelector("#g")
    input_b = document.querySelector("#b")
    input_z1 = document.querySelector("#z1")
    input_z2 = document.querySelector("#z2")
    input_so = document.querySelector("#so")
    input_n = document.querySelector("#n")
    input_alpha = document.querySelector("#alpha")
    input_rho = document.querySelector("#rho")
    input_l = document.querySelector("#l")
    input_z = document.querySelector("#z")
    input_rcx = document.querySelector("#rcx")
    input_rcy = document.querySelector("#rcy")
    input_tb = document.querySelector("#tb")
    input_ts = document.querySelector("#ts")
    input_tpp = document.querySelector("#tpp")
    input_cell_size = document.querySelector("#cell_size")
    input_y1 = document.querySelector("#y1")
    input_y2 = document.querySelector("#y2")
    input_steps = document.querySelector("#steps")

    # read fields values
    unit_sys = input_unit_sys.value # SI - International, US - Imperial/US
    q = input_q.value # Flow
    g = input_g.value # Gravity acceleration
    b = input_b.value # Channel base
    z1 = input_z1.value # Left side slope
    z2 = input_z2.value # Right side slope
    so = input_so.value # Channel slope
    n = input_n.value # Channel roughness
    alpha = input_alpha.value # Kinetic correction factor
    rho = input_rho.value # ρ: fluid density
    l = input_l.value  # channel length for HEC-RAS
    z = input_z.value  # ground level for HEC-RAS
    rcx = input_rcx.value  # river start coordinate x for HEC-RAS
    rcy = input_rcy.value  # river start coordinate y for HEC-RAS
    tb = input_tb.value  # flow duration in hours for HEC-RAS
    ts = input_ts.value  # flow time step (minutes) for HEC-RAS
    tpp = input_tpp.value  # % time to peak flow discharge for HEC-RAS
    cell_size = input_cell_size.value  # DEM resolution for 2D perimeter internal buffer
    y1 = input_y1.value # Numerical method, low elevation seed
    y2 = input_y2.value # Numerical method, high elevation seed
    steps = input_steps.value # Numerical method, steps

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
    l = funcs.numeric_abs_none(l)
    z = funcs.numeric_abs_none(z)
    rcx = funcs.numeric_abs_none(rcx)
    rcy = funcs.numeric_abs_none(rcy)
    tb = funcs.numeric_abs_none(tb)
    ts = funcs.numeric_abs_none(ts)
    tpp = funcs.numeric_abs_none(tpp)
    cell_size = funcs.numeric_abs_none(cell_size)
    y1 = funcs.numeric_abs_none(y1)
    y2 = funcs.numeric_abs_none(y2)
    steps = int(funcs.numeric_abs_none(steps))
    dicts = dictionary.dicts
    if unit_sys.upper() == 'SI':  # Units system eval
        units = dictionary.units_si
    else:
        units = dictionary.units_us
    if alpha == 0: alpha = 1  # alpha validation
    y1aux, y2aux = y1, y2
    y1a = y1
    if y2 < y1:  # eval y2 > y1
        y1, y2 = y2, y1a
    if steps <= 0: steps = 64  # eval # step iterations > 0
    y1a, y2b = y1, y2

    # Yc Calculation
    y2 = funcs.yc(steps, q, g, b, z1, z2, y2, y1, alpha)

    # Yn Calculation
    y2b = funcs.yn(steps, q, b, z1, z2, y2b, y1a, so, n, units['c'])

    # Print results in console
    results = funcs.results(dict['app_version'], datetime.now(), q, g, b, z1, z2, so, n, alpha, rho, y1aux, y2aux,
                            steps, y2b, y2, funcs.shape_type(b, z1, z2), unit_sys, dicts, units, z , l, rcx, rcy, tb, ts, tpp, cell_size)
    output_div = document.querySelector("#output")
    output_div.innerText = results

    # Cross-section plot
    plot = funcs.cross_section_plot(y2, y2b, b, z1, z2, units, z, l)
    display(plot, target='plot1', append="False")
    plot.close()
