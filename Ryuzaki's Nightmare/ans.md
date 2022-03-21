We were provided with an apk. 
The apk, once installed on an android device, asked us to input a 4 digit PIN in order to reveal the flag. 
First we had decompiled the apk. Upon realizing that it is a flutter based application we decided to focus efforts on brute forcing the application. 
The easiest and fastest way to accomplish this task is through the use of ADB and android emulators. 
We had setup a total of 7 android emulators spread across 2 PCs using android studio's VM to allow for parallelization of the brute force attempt
since our bottleneck was the adb process itself, rather than the VM. 
Given an aprox time of 5 seconds per attempt, we estimated a total time of 5*9999/7 = 7142 seconds, which was feasible.
Using the python script(attached) which input the pin and checked in the UI dump for the text 'invalid', we were able to let the brute force attack run unsupervised. 
After 3-4 hours the pin was revealed to us and we were able to access the flag.

//complete