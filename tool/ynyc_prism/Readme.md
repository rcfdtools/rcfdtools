# Yn & Yc - Normal and critical depth in prismatic channels

An open channel flow is the movement of a liquid, like water, in a conduit that has a free surface exposed to the atmosphere. Unlike a pipe that is completely full, open channel flow is driven by gravity, and the top surface of the liquid is not under pressure. Common examples include rivers, streams, canals, and storm drains. [:pineapple:**RUN** Tool.](https://rcfdtools.github.io/rcfdtools/tool/ynyc_prism/) 

<div align="center"><img alt="R.HydroTools" src="assets/prism.svg" width="500px"></div>


## 1. General concepts

### Manning Equation

The Manning equation is an empirical formula used in fluid dynamics to calculate the flow rate (Q) and velocity (v) of water in an open channel. It is based on the channel's cross-sectional area (A), hydraulic radius (R), slope (S), and Manning's roughness coefficient (n). The equation can be written for flow rate as:

<div align="center"><img alt="R.HydroTools" src="assets/manning_equation.svg" width="180px"></div>

where <i>c</i> = 1 for the international system units or <i>c</i> = 1.49 for the imperial system.


### Normal depth (Yn)

Is the constant depth of water in an open channel where the flow is steady and uniform, meaning the water surface slope, channel bottom slope, and energy grade line slope are all equal. This occurs when the forces of gravity and friction are balanced, and the flow velocity is not accelerating or decelerating. It is a crucial concept for engineers designing drainage systems and other hydraulic structures, and it is typically calculated using Manning's equation.


### Critical depth (Yc)

Is the flow depth in an open channel where specific energy is at a minimum for a given discharge. It is the transition point between subcritical flow (where the depth is greater than critical depth) and supercritical flow (where the depth is less than critical depth). Understanding critical depth is vital for designing channels and predicting how water will flow through hydraulic structures.


### Geometric area (A)

In a channel is the cross-sectional area of the flow, which represents the space occupied by the fluid as it moves through the channel. It is a crucial parameter for understanding how much water can pass through a channel at any given time.


### Wet perimeter (P)

Is the length of the channel boundary that is in contact with the fluid flowing through it. This includes the bottom and sides of the channel or pipe, but not the free surface of the water. It is a key factor in fluid mechanics for calculating a channel hydraulic radius and understanding friction losses in open channel and pipe flow.


### Top width (T)

Is the horizontal width at the waters surface. It is a critical measurement used in hydraulics to calculate other channel properties like the flow area and hydraulic depth. For a simple rectangular channel, the top width is the same as the bottom width, but for a trapezoidal channel, it is calculated by adding twice the horizontal run of the side slopes to the bottom width.


### Hydraulic ratio (R)

Is the ratio of the cross-sectional area of the flow to the wetted perimeter. It is calculated as R=A/P, where A is the flow area and P is the wetted perimeter. This value indicates the efficiency of a channel in transporting water, with a higher hydraulic radius leading to increased flow velocity and capacity.

<div align="center"><img alt="R.HydroTools" src="assets/hydraulic_ratio.svg" width="60px"></div>


### Hydraulic depth (D)

Is the ratio of the cross-sectional area of flow A to the top width T of the water surface, expressed as D=A/T. It is a key parameter in open channel hydraulics, particularly useful for calculating things like the Froude number and energy relationships, while hydraulic radius is used for frictional losses. In a rectangular channel, the hydraulic depth is simply equal to the vertical depth of the flow.',

<div align="center"><img alt="R.HydroTools" src="assets/hydraulic_depth.svg" width="60px"></div>


### Velocity (v)

Is the speed of the fluid, which varies across the cross-section, being zero at the boundaries and increasing towards the free surface. It is calculated using formulas like the Manning's equation, which considers the channels hydraulic radius, slope, and roughness. The mean velocity is often used for design and can be estimated by averaging velocities at specific depths, such as 0.2 and 0.8 of the total depth, or by taking the velocity at 0.6 of the depth from the surface.

<div align="center"><img alt="R.HydroTools" src="assets/velocity.svg" width="60px"></div>


### Froude Number

The Froude number is a dimensionless quantity that compares the inertial force of a fluid to the gravitational force acting on it. It is calculated as the ratio of the flow velocity to the velocity of a gravity wave and is used to describe different flow regimes in open channels, such as rivers and canals. The number is categorized based on its value: supercritical (Fr > 1, fast and deep flow), critical (Fr = 1, where flow velocity equals wave velocity), and subcritical (Fr < 1, slow and shallow flow).

<div align="center"><img alt="R.HydroTools" src="assets/froude_number.svg" width="100px"></div>

where <i>v</i> is the flow velocity, <i>g</i> is the acceleration due to gravity, and <i>D</i> is the hydraulic depth.


### Shear stress (τօ), tau

In channels is the force exerted by a fluid flowing over a surface, acting parallel to that surface and causing a drag or friction force. It is calculated as the force per unit area and is a measure of the fluids resistance to flow, which can erode the channel bed or be a factor in sediment transport. The stress is also present between layers of the fluid itself and is influenced by factors like fluid viscosity, flow depth, channel slope, and turbulence.

<div align="center"><img alt="R.HydroTools" src="assets/shear_stress.svg" width="180px"></div>


### Hydraulic force (F)

In open channels, hydraulic force is the force exerted by the flowing water, which is driven primarily by gravity and influenced by pressure and shear stress. This force is essential for understanding and designing channels, as it can be used to measure discharge, control water levels, and dissipate energy through structures like hydraulic jumps.


### Critical slope (Sc)

In open channels is the specific bed slope at which the normal depth of flow Yn is equal to the critical depth Yc. At this slope, the flow is uniform and critical, with a Froude number of 1. It serves as a boundary to classify a channels slope as "mild" So<Sc, where normal depth is greater than critical depth Yn>Yc, or "steep" So>Sc, where normal depth is less than critical depth Yn<Yc.

<div align="center"><img alt="R.HydroTools" src="assets/critical_slope.svg" width="190px"></div>


### Hydraulic force

In open channel flow (like rivers, canals), hydraulic force refers to the forces acting on the water and channel boundaries, primarily driven by gravity (weight component along slope) and balanced by friction/shear stress, with forces like pressure and momentum also influencing flow, especially at transitions where "specific force" helps analyze energy changes and obstacles like weirs or hydraulic jumps. It's about the interplay of pressure, gravity, inertia, and friction that shapes how water moves with a free surface. 

<div align="center"><img alt="R.HydroTools" src="assets/hydraulic_force.svg" width="200px"></div>


### Freeboard (Fb)

Freeboard in water channels is the vertical distance between the normal water surface and the top of the channel bank, acting as a crucial safety margin to prevent overtopping from surges, waves, or unexpected flow increases, ensuring water stays within the channel and doesn't flood surrounding areas or cause structural damage, often a percentage of channel depth or a fixed height, varying by application like irrigation or flood control. It's a design element to manage uncertainties, from wind action to operational errors, keeping hydraulic structures like flumes and weirs functioning correctly. 


## 2. Sample exercises

Samples exercises with different prismatic geometries. 

> Channels with negative side slopes may require deep knowledge about the numerical method used and the approach of the correct geometric solution. 

<div align="center">

| Exercise  and Parameters                                                                                                                                                                                                                                            | Cross-section                                                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| **YnYcE0001** - Trapezoidal ditch channel with negative side slopes and subcritical regime.<br><br>Parameters: unit_sys = 'SI', q = 10, g = 9.806, b = 20, z1 = -4, z2 = -4, so = 0.0008969, n = 0.035, alpha = 1, rho = 1000, y1 = 0.0001, y2 = 2, steps = 64.     | <img alt="R.HydroTools" src="assets/exercise/YnYcE0001.svg" width="600px"> |
| **YnYcE0002** - Trapezoidal ditch channel with negative side slopes and supercritical regime.<br><br>Parameters: unit_sys = 'SI', q = 10, g = 9.806, b = 20, z1 = -4, z2 = -4, so = 0.1, n = 0.035, alpha = 1, rho = 1000, y1 = 0.0001, y2 = 2, steps = 64.         | <img alt="R.HydroTools" src="assets/exercise/YnYcE0002.svg" width="600px"> |
| **YnYcE0003** - Trapezoidal channel in subcritical regime.<br><br>Parameters: unit_sys = 'SI', q = 10, g = 9.806, b = 5, z1 = 2, z2 = 2, so = 0.0008969, n = 0.035, alpha = 1, rho = 1000, y1 = 0.0001, y2 = 5, steps = 64.                                         | <img alt="R.HydroTools" src="assets/exercise/YnYcE0003.svg" width="600px"> |
| **YnYcE0004** - Trapezoidal channel in supercritical regime.<br><br>Parameters: unit_sys = 'SI', q = 10, g = 9.806, b = 5, z1 = 2, z2 = 2, so = 0.1, n = 0.035, alpha = 1, rho = 1000, y1 = 0.0001, y2 = 5, steps = 64.                                             | <img alt="R.HydroTools" src="assets/exercise/YnYcE0004.svg" width="600px"> |
| **YnYcE0005** - Rectangular channel in subcritical regime.<br><br>Parameters: unit_sys = 'SI', q = 10, g = 9.806, b = 5, z1 = 0, z2 = 0, so = 0.0008969, n = 0.035, alpha = 1, rho = 1000, y1 = 0.0001, y2 = 10, steps = 64.                                        | <img alt="R.HydroTools" src="assets/exercise/YnYcE0005.svg" width="600px"> |
| **YnYcE0006** - Rectangular channel in supercritical regime.<br><br>Parameters: unit_sys = 'SI', q = 10, g = 9.806, b = 5, z1 = 0, z2 = 0, so = 0.1, n = 0.035, alpha = 1, rho = 1000, y1 = 0.0001, y2 = 10, steps = 64.                                            | <img alt="R.HydroTools" src="assets/exercise/YnYcE0006.svg" width="600px"> |
| **YnYcE0007** - Triangular channel in subcritical regime.<br><br>Parameters: unit_sys = 'SI', q = 10, g = 9.806, b = 0, z1 = 3, z2 = 3, so = 0.0008969, n = 0.035, alpha = 1, rho = 1000, y1 = 0.0001, y2 = 10, steps = 64.                                         | <img alt="R.HydroTools" src="assets/exercise/YnYcE0007.svg" width="600px"> |
| **YnYcE0008** - Triangular channel in supercritical regime.<br><br>Parameters: unit_sys = 'SI', q = 10, g = 9.806, b = 0, z1 = 3, z2 = 3, so = 0.1, n = 0.035, alpha = 1, rho = 1000, y1 = 0.0001, y2 = 10, steps = 64.                                             | <img alt="R.HydroTools" src="assets/exercise/YnYcE0008.svg" width="600px"> |
| **YnYcE0009** - Triangular ditch channel in subcritical regime.<br><br>Parameters: unit_sys = 'SI', q = 10, g = 9.806, b = 0, z1 = 1, z2 = 30, so = 0.0008969, n = 0.035, alpha = 1, rho = 1000, y1 = 0.0001, y2 = 10, steps = 64.                                  | <img alt="R.HydroTools" src="assets/exercise/YnYcE0009.svg" width="600px"> |
| **YnYcE0010** - Triangular ditch channel in supercritical regime.<br><br>Parameters: unit_sys = 'SI', q = 10, g = 9.806, b = 0, z1 = 1, z2 = 30, so = 0.1, n = 0.035, alpha = 1, rho = 1000, y1 = 0.0001, y2 = 10, steps = 64.                                      | <img alt="R.HydroTools" src="assets/exercise/YnYcE0010.svg" width="600px"> |
| **YnYcE0011** - Trapezoidal ditch channel in subcritical regime.<br><br>Parameters: unit_sys = 'SI', q = 10, g = 9.806, b = 5, z1 = 0, z2 = 30, so = 0.0008969, n = 0.035, alpha = 1, rho = 1000, y1 = 0.0001, y2 = 10, steps = 64.                                 | <img alt="R.HydroTools" src="assets/exercise/YnYcE0011.svg" width="600px"> |
| **YnYcE0012** - Trapezoidal ditch channel in supercritical regime.<br><br>Parameters: unit_sys = 'SI', q = 10, g = 9.806, b = 5, z1 = 0, z2 = 30, so = 0.1, n = 0.035, alpha = 1, rho = 1000, y1 = 0.0001, y2 = 10, steps = 64.                                     | <img alt="R.HydroTools" src="assets/exercise/YnYcE0012.svg" width="600px"> |
| **YnYcE0013** - Trapezoidal ditch channel with negative left side slope in subcritical regime.<br><br>Parameters: unit_sys = 'SI', q = 10, g = 9.806, b = 5, z1 = -5, z2 = 30, so = 0.0008969, n = 0.035, alpha = 1, rho = 1000, y1 = 0.0001, y2 = 10, steps = 64.  | <img alt="R.HydroTools" src="assets/exercise/YnYcE0013.svg" width="600px"> |
| **YnYcE0014** - Trapezoidal ditch channel with negative left side slope in subcritical regime.<br><br>Parameters: unit_sys = 'SI', q = 10, g = 9.806, b = 5, z1 = -5, z2 = 30, so = 0.0008969, n = 0.035, alpha = 1, rho = 1000, y1 = 0.0001, y2 = 10, steps = 64. | <img alt="R.HydroTools" src="assets/exercise/YnYcE0014.svg" width="600px"> |

</div>


## Libraries used

* [Matplotlib](https://matplotlib.org/)
* [Pyscript](https://pyscript.net/)


## References

* https://www.hec.usace.army.mil/confluence/rasdocs/rasum/6.3/entering-and-editing-geometric-data/importing-geometric-data
* https://uomustansiriyah.edu.iq/media/lectures/5/5_2019_04_22!08_20_51_PM.pdf
* https://www.hec.usace.army.mil/confluence/hmsdocs/hmstrm/transform/unit-hydrograph-basic-concepts
* [bennyistanto / Unit Hydrographs](https://gist.github.com/bennyistanto/62a5427c2780c50d2b3dd69649e0a58f)


## Developers

* https://github.com/rcfdtools
* https://github.com/frankv13
* https://github.com/juanrodace
