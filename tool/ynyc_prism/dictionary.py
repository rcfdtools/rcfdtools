# Dictionary definitions
# Author https://github.com/rcfdtools

# General
dicts = {
    'app_version': 'v20251206', # App control version
    'unit_sys': 'Units system',
    'c': 'c, units conversion factor',
    'Q': 'Q, flow',
    'g': 'g, gravity acceleration',
    'b': 'b, channel base',
    'z1': 'z1, left side slope',
    'z2': 'z2, right side slope',
    'So': 'So, channel slope',
    'n': 'n, channel roughness',
    'alpha': 'α, kinetic correction factor, alpha',
    'rho': 'ρ, fluid density, rho',
    'l': 'l, channel length',
    'z': 'z, ground level',
    'rcx': 'Rcx, river start x-coordinate',
    'rcy': 'Rcy, river start y-coordinate',
    'tb': 'Tb, flow duration (hours)',
    'ts': 'Ts, flow time step (minutes)',
    'tpp': 'Tpp, % time to peak flow discharge',
    'cell_size': 'Cell-size, DEM resolution for 2D perimeter internal buffer',
    'y1': 'y1, low elevation seed',
    'y2': 'y2, high elevation seed',
    'steps': 'Steps, step times',
    'D': 'D, hydraulic depth',
    'P': 'P, wet perimeter',
    'T': 'T, top width',
    'R': 'R, hydraulic ratio',
    'Yn': 'Yn, normal depth',
    'Yc': 'Yc, critical depth',
    'v': 'v, velocity',
    'Fr': 'Fr, Froude number',
    'A': 'A, geometric area',
    'τօ': 'τօ, shear stress, tau',
    'F': 'F, hydraulic force',
    'Sc': 'Sc, critical slope'
}

# Units in system international
units_si = {
    'c': 1,
    'q': 'm³/s',
    'length': 'm',
    'rho': 'kg/m³',
    'g': 'm/s²',
    'tau': 'Pa, N/m²', # Shear stress
    'f': 'N'# Hydraulic force, Newton
}

# Units in english or imperial system
units_us = {
    'c': 1.486,
    'q': 'ft³/s',
    'length': 'ft',
    'rho': 'lb/ft³',
    'g': 'ft/s²',
    'tau': 'lbf/ft²', # Shear stress
    'f': 'lbf'# Hydraulic force, Newton
}