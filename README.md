# CABLE-DRIVEN SERIES ELASTIC ACTUATOR FOR UPPER-LIMB REHABILITATIVE EXOSKELETON

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

# CODE

## ROS information and supporting packages:

This implementation uses ROS Melodic

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

* [1] Li S. (2017). Spasticity, Motor Recovery, and Neural Plasticity after Stroke. Frontiers in neurology, 8, 120. doi:10.3389/fneur.2017.00120
* [2]
* [3]
* [4]
* [5]
* [6]

# ACKNOWLEDGEMENTS
