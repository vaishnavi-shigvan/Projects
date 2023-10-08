#Home Automation System Using Raspberry Pi-

Introduction- 
IoT is essentially a platform where embedded devices are connected to the internet so they can collect and exchange data with each other. The term IoT describes the network of physical objects – things that are embedded with sensors, software and other technologies for the purpose of connecting and exchanging data with other devices connected over the internet.
The focus of our project is on helping users to operate home appliances from their own smartphones. Users will be able to control the home appliances using a Bluetooth connection or a smart assistant that is available on Android Smartphones such as Alexa. The goal behind IoT is used to have devices that self-report in real time, improving efficiency and bringing important information to the surface more quickly than a system depending on human intervention.

Motivation -
The spread of Covid-19 all over the world has brought the world into a pandemic state. It has made a powerful impact on the consumption of energy due to continuous usage of home appliances by multiple family members simultaneously. It has posed some serious issues for the environment, global economy and our personal lives. Safety of the user in the existing traditional system is a major concern for every household.

Problem Statement-
	The involvement of physical switches and other operating mechanisms in today’s system has made a huge impact on how we interact with the appliances in our homes. There are often times when these mechanisms are left unattended which result into unnecessary increase in power consumption, and ultimately, increase in cost of operation on the utilities which may drastically affect our economical capabilities.
It can be inconvenient as well as inconsistent to always require human intervention to operate the appliances. In homes, the switches are installed in the particular area which control the limited set of appliances. Lack of interconnectivity amongst these appliances make them inconvenient to operate as there is no centralised controlling unit. 

System Analysis-
•	Existing System-
1.	Power consumption and the cost of using day to day appliances.
2.	The safety of the end user is a big issue and the loose electric components are not reliable.
3.	Physical interaction with the controlling system is required.
4.	Unattended appliances may cause life threatening consequences. 


•	Scope & Limitations of Existing System- 
		In this century, the increase in the usage of electrical appliances is tremendous. The tremendous rise power consumption has resulted into major environmental crisis that include excessive generation of heat, which contributes to global warming. Furthermore, the devices in the existing system have very limited scope as they are not interfaced for any kind of soft communication with other devices / appliances in the system i.e. they are stand-alone devices. This not only gives rise to inconvenience, but may also prove to be as a hazardous environment for the user.
However, even in the most ideal implementation of the existing system models, the switches or other controlling mechanisms always require physical human interaction, which may not always be possible and there is no way to remotely control these devices and they are left in unattended state.

•	Proposed Project Scope -
The aim is to simulate a small scale prototype that establishes wireless remote control over a network of home appliances. The application is designed to run on the commands given by the user in the Bluetooth controller app (Pi3 Bluetooth Manager), which is bridged with a python program that uses Bluetooth socket module and the RPi library. 
The system can be implemented in homes as well, being in-charge of control of the electrical appliances.
The development of technology friendly environment. The system incorporates the use of
technology and making Home Automation System.
The scope of IoT-based home automation increases by the day because it is a growing technology.

•	Integrating smart home devices-
Feasibility study 
•	Technical Feasibility 
The total number of entities and components involved in this project were 4(Raspberry Pi 3 model b+, Relay Module, Bluetooth device, Amazon Alexa assistant). The major part of the project works on aforementioned hardware and the software support from Amazon INC and the Bluetooth Low Emission (BLE) Technology. This home automation system, in
addition to contributing to energy efficiency, comfort and safety, will have the capacity to contribute to the reduction of different electrical anomalies observed in the existing system.

•	Operational Feasibility
The administrative components are useful for controlling the appliances connected in the network.
The connected LEDs don’t play a major role other than to operate on the given commands by the user.
In the experimental tests that were performed, a 3m range was obtained without any interference or obstacles in between, guaranteeing full coverage of the area of a single room. User can use the integrated interface to interact with Alexa.


•	Economical Feasibility
The initial setup cost of the home automation system is radically high but once the system is up, no additional expenditure is needed to implement the new devices into the system. The objective that led this study was to explore and investigate the increase in comfort and safety and reduction in the electrical energy consumption so that it is possible to achieve greater energy efficiency.

