<div align="center"><a href="https://github.com/rcfdtools" target="_blank"><img src="https://github.com/rcfdtools/rcfdtools/blob/main/graph/rcfdtools_banner.png" alt="R.LTWB" width="100%" border="0" /></a></div>

# COURSE: _“Water Resources Engineering and management - WREM”_
Keywords: `hydrology` `hydraulics` `geographic-information-systems` `hec-ras` `hec-hms` `qgis` `river-design` `river-modeling` `river-profile` `river-slope` `manning-roughness` 

Water Resources Engineering and Management is a specialized field that blends civil engineering, hydrology, hydraulics and environmental science to sustainably supply, distribute, and protect the world's freshwater resources. It focuses on balancing human demands (such as drinking water, agriculture, and industry) with ecological preservation while mitigating water-related hazards like floods and droughts. The combination of hydrology and hydraulics allow engineers to calculate how much water is coming and design systems to safely manage, transport, or utilize it.


## Course goals

* To provide participants with detailed knowledge of the use of GIS applied to Civil Engineering, through the use of publicly available software tools.
* To develop skills in the graphic representation of geographic elements.
* To easily and accurately search, select, and filter spatial entities and attributes.
* To acquire the necessary knowledge for information analysis through simple and complex searches, proximity, overlay, and data merging.
* To download, process, and analyze terrain models, raster images, and satellite information from remote sensors.
* To create computational hydrological and hydraulic models.


## Participants

The content presented in this course is aimed at students and professionals from different disciplines who need to learn and/or strengthen their knowledge in the use of software tools, such as:

* Engineers
* Specialists
* Territorial managers.

> A basic level of English is required because we will be using the user interfaces in this language.
> 
> As a prerequisite, students require basic knowledge of computer programming.


## Academic Methodology

* Through practical workshops, participants will be introduced to different concepts and applications of Geographic Information Systems in the development of applied engineering studies.
* At the beginning of each class, the instructor will give a general presentation and demonstration of the concepts and computer tools to be used, and then the students will complete the content of each workshop, activity, or exercise.
* Before each class, it is recommended that participants read the class guides to better understand the explanations received in class.


## Requirements and folder structure

The following tools and directory structure are required for the development of the course and research activities:

<div align="center">

