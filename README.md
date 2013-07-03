There are 2 folders:DrRobotMotionSensorDriver and drrobot_jaguar4x4_player.

You could copy all 2 folders to your ROS working folder.

For git user, you need clone these 2 folders from repository.

Use "make clean" in each folder to clean all the cache/build files.
Then use "rosmake" to build again.

You need make sure you already installed all the depend packages. You could find them in manifest file in drrobot_jaguar4x4_player folder.


The demo program will public all the sensor information and received command from joystick to control the robot.
After run roscore
you could use command " roslaunch drrobot_jaguar4x4_player drrobot_play1.launch" to lauch all the program.
It will auto load the parameter file "drrobotplayer_jaguar4x4.yaml" to ros parameter server.
If you modified IP, you could edit this file.

IMU: now the sample code will publish the IMU raw data. You need referee the datasheet to transfer the value to real sensor reading.
	Accelerometer Sensor: ADXL345
	Gyro Sensor: ITG3200
	Magnetometer Sensor: HMC5883L

GPS: You could find ROS package at http://www.ros.org/wiki/gpsd_client/Tutorials/Getting%20Started%20with%20gpsd_client
	After you install GPSD server and GPDS client. 
	1 .You could access the GPS on the robot by command:
		gpsd tcp://192.168.0.61:10002
	2. You could check the gpsd running by command:
		gpspipe -r
	   It should ouput NEMA sentences.
	3. Then you could run gpsd_client (with roscore)
		rosrun gpsd_client gpsd_client _host:=localhost _port:=2947 _use_gps_time:=false _check_fix_by_variance:=false
	4. THen you could use rostopic to check the publish "fix" message
		rostopic echo /fix

	
Axis camera:	http://ros.org/wiki/axis_camera
	Please note: the default setting for camera on the robot is:
		IP:192.168.0.65
		Port:8081
		ID: root
		PWD: drrobot

Laser(Hokuyo) : You could find more information from ROS
			http://www.ros.org/wiki/hokuyo_node
			http://www.ros.org/wiki/hokuyo_node/Tutorials/UsingTheHokuyoNode
		On the robot, by default, the laser scanner is connected as network device, IP:192.168.0.60, port:10002
		So you need redirect the TCP socket to serial port as hokuyo_node used.
		You could find and install some virtual serial port redirect  software to do it.
		One is "socat". Use "sudo apt-get install socat" to install it.

		After that:
		1. sudo mknod -m 666 /dev/ttyS51 c 4 115
		2. sudo socat PTY,link=/dev/ttyS51, TCP4:192.168.0.60:10002
		3. open another terminal, to check the /dev/ttyS51 read/write permision.
			If it is linked to /dev/pts/*, check it too.
			Maybe you need use "sudo chmod a=r+w /dev/pts/*"
		4. after run roscore, open another terminal,
			"rosrun hokuyo_node getID /dev/ttyS51"  -- will return the device ID
			"rosrun hokuyo_node getFirmwareVersion /dev/ttyS51"  -- will return the device firmware version
		5. set port number for hokuyo_node
			rosparam set hokuyo_node/port /dev/ttyS51
		6. Run hokuyo_node
			rosrun hokuyo_node hokuyo_node
		7.you could use "rostopic echo /scan" to view the scan data.
			or use rviz to view.

				

		