System Design- 
•	Raspberry Pi 
The Raspberry Pi is a credit card–sized single-board computer. Raspberry pi is low cost minicomputer. It is possible to connect Monitor of PC as well as television to the Raspberry pi. Mouse and Keyboard can be connected to the Raspberry pi. All models having a Broadcom system on a chip, it includes an ARM compatible central processing unit (CPU) and an on-chip graphics processing unit (GPU). CPU speed ranges from 700 MHz to 1.2 GHz for the Pi 3. On board memory range from 256 MB to 1 GB RAM. SD cards are used to store the operating system and program memory. Most of the Raspberry pi board are having USB ports, HDMI port, Audio jack, 40 GPIO pins, In-built Bluetooth, WIFI and so on.

Raspberry pi is having its own LINUX based operating system. We have used Raspberry Pi OS (raspios-bullseye-arm64) on our Pi. Installation of the operating system is also possible by using the NOOBS software. Raspberry pi supports different programming languages like C++, Python, SQL. It also supports java, javascript, php and so on. 

•	Relay Module 
Relay is an electromagnetic switch. Relay allows one circuit to switch on or off another circuit while they are separated. Relay is used when we want to use a low voltage circuit to turn ON and OFF the device which required high voltage for its operation. For example, 5V supply connected to the relay is sufficient to drive the bulb operated on 230V AC mains. Relays are available in various configurations of operating voltages like 6V, 9V, 12V, 24V and so on. Relay is divided into two parts, one is input and other is output. Input side is a coil which generates magnetic field when small input voltage is given to it. 
Relay has three contactors: Normally closed (NC), Normally opened (NO) and common (COM). 
By using the proper combinations of the contactors electrical appliances may turn ON or OFF.

  
Relay Module-
•	Mobile Devices- 
Mobile devices are noting but small computing devices. They are small enough so that we can operate and hold in hand. They are also having their own operating systems. Mobile device can be move from one location to other. Example of mobile devices are: Smart phones, Laptops, Tablets and so on.
	
Sensors / Component details- 
•	Inbuilt Bluetooth sensor 
•	Female to female connector
•	USB adapter

Implementations Details -
          The designed board has 4 sockets. We have used a channel relay module. Each of the socket represents device that will be connected to our system. Due to the limited scope of the scalability, let us assume that 4 LED Bulbs connected to these sockets represent different devices. So lighting the bulb ON/OFF will signify that we have turned ON/OFF the specific device.

•	Board implementation-
Our holders are connected to each other in the following manner –
Ground (GND) of each holder is interconnected to the other as a common GND. 
Live wire of each device is separate and not interconnected. 

•	Relay Implementation -
Live wire of each holder has been independently given as the Normally Open(NO) to the Relay Module. All the Common Contactors of every Channel of our Relay Module are interconnected. The live wire of Relay module and the common GND wire have been further used to make a plug, which will go into the 230V AC mains power source.

•	Raspberry Pi Implementation-  
Firstly, we have connected the VCC and GND of our Raspberry Pi(GPIO.BOARD Pin number 2 and GPIO.BOARD Pin number 6 respectively) to the VCC and GND on our relay module.  


For input 4 on relay module-
We have used GPIO.BOARD Pin 15 to act as an input, that will perform the operations as per the python program.

For input 3 on relay module 
We have used GPIO.BOARD Pin 13 to act as an input, that will perform the operations as per the python program.

For input 2 on relay module 
We have used GPIO.BOARD Pin 11 to ac t as an input, that will perform the operations as per the python program.

For input 1 on relay module
We have used GPIO.BOARD Pin 40 to act as an input, that will perform the operations as per the python program.

Installation of Raspios-bullseye-arm64- 
Step1 : Install and run Rufus Utility  	    
Step 2 : Select the SD card for installing our OS as the   devices	  
Step 3 : Boot Selection  : Disk or ISO Image
Step 4 : Start
         

The Rufus utility will display a warning message “all the contents on the SD card will be erased” in order to install the OS on the SD card.
Accept and install the operating system.


	Software Specifications -
	Smart Assistant application: Alexa installed on Raspberry Pi
	Implementation using Python
	Raspios-bullseye-arm64 for Raspberry Pi 3B+
	Pi3 Bluetooth Controller App


	Hardware Specifications -
	Raspberry Pi 3 Model B+ BCM2837B0 SoC. IoT, PoE Enabled
	16 GB SD Card
	4 Channel relay module (5V)
	Android Device 

 Test Cases 