| Requirement                                                                                   | Description                                                                                |
|:----------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------|
| [:toolbox:Tool](https://www.office.com/)                                                      | Microsoft 365 (Word, Excel, OneDrive, Teams).                                              |
| [:toolbox:Tool](https://notepad-plus-plus.org/)                                               | Notepad++ (text editor).                                                                   |
| [:toolbox:Tool](https://qgis.org/)                                                            | QGIS 3.44.10, 4.0.2 or newer.                                                              |
| [:toolbox:Tool](https://www.7-zip.org/)                                                       | 7-Zip File Manager (file compressor).                                                    |
| [:toolbox:Tool](https://www.hec.usace.army.mil/software/hec-hms/)                             | HEC-HMS 4.13 or newer.                                                                     |
| [:toolbox:Tool](https://www.hec.usace.army.mil/software/hec-dssvue/)                          | HEC-DSSVue 3.2.3 (functional version for massive hyetograph load).                         |
| [:toolbox:Tool](https://www.hec.usace.army.mil/software/hec-ras/)                             | HEC-RAS 7.0 or newer.                                                                      |
| [:construction_worker:GitHub user account](https://github.com/)                               | Course resourcess access and upgrading notificacions.                                      |
| [:construction_worker:USGS user account](https://ers.cr.usgs.gov/register/contact)            | USGS - United States Geological Survey account (satellital images).                        |
| [:construction_worker:Copernicus user account](https://dataspace.copernicus.eu/)              | European Union's Earth observation program account (ERA5 data).                            |
| [:construction_worker:OpenTopography user account](https://portal.opentopography.org/newUser) | OpenTopography account (high-resolution topographic data as LiDAR, radar, photogrammetry). |
| [:package:Folder structure](file/Readme.md)                                                   | Required folder structure.                                                                 |
| [:memo:Technical report layout](file/report/)                                                 | Report layout for students technical reports.                                              |

</div>


### Engineering regional settings

* **Operational system**: in _Microsoft Windows / Control Panel / Region / Formats / Additional settings..._, set _Decimal symbol_ as point ` . `, _Digit grouping symbol_ as comma ` , ` and _List separator_ as coma ` , `.
* **Microsoft Excel**: from the menu _File / Options / Advanced / Editing Options_, uncheck the box _Use system separators_ and set point ` . ` as _Decimal separator_ and comma ` , ` as _Thousands separator_. 
* **QGIS**, from the menu _Settings / General / Override System Locale_, set _User interface translation_ as _American English_ and _Locale (number, date and currency formats)_ as _English United States (en_US)_.


## :large_blue_circle:Module 1: Geographic information systems - GIS

A Geographic Information System (GIS) is a digital framework used to capture, store, analyze, and visualize spatial data. In hydrology and hydraulics, GIS acts as the spatial engine of water management. It maps terrain and landscape characteristics to calculate how water moves across a landscape.

| Activitie                                                           | Scope / Workshop reference                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Duration (10 hr) |
|:--------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------:|
| Case study                                                          | A case study in water resources engineering is an in-depth investigation of a real-world water project, problem, or disaster. It analyzes the technical, environmental, and socioeconomic factors behind an infrastructure challenge, demonstrating how engineers apply fluid mechanics and hydrology to design effective solutions.<br/><br/>https://github.com/rcfdtools/R.IAMB/blob/main/activity/CaseStudy/Readme.md                                                                                                                      |        1         |
| Satellite imagery Landsat & Sentinel-2                              | Satellite imagery refers to visual and geospatial data of the Earth's surface captured by satellites orbiting the planet. It is not just simple photography; it is a sophisticated collection of data across the electromagnetic spectrum used to track weather, assess environmental changes, and map terrain. Satellites are equipped with specialized sensors (like cameras and radars) that measure energy reflected or emitted from the Earth.<br/><br/>https://github.com/rcfdtools/R.IAMB/blob/main/activity/RemoteSensingDL/Readme.md |       1.5        |
| Digital elevation models - DEM: COP30, Slope, Thermic level, Lidar  | A DEM is a digital 3D representation of the Earth’s surface, typically formatted as a grid of squares (pixels) where each pixel holds an elevation value. LiDAR is a remote sensing method that fires rapid pulses of laser light from an airplane, drone, or tripod down to the ground.<br/><br/>https://github.com/rcfdtools/R.IAMB/blob/main/activity/RemoteSensingDL/Readme.md<br/>https://github.com/rcfdtools/R.HydroBogota/blob/main/file/data/Readme.md                                                                               |       1.5        |
| Geologic map                                                        | A geologic map is a specialized map used to visualize the types of rocks, sediments, and structural features present at or near the Earth's surface. It acts as a foundational tool for understanding the 3D structure of the ground, geologic history, and potential natural resources or hazards.<br/><br/>https://github.com/rcfdtools/R.IAMB/blob/main/activity/Geology/Readme.md                                                                                                                                                         |       1.5        |
| Land soil and Land use                                              | A land soil study is a detailed analysis of a plot of land's physical, chemical, and biological properties. It determines the soil's load-bearing capacity for construction or its nutrient composition for agriculture, ensuring safe development and optimal land management.<br/><br/>https://github.com/rcfdtools/R.IAMB/blob/main/activity/LandSoil/Readme.md<br/>https://github.com/rcfdtools/R.HydroBogota/blob/main/file/data/Readme.md                                                                                               |       1.5        |
| Drainage network                                                    | A drainage network is an interconnected system of channels, streams, and rivers that collects precipitation and surface runoff from a specific land area, funneling it downhill into a single outlet.<br/>https://github.com/rcfdtools/R.IAMB/blob/main/activity/BasinLimit/Readme.md                                                                                                                                                                                                                                                         |       1.5        |
| Hydrometeorological stations                                        | A hydrometeorological station is a specialized facility equipped with instruments to measure and record both atmospheric weather conditions and water-related (hydrological) parameters. They bridge the gap between meteorology and hydrology by tracking how weather events impact water resources, such as river levels, rainfall, and soil moisture.<br/><br/>https://github.com/rcfdtools/R.IAMB/blob/main/activity/CNEStation/Readme.md                                                                                                 |       1.5        |


## :large_blue_circle:Module 2: Hydrology

Hydrology focuses on the Earth's water cycle. It deals with the occurrence, distribution, and movement of water across the globe, including rainfall, evaporation, and groundwater flow. 

| Activitie                                                                            | Scope / Workshop reference                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Duration (10 hr) |
|:-------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------:|
| Maximum probable precipitation in 24 hours: PDF selection and Tr interpolation maps  | Maximum Precipitation in 24 hours (PMax24h) is the greatest amount of rainfall for a specific duration that is meteorologically possible for a given location, acting as a "worst-case" scenario for extreme storms, crucial for designing safety-critical infrastructure like bridges, river deviations, dams, spillways, and nuclear plants to prevent catastrophic failure.<br/><br/>https://github.com/rcfdtools/R.HydroTools/blob/main/tool/PMP                                                                                                                                                                                                                                                           |       1.5        |
| Curve Number map - CN                                                                | A Curve Number (CN) map is a spatial/geographic representation of an area's stormwater runoff potential. Developed by the USDA Natural Resources Conservation Service (NRCS), it predicts how much rainfall will become direct runoff versus how much will infiltrate the ground.<br/><br/>https://www.youtube.com/watch?v=eMlo-uBMlHs&t=2s                                                                                                                                                                                                                                                                                                                                                                    |        1         |
| Subbasin restitution and morphometric parameters                                     | A subbasin is a smaller, distinct geographic watershed that drains into a larger river system. Subbasin restitution refers to the geomorphological and ecological restoration of this area, while morphometric parameters are the mathematical measurements of its size, shape, and physical landforms used to model its hydrological and erosion behaviors. Understanding these concepts helps scientists and environmental planners assess water resources, control erosion, and map flood risks.<br/><br/>https://github.com/rcfdtools/R.TSIG/blob/main/activity/TSIG_Taller9.pdf<br/>https://github.com/rcfdtools/R.IAMB/blob/main/activity/BasinLimit/Readme.md<br/>https://forms.office.com/r/5xS3WwmKJs |       1.5        |
| Maximum precipitation simulation                                                     | A hydrological maximum precipitation simulation models extreme, worst-case rainfall events to predict the resulting water runoff and prevent downstream flooding. These concepts are critical for civil engineers, hydrologists, and environmental planners managing water security and climate adaptation.<br/><br/>https://github.com/rcfdtools/R.TSIG/blob/main/activity/TSIG_Taller9.pdf                                                                                                                                                                                                                                                                                                                   |       1.5        |
| Long-term hydrological balance                                                       | The long-term hydrological balance is the mathematical equilibrium between water inputs (e.g., precipitation) and outputs (e.g., evapotranspiration, runoff) within a specific geographic area over a multi-year period. Averaging these fluctuations over time means the net change in water storage essentially becomes zero, helping assess regional water availability. The fundamental equation governing this equilibrium over a long period (where the change in storage (_ΔS = 0_) is: _Precipitation (P) = Evapotranspiration (E) + Runoff (R)_.<br/><br/>https://github.com/rcfdtools/R.LTWB/blob/main/README.md                                                                                     |       1.5        |
| Elevation area & Elevation volume curves in reservoirs                               | Elevation-Area and Elevation-Volume curves are graphical tools used by engineers to define the physical geometry of a reservoir. They represent how much water surface area and total water capacity correspond to any given water level elevation, which is critical for planning, flood control, and power generation.<br/><br/>https://github.com/rcfdtools/R.SIGE/blob/main/activity/Reservoir/Readme.md                                                                                                                                                                                                                                                                                                   |       1.5        |
| ERA5-Land analysis                                                                   | ERA5-Land is a high-resolution global climate reanalysis dataset that provides hourly estimates of the water and energy cycles over land. Produced by the European Centre for Medium-Range Weather Forecasts (ECMWF), it offers data from 1950 to the present, featuring an enhanced spatial resolution of about 9 km.<br/><br/>https://github.com/rcfdtools/R.SIGE/blob/main/activity/RemoteSensingERA5/Readme.md<br/>https://github.com/rcfdtools/R.TSIG/blob/main/activity/ERA5/Readme.md                                                                                                                                                                                                                   |       1.5        |


## :large_blue_circle:Module 3: Hydraulics

Hydraulics focuses on the mechanical properties and physical flow of water. It applies fluid mechanics to engineer practical systems like pipes, pumps, river channels, dams, and stormwater networks. 

| Activitie                                            | Scope / Workshop reference                                                                                                                                                                                                                                                                                                                                                                                                             | Duration (5 hr) |
|:-----------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------:|
| Prismatic channel design and flow simulation 1D / 2D | Prismatic channel design involves engineering artificial waterways (e.g., canals, spillways, or sewers) with a constant cross-sectional shape, size, and bottom slope over their entire length. 1D/2D flow simulation uses computational hydraulics to calculate water flow velocities and depths, either in a single direction (1D) or across an entire spatial plane (2D).<br/><br/>https://rcfdtools.github.io/rcfdtools/tool/ynyc/ |        2        |
| Open channel flow simulation 1D / 2D                 | Open channel flow simulation analyzes the movement of fluids (like water) with a free surface exposed to the air. 1D (One-Dimensional) models calculate flow along a single longitudinal path. 2D (Two-Dimensional) models map flow across an area, tracking depth and velocity vectors in multiple directions.<br/><br/>https://github.com/rcfdtools/R.HCMC/blob/main/README.md                                                       |        3        |


##

_R.WREM is free to use for academic purposes; learn about our license, clauses, conditions of use, and how to reference the content published in this repository, giving a [click here](LICENSE.md)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

 [:infinity: More course and tools](https://github.com/rcfdtools) | [:beginner: Help / Collaborate](https://github.com/rcfdtools/R.TSIG/discussions/1) | [:notebook: References](file/ref/Readme.md) | [:label: Abbreviations and definitions](file/ref/Definitions.md) |
|------------------------------------------------------------------|----------------------------------------------------------------------------------|------------------------------------------------|----------------------------------------------------------------|

<div align="center"><img alt="rcfdtools" src="file/graph/R.WREM.svg" height="46px"></div>
