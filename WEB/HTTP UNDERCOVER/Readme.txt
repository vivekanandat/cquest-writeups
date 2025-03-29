This is a web exploitation challenge and you are provided with a URL:
https://esrimaniteja.pythonanywhere.com/

its a simple login page where you have two options to login as admin or user
(I have provided the screenshots of this challenge solution in this directory)

So the admin button is blocked in the frontend and in order to get the flag you should login as admin with basic username asd password(username: admin  password: admin)

Follow the steps:
-Open Burp-Suite(available in both Windows and Linux)											(Screenshot-1)
-In proxy tab switch on the "Intercept"															(Screenshot-2)
-Now open the browser of burp-suite															(Screenshot-3)
-Now copy and enter the url i have provided above in browser
- the burpsuite intercepts before loading the site so click forward, now the page will be loaded		(Screenshot-4)
-Enter username: admin, password: admin   and click, the burpsuite will intercept 					(Screenshot-5)
-Now after change the "role=user" to "role=admin" in the bottom of the request message 			(Screenshot-6)
-click forward, there you go now you have logged in as admin and you will be able to see the flag		(Screenshot-7)

flag: cquest{Th1s_is_Bas1c_Int3rc3ption}


Author: E. Srimani Teja