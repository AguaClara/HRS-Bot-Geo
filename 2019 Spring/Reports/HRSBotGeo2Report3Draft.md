# High Rate Sedimentation: Bottom Geometry Report 3 Draft
#### Madeleine Lee (ml895)
#### Luis Benitez (leb252)
April 12, 2019

**[Sidney: Hey team! I'm going to be making comments in these square brackets.]**

**[In the future, please don't start a new file for new drafts. It's confusing because I can't look at and resolve previous comments.]**

**[Overall: Good job guys! Please go back and make sure everything is in consistent past tense when referring to current semester or prior semester work. Remember to refer to your figures in the actual body of the text otherwise they are just floating and they really should be used! I would also love it if you could connect your "Results" and "Analysis" sections more. Some of examples of how you can do this: 1) by referring to the wonderful graphs and tables you made in "Results" in your text in "Analysis" or 2) by simply merging them into one section.]**

## Abstract
The purpose of the High Rate Sedimentation: Bottom Geometry team is to develop a new geometry of the bottom of the tube settler to prevent floc buildup since floc buildup increases the maintenance and cleaning time  for the system as the buildup can only be removed manually. Manual removal involves running water through the system and draining it repeatedly until the effluent turbidity reads less than 1 NTU, which is a very time consuming process. These geometries will be developed using rapid prototyping techniques including designing the parts in Onshape and 3D printing. To test these geometries, they will be directly inserted into the bottom of the tube settler. A successful geometry would cause resuspension of flocs without any buildup. Geometries that have been proven to cause buildup are those with regular conical shapes because it allows flocs to lock together in a ring such that the upflow of water cannot break it up.

## Introduction
The Bottom Geometry team was created to improve sedimentation in the AguaClara Cornell lab, which is a crucial part of the water treatment process as it acts as the major removal method for suspended and coagulated minerals, dirt, and particles. The process of sedimentation occurs when large flocs, which are clumps of particles created by the flocculator, are removed through settling -- the process by which particles settle to the bottom of a liquid. During sedimentation, a floc blanket, or a layer of suspended flocs, forms and captures other flocs that are too small to settle.

Figure 1 below depicts a tube settler used in the current apparatus. The water treatment process that occurs in the tube settler is sedimentation. The tube settler uses a similar design to an AguaClara plant. The recirculator in the tube settler, a vertical portion of the tube, is where the floc blanket forms and accumulates. The tilted portion at the top of the tube settler act similar to the plate settlers in the plant by stopping flocs from leaving the tank. The floc weir acts identically to the floc weir in the AguaClara plant by removing excess flocs in the floc blanket to keep it at a constant height.

