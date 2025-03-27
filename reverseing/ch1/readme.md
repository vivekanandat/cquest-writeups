
![image](https://github.com/user-attachments/assets/4250eeba-440b-4bd7-90b7-f3a711fa16b4)

we can see that running the binary does nothing


before opening the binary in gdb for analysis we can run strings cmd to get all the strings in the binary file(this might give us the flag if we r lucky)

![image](https://github.com/user-attachments/assets/85ad0ad7-a40f-4203-a7d2-7fb173f4d4d0)

thats a lot of data we can now either go through all this data to check if the flag is present or ....

![image](https://github.com/user-attachments/assets/54a43fa1-c468-4788-bb32-3b926ecaeb51)

since we already know the flag format we can use grep for that 

and we have the flag
