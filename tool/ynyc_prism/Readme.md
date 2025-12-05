# Yn & Yc - Normal and critical depth in prismatic channels

An open channel flow is the movement of a liquid, like water, in a conduit that has a free surface exposed to the atmosphere. Unlike a pipe that is completely full, open channel flow is driven by gravity, and the top surface of the liquid is not under pressure. Common examples include rivers, streams, canals, and storm drains. 


## General concepts

### Manning Equation

The Manning equation is an empirical formula used in fluid dynamics to calculate the flow rate (Q) and velocity (v) of water in an open channel. It is based on the channel's cross-sectional area (A), hydraulic radius (R), slope (S), and Manning's roughness coefficient (n). The equation can be written for flow rate as:

<img alt="R.HydroTools" src="assets/manning_equation.svg" width="140px">

where <i>c</i> = 1 for the international system units or <i>c</i> = 1.49 for the imperial system.


### Froude Number

The Froude number is a dimensionless quantity that compares the inertial force of a fluid to the gravitational force acting on it. It is calculated as the ratio of the flow velocity to the velocity of a gravity wave and is used to describe different flow regimes in open channels, such as rivers and canals. The number is categorized based on its value: supercritical (Fr > 1, fast and deep flow), critical (Fr = 1, where flow velocity equals wave velocity), and subcritical (Fr < 1, slow and shallow flow).

<img alt="R.HydroTools" src="assets/froude_number.svg" width="80px">

where <i>v</i> is the flow velocity, <i>g</i> is the acceleration due to gravity, and <i>D</i> is the hydraulic depth.



## Developers

* github.com/rcfdtools
* github.com/frankv13
* github.com/juanrodace


## Libraries

* [Matplotlib](https://matplotlib.org/)
* [Pyscript](https://pyscript.net/)