![Tube Settler](https://raw.githubusercontent.com/AguaClara/high_rate_sedimentation/master/Images/Setup/Sedimentation%20Tank%20A.png)
![Plant design](https://github.com/AguaClara/HRS-Bot-Geo/blob/master/Images/plant%20design.PNG?raw=true)
Figure 1: Comparison of lab and AguaClara plant sedimentation tanks.

The main challenge for Bottom Geometry is finding an optimal bottom geometry for the tube settler to prevent sediment buildup, also known as floc buildup or gelling, at the bottom. Floc buildup occurs when flocs clump together and form a dense, solid layer that cannot be broken up by the upflow of water. Figure 2 below depicts an image of this buildup. The nature of the bottom geometry influences the density of the floc blanket and the buildup as well. For example, a flat bottom surrounding the water inlet would allow flocs to stack on top of each other and create such a layer.

![Floc buildup](https://raw.githubusercontent.com/AguaClara/HRS-Bot-Geo/master/2019%20Spring/images/floc%20buildup.jpg)
Figure 2: Image of floc buildup. Cleaning the tube settler requires disconnecting the inflow tube to remove the water in the tube and flushing water through the system to remove particles until the effluent turbidity reads less than 1 NTU.

Although the sediment buildup does not affect sedimentation efficiency, this buildup should be avoided to decrease maintenance and cleaning time of the tube settler. Although sediment buildup is not an issue in AguaClara’s plants, solving the problem at a lab-scale will provide researchers (of whom wish to learn from lab-scale experiments) with documentation on a geometry and a fabrication method. Thus by reducing the maintenance time, it would allow researchers to proceed with their experiments with more ease.

As a continuing team, Bottom Geometry will be moving forward with testing the inserts designed in previous semesters. One main design that will be tested: a sloped-wall shape that converges to a rectangle, depicted in Figure 3. This semester, with the use of rapid prototyping techniques, the Bottom Geometry team will be able to pass through iterations of designs to find an optimal one that can prevent sediment buildup in the lab apparatus.

![Symmetrical AguaClara Plant Design -- Early Version](https://raw.githubusercontent.com/AguaClara/HRS-Bot-Geo/master/Images/fluoride%20auto%20insert.PNG)
Figure 3: Filter insert with symmetrical, rectangular cross sections and a sloped top portion.

## Literature Review and Previous Work
Previous High Rate Sedimentation teams have determined configurations of bottom geometries that contribute to floc buildup. Initially, the tube settler had a flat bottom where water flows in, but floc buildup grew about half an inch in height every ten minutes. To avoid a flat bottom, the Summer 2018 High Rate Sedimentation team drilled a regular cone shape into an insert that would be placed in the bottom of the tube settler, depicted in Figure 4. However, floc buildup was still observed (see Figure 2), possibly due to the fact that flocs could have locked together in a ring around the drilled hole such that it could not be broken up and resuspended by the upflow of water.

![Conical Insert 1](https://raw.githubusercontent.com/AguaClara/HRS-Bot-Geo/master/Images/ConicalBottom.jpg)
![Conical Insert 1](https://raw.githubusercontent.com/AguaClara/HRS-Bot-Geo/master/Images/conicalbottom2.png)
Figure 4: Conical filter insert created by HRS Summer 2018 that caused floc buildup.

A previous Fluoride team proposed another change in the bottom geometry in which the bottom of the tube was cut at an angle and the bottom was closed except for a small part at the longest part of the tube for the inflow, pictured in Figure 5. The tube was essentially “squished” at the bottom such that the cross sectional areas are more rectangular than circular. This prevents flocs from locking together in a ring and causing buildup at the bottom. The stream of water broke up the buildup and allowed flocs to recirculate in the tube settler.

![Sliced tube bottom geometry](https://raw.githubusercontent.com/AguaClara/HRS-Bot-Geo/master/Images/TriSedTank.jpeg)
Figure 5: Sliced tube bottom geometry by previous Fluoride team. Click [this link](https://www.youtube.com/watch?v=EajLuP6eX9w&feature=youtu.be) for a video of the sedimentation tank.

The Fall 2018 Bottom Geometry team developed new designs for the inserts that avoided centered and circular shapes, pictured in Figure 6. One of the designs features sloped slides that allow flocs to slide down. The sloped sides converge to a rectangular opening, and this rectangular opening converges to another smaller square where water is supposed to flow in. This design may prevent flocs from locking in a ring. The hypothesis is that flocs will not lock in a ring since the upflow of water would break up any rings that would form.

![Symmetrical AguaClara Plant Design -- Early Version](https://raw.githubusercontent.com/AguaClara/HRS-Bot-Geo/master/Images/fluoride%20auto%20insert.PNG)
Figure 6: Filter insert with symmetrical, rectangular cross sections and a sloped top portion. This insert was an early version of the sloped top design. It was later changed to cover the ledge and to fit the coupling that is screwed into the bottom of the tube settler.

## Methods
### Designing the Inserts
Redesigning the inserts require an examination of the existing bottom geometry in the lab apparatus and in the existing AguaClara plant. In the lab apparatus, the coupling that screws into the bottom of the tube settler is pictured below in Figure 7. It has a flat bottom that would allow flocs to settle and stack on top of it. To combat this, a cylindrical insert was designed, pictured in Figure 8. The top half reflects the geometry pictured in Figure 6. The bottom half is a cylinder with a rectangular prism cut out from the middle. The cross section is a square that has the same area as a circular cross section of the water inflow tube. The equal area will maintain the same upflow velocity. After the inserts were designed in Onshape, the designs were sent to the Rapid Prototyping Lab in Upson Hall.

![Coupling](https://raw.githubusercontent.com/AguaClara/HRS-Bot-Geo/master/2019%20Spring/images/coupling.jpg)
Figure 7: The inner geometry of the coupling.

![Stacked Cylinder](https://raw.githubusercontent.com/AguaClara/HRS-Bot-Geo/master/2019%20Spring/images/stackedcyl1c.jpg)
![Stacked Cyl in Coupling Top](https://raw.githubusercontent.com/AguaClara/HRS-Bot-Geo/master/2019%20Spring/images/stackedcyl1b.jpg)
![Stacked Cyl in Coupling Bottom](https://raw.githubusercontent.com/AguaClara/HRS-Bot-Geo/master/2019%20Spring/images/stackedcyl1a.jpg)
Figure 8: A stacked cylinder filter insert.

**[A consistent issue: please refer to all of your figures in the text where you intend for them to explain something or serve some sort of purpose. Otherwise, they're just floating around and someone skimming your paper cannot quickly identify which figures go with which specific pieces of information.]**

### Calculations
#### Coagulant Dosing
Python coagulant dosing calculations were used to determine the required coagulant pump speed for the desired coagulant dosage. The Summer 2018 High Rate Sedimentation team also determined that a coagulant dose of 4.5 mg/L was optimal to ensure that coagulant was not a limiting factor in the system. This dose corresponds to a pump speed of 6.2 RPM. This code can be found in the [Manual](#Manual) section of this report.

#### Flow Rate
The flow rate through the system was calculated in accordance with the desired upflow velocity of 2 mm/s and 3 mm/s, as determined by the Summer 2018 High Rate Sedimentation team. The tube settler has an inner diameter of 1 inch, so the following formula

<div style="text-align:center"><img src ="https://raw.githubusercontent.com/AguaClara/HRS-Bot-Geo/master/Images/dvdt.svg?sanitize=true" /></div>

was used to determine the flow rates. A 2 mm/s upflow velocity corresponds to a flow rate of 60 mL/min, and a 3 mm/s upflow velocity corresponds to a flow rate of 90 mL/min. 

### ProCoDA Methods
PID Control is the state that is used to run experiments. PID Control controls the clay pump speed to keep the influent turbidity stable at 100 NTU, which is the standardized influent turbidity for the AguaClara High Rate Sedimentation teams. The values of P, i, and D were calibrated using [this guide](https://confluence.cornell.edu/display/AGUACLARA/Calibrating+PID+Control).

### Experimental Apparatus
The overall experimental setup consists of clay and coagulant reservoirs, four distinct pumps, a flocculator, a tube settler, a pressure attenuator, and two turbidimeters. The clay stock tank is the clay reservoir and holds a mixture of clay and water. There is also a stirrer that continuously mixes the contents of the stock tank. The PaCl coagulant stock tank contains water and PaCl (the coagulant agent) at a concentration of 5 mg/L. The first pump, the water pump, controls the water flow throughout the system with the flow rate set manually. The second pump, the clay pump, is controlled by ProCoDA with the use of PID Control to dose clay into the system to maintain an influent turbidity of 100 NTU. The third pump, the coagulant pump, is used to control the coagulant dose and is set manually to dose the optimal coagulant concentration determined by the Summer 2018 High Rate Sedimentation team. The final pump, the effluent pump, is used to pump effluent out of the floc weir to prevent the buildup of too many flocs.

The flocculator is tubing wound around a cardboard cylinder. The purpose of the flocculator is to combine clay and coagulant from their respective stock tanks such that the clay particles clump together and form flocs. Sedimentation occurs in the tube settler, where flocs are recirculated through the settler. Optimal performance of the tube settler involves the formation of a floc blanket, or a suspended fluidized bed of flocs that capture other flocs that are too small to settle. The flocs then flow down the floc weir, the extension jutting out from the left side of the tube settler. The pressure attenuator indicates whether there is pressure building up in the system; i.e. if water is rising in the attenuator, pressure is building up somewhere, likely due to a closed valve. Lastly, there are two turbidimeters: one that measures influent turbidity and one that measures effluent turbidity. All these components are labeled in Figure 10 below. **[You may want to separate this into two or more paragraphs. It's very long.]**

![HRS Bottom Geometry Apparatus](https://raw.githubusercontent.com/AguaClara/HRS-Bot-Geo/master/Images/ExperimentalApparatus.PNG)
Figure 10: Bottom Geometry apparatus with labeled components.

### Procedure
#### Cleaning the Apparatus
First, the tube settler was drained of any water and clay. Next, the turbidimeters were cleaned as per the instructions in the [AguaClara Tutorial Wiki Page](https://github.com/AguaClara/aguaclara_tutorial/wiki/Cleaning-a-Turbidimeter). Then water was run through the system at 150 RPM to clean the rest of the system and remove the residual sediment. The flocculator was cleaned by opening the valve between the flocculator and syringe and letting water fill the syringe. When the syringe was filled halfway, the water was forced out, which pushed the residual sediment out of the flocculator. Water continued to run through the system until the influent and effluent turbidimeters read 0 to 1 NTU.

#### Experimental Procedure
At the beginning of an experiment, all valves and connections were checked **[Grammar? Figure out which tense you are using and stick to it. Note: Your report should be in consistent past tense.]** to ensure desired pathways were clear and undesired pathways were blocked. Next, water and coagulant pumps were set to desired experimental flow rates. The clay stock tank was filled with clay and tap water, and the coagulant stock tank was filled with coagulant and deionized water at the proper concentrations. Next, the clay, coagulant, and waste pumps were turned on. Lastly, ProCoDA was turned on and the state was set to PID Control.

## Results and Analysis
A successful experiment in the context of the Bottom Geometry team would mean that the floc blanket is stable and there is no buildup of flocs at the bottom of the tube settler, or gelling. Floc blankets form when flocs continually recirculate and suspend in the tube settler; the formation of a floc blanket is influenced by the bottom geometry because the geometry determines whether flocs will settle at the bottom. A flat geometry allows flocs to settle, while a sloped geometry would cause flocs to slide down, preventing a floc from being stagnant.

A stable floc blanket is indicated by the effluent turbidity -- effluent turbidity is inversely correlated with performance; i.e. a lower effluent turbidity indicates better performance and greater floc blanket stability, which means the floc blanket does not decay. A stable floc blanket is also indicated by the time it takes for the effluent turbidity to start increasing after reaching the maximum removal. If it takes a longer time for turbidity to increase, the blanket is more stable.

### Baseline Experiment
A baseline control experiment, at 2 mm/s upflow velocity, was conducted without any printed inserts. As seen in Figure 11, the effluent turbidity lies between 4 to 40 NTU. Within the first ten hours of the experiment, the effluent turbidity remained fairly constant, therefore indicating a floc blanket formed and stabilized; however, the floc blanket began to decay exponentially, illustrated by the rapid increase in effluent turbidity after the tenth hour. Flocs also settled at the bottom of the tube settler, producing "gelling," or forming a thick and dense layer, in a very compact manner (Figure 12). The exponential increase of the turbidity indicated an exponential decay of the floc blanket. This led to the implementation of the stacked cylinder design, whose goal was to stabilize the floc blanket and prevent gelling.

![Baseline Results](https://raw.githubusercontent.com/AguaClara/HRS-Bot-Geo/master/2019%20Spring/images/Control_Exp_3-8.JPG)
Figure 11: Baseline experiment results. The turbidity increased exponentially.

![Gelling in Baseline Experiment](https://raw.githubusercontent.com/AguaClara/HRS-Bot-Geo/master/2019%20Spring/images/floc%20buildup.jpg)
Figure 12: Gelling at the bottom of the tube settler.

### Experiment with 45° Cylindrical Insert
The following data was collected for an experiment running at 2 mm/s that included the 45° cylindrical insert to alter the bottom geometry of the tube settler.

![Stacked Cyl Results](https://raw.githubusercontent.com/AguaClara/HRS-Bot-Geo/master/2019%20Spring/images/First_Bott_Geo.JPG)
Figure 13: Results from using the stacked cylinder 3D printed insert.

![Stacked Cyl Gelling](https://raw.githubusercontent.com/AguaClara/HRS-Bot-Geo/master/2019%20Spring/images/stackedcyl1%20floc%20buildup2.jpg)
![Stacked Cyl Gelling Closeup](https://raw.githubusercontent.com/AguaClara/HRS-Bot-Geo/master/2019%20Spring/images/stackedcyl1%20floc%20buildup1.jpg)
Figure 14: Gelling in the experiment with the stacked cylinder 3D printed insert.

In the experiment with the stacked cylinder insert, the floc blanket (which also formed and stabilized within the first ten hours) did not decay as quickly as that in the baseline experiment, which was indicated by a less steep increase in effluent turbidity (see Figure 13) compared to the baseline experiment. This was likely due to the bottom geometry, whose sloped sides allowed flocs to slide down and be resuspended by the inflow of water. However, gelling was still observed, but was a less compact type of gelling as can be seen in Figure 14. We have concluded the gelling was likely due to the angle of the slope of the insert, which is 45°, and kinetic or rolling friction (the force that resists an object's motion when the object rolls on a surface) because although an increase in the slope angle reduces the rolling friction, an increase in weight increases the rolling friction.

Within the first ten hours of the experiment, the rolling friction did not affect the individual flocs as much because of the flocs' weight, a relatively small weight. This lack of rolling friction allowed the flocs to slide down the slope, thus preventing flocs from stacking on top of each other and creating buildup. However, as the flocs began to stack on top of each other, due to the angle of the slope, their combined weight increased, which caused the rolling friction to increase. With the flocs moving at a slower speed and less freely at the bottom of the stacked cylinder insert, flocs began to stack on top of each other, which was also seen in the baseline experiment.

The gelling in both experiments create a positive feedback loop in which floc buildup is amplified. For example, gelling creates a dense layer of flocs within a horizontal cross section of the tube settler, which decreases the empty area in the cross section. Below is the equation that relates flow rate to cross sectional area and velocity.

<div style="text-align:center"><img src ="https://raw.githubusercontent.com/AguaClara/HRS-Bot-Geo/master/Images/q%3Dav.svg?sanitize=true" /></div>

According to the equation, if Q (flow rate in units of volume per time) is held constant, and A (area in units of area) is decreased, then v (velocity in units of distance per time) is increased. If the velocity is increased, then the flocs are carried along the inflow of water. Traveling in the direction of the velocity does not allow the flocs to have the opportunity to recirculate and resuspend in the tube settler and instead settle into the floc buildup or gel. Since the buildup continues to grow, the area is continually decreased and the velocity is continually increased, causing more and more buildup.
There is also a spike in the data that is followed by a decrease in the effluent turbidity. This likely occurred because the floc blanket was agitated. The flocs were still stacked together, but because of gelling they were able to move through the tube settler as a group. As they moved upwards, they were able to push the non-bounded flocs (located at the top of the settler tube) out of the tube and into the effluent turbidimeter, increasing the effluent turbidity measured.

In terms of how these results relate to future work, it is confirmed that a slope angle of 45° is too low and it has been increased in the new insert designs, that we will begin to experiment with in future experiments.

 **[Use consistent past tense]**

## Conclusions
The Bottom Geometry team noticed significant differences between their results and that of previous AguaClara teams. Unlike previous semesters, the team tested inserts with sloped, and moved away from conical designs. The new cylindrical insert showed an improvement in reducing effluent turbidity, and therefore a reduced rate of floc blanket decay. However, a slope of 45° for the insert is too shallow and needs to be increased in future experiments. Without an insert at the bottom of the tube settler, the floc blanket began to decay exponentially; however, when an insert was attached to the tube settler, the floc blanket decay began to decay linearly and did not decay exponentially like the baseline experiment.

The team has determined that it is more beneficial to have inserts in order to prevent floc decay; however, these inserts still cause floc buildup and gelling. Therefore, the team will continue to work on and improve their cylindrical design by detemining the best angle to prevent gelling. In terms of how this relates to AguaClara, the Bottom Geometry team is making progress in finding an optimal angle in the sloped insert that can eliminate gelling.

## Future Work
Next steps include designing an insert that fits into the visible, transparent part of the tube settler to understand how flocs and the geometry interact. The cylindrical insert only fit into the coupling that is screwed into the bottom of the settler, so the interaction between the flocs and the sloped geometry was not seen. Designing a longer cylindrical insert for the tube settler would elucidate what slope angles are optimal to prevent floc buildup. Greater slope angles (or steeper sides) will be tested for a 2 mm/s upflow velocity as well as a 3 mm/s upflow velocity.

A successful insert would be a great benefit to the AguaClara Cornell lab. This insert would eliminate floc buildup at the bottom of the tube settler, which would decrease the maintenance and cleaning time of any lab apparatus, allowing researchers to carry out experiments more quickly. After such an insert is designed, research in this area should end because the filter would have completed its role of reducing cleaning time -- no further work is needed.

## Manual
### Purpose and Hypothesis
The purpose of the Bottom Geometry team is to find an optimal bottom geometry of the tube settler that prevents floc buildup, or gelling because the removing the buildup and cleaning the apparatus is very time consuming. If floc buildup can be avoided, running experiments will be more efficient since researchers will spend less time cleaning the apparatus. The hypothesis is that geometries that involve flat or regular cone shapes cause floc buildup, and geometries that involve sloped sides do not.

### Materials List
A materials list is included below.
- Four pumps
  - 1 water pump
  - 1 clay pump
  - 1 coagulant pump
  - 1 effluent pump
- 1 flocculator (tubing wound around cardboard tube)
- 1 clay stock tank
  - clay from stock
  - tap water
- 1 coagulant stock tank
  - PaCl of known concentration
  - deionized water
- 1 pressure attenuator (plastic bottle)
- 2 turbidimeters
- 1 tube settler
- tubing
- 3D printed insert

### Apparatus Setup
See the [Experimental Apparatus](#Experimental-Apparatus) section for more details. Follow the same tubing connections.

![HRS Bottom Geometry Apparatus](https://raw.githubusercontent.com/AguaClara/HRS-Bot-Geo/master/Images/ExperimentalApparatus.PNG)
Figure 15: Bottom Geometry apparatus with labeled components.

### Procedure
#### PaCl Dosing Calculations

The calculation logic for determining the coagulant dosing is derived from Dr. Monroe Weber-Shirk's CEE 4540 lecture notes.

```Python
## PACl Dosing

from aguaclara.play import*

#inputs
C_sys = 4.5*(u.mg/u.L)         #C_sys is the desired concentration of coagulant in the system
C_labstock = 70.28*(u.g/u.L)   #C_labstock is the concentration of coagulant in the stock
Q_sys = 1*(u.mL/u.s)           #Q_sys is the flow rate of the system
K_dilution = 5*(u.mL/u.L)      #K_dilution is the volume of coagulant per liter of distilled water
V_reservoir = 5*(u.L)          #V_reservoir is the volume of the coagulant stock tank in the system
Frac_reservoir = .76
Q_per_rpm = .00195 *(u.mL/u.s) #Q_per_rpm is the coagulant pump flow rate per rpm

#Calculations
M_flow_coag = (Q_sys * C_sys).to(u.mg/u.s)
C_reservoir = (C_labstock * K_dilution).to(u.gram/u.L)
Q_reservoir = (M_flow_coag / C_reservoir).to(u.mL/u.s)
V_lab = ((V_reservoir * C_reservoir) / C_labstock).to(u.L)

#Outputs
RPM = Q_reservoir / Q_per_rpm                                       #RPM is the RPM required for coagulant dosage
RunTime = ((V_reservoir * Frac_reservoir) / Q_reservoir).to(u.hour) #RunTime is the run time of the system

print('The RPM needed for this coagulant dosage is' ,RPM)

print('The run time is ', RunTime)
```

#### Cleaning the Apparatus
1. Drain the tube settler.
    1. Close the valves that are connected to the tube where water is flowing into the tube settler (between flocculator and tube settler) and into the effluent turbidimeter (between tube settler and turbidimeter). Disconnect both tubes and let the water drain into a waste bucket.
    2. Close the valve that is connected to the bottom end of the floc weir and disconnect the tube connected to the floc weir. Reopen the valve to let water drain from the weir. Reconnect the tube.
    3. Reconnect the tubes connected to the tube settler and reopen the valves closed in Step 1.1.
2. Clean the turbidimeters as per the instructions in the [AguaClara Tutorial Wiki Page](https://github.com/AguaClara/aguaclara_tutorial/wiki/Cleaning-a-Turbidimeter).
3. Run water through the system at 150 RPM. To clean the flocculator, open the valve that connects the flocculator to the syringe. When the syringe is halfway filled, push to empty the syringe and to flush water through the flocculator. Repeat until the flocculator is cleared of clay, and close the valve when finished.
4. Continue to run water through the system until the influent and effluent turbidimeters read 0 to 1 NTU.

#### ProCoDA Settings
![PID Control Outputs](https://raw.githubusercontent.com/AguaClara/HRS-Bot-Geo/master/2019%20Spring/images/pid%20ctrl%20outputs.jpg)
![PID Control Rules](https://raw.githubusercontent.com/AguaClara/HRS-Bot-Geo/master/2019%20Spring/images/pid%20ctrl%20rules.jpg)
Figure 9: Rules and Outputs of PID Control. These are the parameters used in the experiments.

Table 1: This table details the set points in ProCoDA for the PID Control state.

| Set Point             | Setting |
|:--------------------- |:------- |
| Turb Target           | 100     |
| P                     | 68      |
| i                     | 125     |
| D                     | 0       |
| Influent Turbidty ID  | 1       |
| Effluent Turbidity ID | 2       |
| Floc removal time     | 10      |
| Run time              | 3590    |
| Fast pump             | 0.5     |
| Normal pump           | 0.12    |

#### Experimental Procedure
1. Check all valves and connections to make sure desired pathways are clear and undesired pathways are blocked.
2. Verify water and coagulant pumps are set to desired experimental flow rates.
3. Fill clay stock tank with water and clay. Tap water will suffice. Turn on the stirrer.
4. Fill coagulant stock tank with water and coagulant.
    1. In a 1L graduated cylinder, fill to top with deionized water. In a smaller graduated cylinder, measure out 5 mL of coagulant. Pour into the 1L graduated cylinder, and pour into coagulant stock tank. Repeat until the stock tank is fully filled.
5. Turn on the clay, coagulant, and waste pumps.
6. Turn on ProCoDA and set state to PID Control to turn on the clay pump.
7. After the experiment has run for the desired runtime, set ProCoDA state to OFF, and turn off the water pump and coagulant pump.

#### Data Collection and Analyzation
Data is automatically collected by ProCoDA in an Excel sheet. For experiments that run over the course of two days, two sheets are produced. The key parameters for the data is the day fraction, influent turbidity, and effluent turbidity. Day fraction represents the fraction of a day since the beginning of that day starting at midnight. The beginning of an experiment is indicated by the influent turbidity. The point where the influent turbidity begins to stabilize at 100±5 NTU is where the experiment begins, and all data after this point is valid until the experiment ends. Next, the Day Fraction column of the first sheet is analyzed. To convert day fraction to hours since experiment started, a formula is used in Excel. The first value in the Day Fraction column is subtracted from the first value in the Day Fraction column and multiplied by 24 hours to represent the 0th hour since the experiment started. The first value in this column is subtracted from the second value and multiplied by 24 hours, and so forth. Each time has an associated effluent turbidity value.

For the second sheet that contains data collected from the second day of the experiment, a different formula is used to find the time since the experiment began for the to run. Starting with the first value in the second sheet, the first value from the second sheet is subtracted from the first value from the second sheet, multiplied by 24 hours, and the last converted day fraction value from the first sheet is added. This formula is applied to the rest of the day fraction values in the second sheet. These times also have an associated effluent turbidity value. A graph was created to plot the effluent turbidity over time that the experiment ran.

![Example Day Fraction Conversion](https://raw.githubusercontent.com/AguaClara/HRS-Bot-Geo/master/2019%20Spring/images/example%20data%20calc.PNG)
Figure 16: An example day fraction conversion to time since the experiment started. The last three values of the first sheet and the fist three values of the second sheet are included and the formulas are shown.

The following code was used to graph the data collected from the experiments. The sheer amount of data, over 100,000 data points, was too much for Python to graph and had a very long processing time. The team decided that it would be more efficient to graph the data in Excel. The code below works for fewer data points, i.e. 10,000. 

```Python
import matplotlib.pyplot as plt
import xlrd
import numpy as py
file_location = "/Users/dowens2017/Desktop/AguaClara/newnewexcel.xlsx"

workbook = xlrd.open_workbook(file_location)
first_sheet = workbook.sheet_by_index(0)

# x axis values
x = [first_sheet.cell_value(i, 0) for i in range(10000)]
# corresponding y axis values
y = [first_sheet.cell_value(i, 1) for i in range(10000)]

# plotting the points
plt.plot(x, y)
```
