We were provided with an apk. 
The apk, once installed on an android device, asked us to input a 4 digit PIN in order to reveal the flag. 
First we had decompiled the apk. Upon realizing that it is a flutter based application we decided to focus efforts on brute forcing the application. 
The easiest and fastest way to accomplish this task is through the use of ADB and android emulators. 
We had setup a total of 7 android emulators spread across 2 PCs using android studio's VM to allow for parallelization of the brute force attempt
since our bottleneck was the adb process itself, rather than the VM. 
Given an aprox time of 5 seconds per attempt, we estimated a total time of 5*9999/7 = 7142 seconds, which was feasible.
Using the python script(below) which input the pin and checked in the UI dump for the text 'invalid', we were able to let the brute force attack run unsupervised. 
After 3-4 hours the pin was revealed to us and we were able to access the flag.

'''
import subprocess
subprocess.call("adb devices",shell=True) 

for x in range(1441, 0, -1): #adjust range based on vm
	f = "adb -s emulator-5556 shell input \"keyboard text \'" + str(x) + "\'\""
	subprocess.call("adb -s emulator-5556 shell input keyevent 67 keyevent 67 keyevent 67 keyevent 67",shell=True)
	subprocess.call(f,shell=True)
	subprocess.call("adb -s emulator-5556 shell input tap 498 1182",shell=True)
	temp = str(subprocess.check_output("adb -s emulator-5556 exec-out uiautomator dump /dev/tty",shell=True))
	print(x)
	if("Invalid" not in temp):
		print("breaking")
		print("pin is: ",x)
		break
	subprocess.call("adb -s emulator-5556 shell input keyevent 4",shell=True)
'''
