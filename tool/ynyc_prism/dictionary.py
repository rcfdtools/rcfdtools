# Dictionary definitions
dictionary = {
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

    'y1': 'y1, low elevation seed',

    'y2': 'y2, high elevation seed',

    'steps': 'Steps, step times',

    'D': 'Hydraulic depth (D)\n\nIs the ratio of the cross-sectional area of flow A to the top width T of the water surface, expressed as D=A/T. It is a key parameter in open channel hydraulics, particularly useful for calculating things like the Froude number and energy relationships, while hydraulic radius is used for frictional losses. In a rectangular channel, the hydraulic depth is simply equal to the vertical depth of the flow.',

    'P': 'Wet perimeter (P)\n\nIs the length of the channel boundary that is in contact with the fluid flowing through it. This includes the bottom and sides of the channel or pipe, but not the free surface of the water. It is a key factor in fluid mechanics for calculating a channel hydraulic radius and understanding friction losses in open channel and pipe flow.',

    'T': 'Top width (T)\n\nIs the horizontal width at the waters surface. It is a critical measurement used in hydraulics to calculate other channel properties like the flow area and hydraulic depth. For a simple rectangular channel, the top width is the same as the bottom width, but for a trapezoidal channel, it is calculated by adding twice the horizontal run of the side slopes to the bottom width.',

    'R': 'Hydraulic ratio (R)\n\nIs the ratio of the cross-sectional area of the flow to the wetted perimeter. It is calculated as R=A/P, where A is the flow area and P is the wetted perimeter. This value indicates the efficiency of a channel in transporting water, with a higher hydraulic radius leading to increased flow velocity and capacity.',

    'Yn': 'Normal depth (Yn)\n\nIs the constant depth of water in an open channel where the flow is steady and uniform, meaning the water surface slope, channel bottom slope, and energy grade line slope are all equal. This occurs when the forces of gravity and friction are balanced, and the flow velocity is not accelerating or decelerating. It is a crucial concept for engineers designing drainage systems and other hydraulic structures, and it is typically calculated using Mannings equation.',

    'Yc': 'Critical depth (Yc)\n\nIs the flow depth in an open channel where specific energy is at a minimum for a given discharge. It is the transition point between subcritical flow (where the depth is greater than critical depth) and supercritical flow (where the depth is less than critical depth). Understanding critical depth is vital for designing channels and predicting how water will flow through hydraulic structures.',

    'V': 'Velocity (V)\n\nIs the speed of the fluid, which varies across the cross-section, being zero at the boundaries and increasing towards the free surface. It is calculated using formulas like the Mannings equation, which considers the channels hydraulic radius, slope, and roughness. The mean velocity is often used for design and can be estimated by averaging velocities at specific depths, such as 0.2 and 0.8 of the total depth, or by taking the velocity at 0.6 of the depth from the surface.',

    'Fr': 'Froude number (Fr)\n\nIn open channels is a dimensionless value that compares inertial forces to gravitational forces to determine the flow regime: subcritical Fr<1, critical F=1, or supercritical Fr>1. It is calculated as the ratio of the flow velocity to the wave velocity, with velocity being the flow speed V and wave velocity being √gD, where g is the acceleration due to gravity and D is the hydraulic depth A/T.',

    'A': 'Geometric area (A)\n\nIn a channel is the cross-sectional area of the flow, which represents the space occupied by the fluid as it moves through the channel. It is a crucial parameter for understanding how much water can pass through a channel at any given time.',

    'τօ': 'Shear stress (τօ), tau\n\nIn channels is the force exerted by a fluid flowing over a surface, acting parallel to that surface and causing a drag or friction force. It is calculated as the force per unit area and is a measure of the fluids resistance to flow, which can erode the channel bed or be a factor in sediment transport. The stress is also present between layers of the fluid itself and is influenced by factors like fluid viscosity, flow depth, channel slope, and turbulence.',

    'F': 'Hydraulic force (F)\n\nIn open channels, hydraulic force is the force exerted by the flowing water, which is driven primarily by gravity and influenced by pressure and shear stress. This force is essential for understanding and designing channels, as it can be used to measure discharge, control water levels, and dissipate energy through structures like hydraulic jumps.',

    'Sc': 'Critical slope (Sc)\n\nIn open channels is the specific bed slope at which the normal depth of flow Yn is equal to the critical depth Yc. At this slope, the flow is uniform and critical, with a Froude number of 1. It serves as a boundary to classify a channels slope as "mild" So<Sc, where normal depth is greater than critical depth Yn>Yc, or "steep" So>Sc, where normal depth is less than critical depth Yn<Yc.'
}