•	Behavior of system on invalid commands 
•	Behavior of system on valid commands 


Module Name : Valid Inputs
 	 	 	 	 	 	 	 
Test Scenario ID	Bluetooth inputs	Test Case ID	Bluetooth inputs - 1A
Test Case Description	Bluetooth input - Positive test case	Test Priority	High
				
Pre-Requisite	NA	Post-Requisite	NA	
Test Execution Steps	 
 	 	 	 	 	 	 	 	 	 
Sr. No.	Action	Inputs	Expected Output	Actual Output	Test Result
1	Enter valid LED number with +	1	LED 1 turns on	LED 1 turned on	Pass
2	Enter valid LED number with -	-1	LED 1 turns off	LED 1 turned off	Pass
3	Enter valid LED number with +	2	LED 2 turns on	LED 2  turned on	Pass
4	Enter valid LED number with -	-2	LED 2 turns off	LED 2 turned off	Pass
5	Enter valid LED number with +	3	LED 3 turns on	LED 3  turned on	Pass
6	Enter valid LED number with -	-3	LED 3 turns off	LED 3 turned off	Pass
7	Enter valid LED number with +	4	LED 4 turns on	LED 4  turned on	Pass
8	Enter valid LED number with -	-4	LED 4 turns off	LED 4 turned off	Pass
9	Exit the program	exit	Program stops	Program stopped and Bluetooth disconnected	Pass

Test Scenario ID	Bluetooth inputs	Test Case ID	Bluetooth inputs - 1B
Test Case Description	Bluetooth input - Negative test case	Test Priority	High
				
Pre-Requisite	NA	Post-Requisite	NA	

Sr. No.	Action	Inputs	Expected Output	Actual Output	Test Result
1	Enter invalid LED number with +	12	Nothing happens	Nothing happens	Pass
2	Enter invalid LED number with -	-13	Nothing happens	Nothing happens	Pass
3	Random text	dfhhf	Program should exit	Program exited	Pass

Conclusion & Recommendation 
Implementation of Home automation system is completed successfully using Bluetooth and Raspberry Pi. It is reliable and scalable home automation system with low cost and easy to implement. It makes human life comfortable, convenient and safe.
Thus, the designed system accomplishes the goal of implementing an extensively open-sourced Home Automation System using wireless communication and co-dependency of multiple home appliances on a centralised controlling system in a particular environment. 

Limitations -
	Due to the security policy imposed by Amazon INC, the current installation of Alexa on the Raspberry Pi is interactive with the user but it does not allow certain features such as:
1.	Music playback or music controls. 
2.	Controlling other devices that are connected in the same network.
3.	Modifying the system settings or working with the permissions without the user’s interference. 
4.	Controller device and the system needs to maintain a Bluetooth connection all the time to operate.
5.	Poor Bluetooth connection or too many obstacles that hinder the range of the connection may affect the efficiency of the system.
6.	User must always have access to the smartphone which acts as a controlling device to the proposed system.
7.	Physical security of hardware and the appliances, from theft, can’t be guaranteed.
8.	Over a period of time, the components may not perform optimally and their mission capability may adversely affect due to degradation of manufacturing quality.
9.	Poor integration of multiple devices into the system may adversely affect the functioning of the entire system.
10.	An active internet connection is required for user to interact with Alexa.

 Future Scope- 
            Future scope for the home automation system involves making homes even smarter.     Homes can be interfaced with sensors including motion sensors, light sensors and   temperature sensors and provide automated toggling of devices based on conditions.
           The aforementioned limitations can be overcome with further development on the proposed system with the help of developers and engineers that will work on the physical scalability and the intermediate entities involved with Amazon INC. 
1.	User(s) will be able to control the music playback and interact with the multiple music-streaming platforms in multi-room.
2.	Controlling and interacting with the other smart devices in the environment will be possible. 

Bibliography & References -
Installation of Amazon Alexa on Raspberry Pi and activating the product 

•	https://developer.amazon.com/en-US/docs/alexa/avs-device-sdk/raspberry-pi-script.html
•	https://developer.amazon.com/en-US/docs/alexa/avs-device-sdk/raspberry-pi.html
•	https://developer.amazon.com/alexa/console/avs/products/EchoR3pi/details/capabilities

Product Page -
•	https://developer.amazon.com/alexa/console/avs/products/EchoR3pi/details/info
