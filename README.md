# CABLE-DRIVEN SERIES ELASTIC ACTUATOR FOR UPPER-LIMB REHABILITATIVE EXOSKELETON
You can see the demo video [here](https://www.youtube.com/watch?v=A_MqyhAG-6s)!

![singleroller](/images/triplefollerjoint.jpg)

Individuals effected by a stroke will often develop symptomatic neuromotor control deficits. Depending on the degree of the stroke and the localization in the brain, these deficits can be categorized into impairments of specific neuromotor pathways. Reticulospinal (RS) hyperexcitability is currently believed to be the most likely candidate responsible for a common form of post-stroke spasticity, which can result in weakness and spasmodic motion control in the effected individual. In many cases, motor recovery and reduced spasticity can be achieved through rehabilitative therapy; historically this often takes form via hands-on manipulation and assistance by occupational therapists, repetitive goal-oriented intensive therapy, and medicinal treatments. These therapies, while effective, are often limited in scope by the availability and individual training of medical personnel, the cost of travel and therapy, and difficulties in customizing therapeutic approaches for individual patients.

Ideally, the design of a modular device to facilitate certain aspects common to motor recovery therapies would allow for a greater degree of accessibility to effected populations and more effective and regular training intervals (regularity of training periods is a key factor of successful neurorehabilitation). To this end, we propose a lightweight gravity-balancing exoskeleton with cable-driven elastic actuation, engineered to provide feedback which encourages synergistic patterns of movement that post-stroke spasticity commonly prohibits.

# DESCRIBE EXO; DESCRIBE AND SHOW SEA PROTOTYPES/COMPONENTS
A gravity-balancing machine (in this case, a gravity-balancing orthosis (GBO)) is defined as a mechanical system which can offload the force due to gravity (in part or whole) experienced by a load onto a separate component of the mechanism. In this device, the gravity-balancing subsystem is confined to the upper limbs, allowing for the downward force due to gravity to be offloaded via a series of counterweights (with specific degrees of freedom) onto the user's back. The device is engineered to assist with upper limb neuromotor rehabilitation, and--as such--is concentrated on the minimization of external forces on the upper limbs. Depending on the stage of recovery that a survivor of stroke is currently working through (and concordantly the severity of neuromuscular weakness), the reduction of gravitational forces can greatly reduce the effort/focus required by the user that is dedicated solely to counteracting gravity. Instead, the user's focus can be directed towards the repetitive goal-oriented therapy motions in a manner somewhat analogous to water immersive and equine therapy used for lower-limb rehabilitative approaches. Due to the positioning of the counterweights, the GBO can perform well for a wide range of arm configurations--and can certainly perform well within the range required for the user to engage in therapeutic tasks.

# EXO OVERVIEW
The GBO upper-limb exoskeleton is comprised of a consumer backpack frame (with waist strap for further weight distribution along the user's trunk), and a series of carbon fiber tubes (lightweight, high tensile strength).

![singleroller](/images/exo2.jpeg)

# SEA OVERVIEW
A series elastic actuator (SEA) is a form of actuator that inherently supports an elastic component between the actual actuator and the actuator's load. This boasts a number of helpful applications, especially in the domain of rehabilitative/assistive robotics. The elastic component allows for an otherwise rigid robotic system to interact with the environment around it (or a human element) in a non-rigid manner, providing 'give' to the joints. A wonderful caveatthat lends itself well to the realm of rehabilitative robotics is the ability to directly calculate the torque on a joint by tracking the difference in displacement of the motor and load on either side of the elastic component.

# SEA COMPONENTS

## BOM:

* Raspberry Pi 4 Model B (2GB RAM) x1 ($45.00)
* Torsion Spring (360 deg, Left-Hand Wound, 0.174''OD) x2 ($5.59 for 6)
* Ball Bearing (Open, Trade Number R2, for 1/8'' Shaft Diameter) x2 ($6.21 each)
* Carbon Fiber Tube (1" OD, 15/16'' ID, 3ft) x1 (95.99 each)
* Dyneema Throw Line (MBS: 650lb) x1 ($26.00/54.8m)
* Dycem Non-Slip Material Roll x1 ($18.45/1m)
* Pololu 250:1 Micro Metal Gearmotor (HP 6V with Extended Motor Shaft) x2 ($16.95 each)
* Pololu Magnetic Encoder Pair Kit for Micro Metal Gearmotors (12 CPR, 2.7-18V) x2 ($8.95 each)
* AEAT-6012 Magnetic Encoder x2 ($28.79 each)
* PLA and Ultimaker 2/3 (or equivalent)

## Assembly



### Motors and motor encoders

The requirements

### Spool and spool encoders

### Spring choice



# SEA PROTOTYPES AND FINAL

<p align="center"> <script src="https://embed.github.com/view/3d/mossti/exo_rendering/master/stl_files/Assembly.stl"></script> </p>

# CODE

## ROS information and supporting packages:

This implementation uses:
* ROS Melodic
* catkin, geometry_msgs, roscpp, rospy, std_msgs
* teleop_tools package (for keyboard input tensioning) [get it here](https://github.com/ros-teleop/teleop_tools)!

To use this code, copy the 'exo_joint' and the 'teleop_tools' packages into your ROS workspace's src folder and run 'catkin_make'.

## Pre-tensioning

## Prevent angular deflection:

The goal with this code (test = '1')

## Follow angular deflection:

The goal with this code (test = '2')

## Cable actuation:

![singleroller](/images/singleroller.jpg)

![doubleroller](/images/tripleroller.jpg)

# FUTURE CONSIDERATIONS

One of the largest issues faced was the pre-tensioning of the cable drive. The cable used (Dyneema 650lb throw-line)

# CITATIONS

* [1] Agarwal, Priyanshu & Deshpande, Ashish. (2017). Series Elastic Actuators (SEAs) for Small-scale Robotic Applications. Journal of Mechanisms and Robotics. 9. 10.1115/1.4035987.  
* [2] Agarwal, P., Yun, Y., Fox, J., Madden, K., & Deshpande, A. D. (2017). Design, control, and testing of a thumb exoskeleton with series elastic actuation. The International Journal of Robotics Research, 36(3), 355–375. https://doi.org/10.1177/0278364917694428
* [3] F. Huang, R. B. Gillespie and A. Kuo, "Haptic feedback and human performance in a dynamic task," Proceedings 10th Symposium on Haptic Interfaces for Virtual Environment and Teleoperator Systems. HAPTICS 2002, Orlando, FL, USA, 2002, pp. 24-31.
doi: 10.1109/HAPTIC.2002.998937
* [4] Felix C. Huang, R. Brent Gillespie & Arthur D. Kuo (2007) Visual and Haptic Feedback Contribute to Tuning and Online Control During Object Manipulation, Journal of Motor Behavior, 39:3, 179-193, DOI: 10.3200/JMBR.39.3.179-193
* [5] Li S. (2017). Spasticity, Motor Recovery, and Neural Plasticity after Stroke. Frontiers in neurology, 8, 120. doi:10.3389/fneur.2017.00120
* [6] Xu, Y., Terekhov, A. V., Latash, M. L., & Zatsiorsky, V. M. (2012). Forces and moments generated by the human arm: variability and control. Experimental brain research, 223(2), 159–175. doi:10.1007/s00221-012-3235-0

# ACKNOWLEDGEMENTS

Special thanks to the wonderful folks in the MSR 2018-2019 cohort, Dr. Elwin, Dr. Schultz, Bill Hunt, and Dr. Huang.
