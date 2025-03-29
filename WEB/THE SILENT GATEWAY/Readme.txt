This is also a challenge where you need to solve it using burpsuite. So you are provided with a URL:
https://rogteja.pythonanywhere.com/

of a simple login page
where you need to bypass the authentication in order to get the flag.
Follow the same steps as given in the "HTTP UNDERCOVER" till opening the url in burpsuite browser
Now in order to bypass the authentication you need to add a header in the header sections of the request when you try to login with
username: admin  password: password

The header is:
Name: X-Auth-Bypass
Value: open_sesame

click add and click forward, there you go now you can see the flag in the site 

flag: cquest{Header_Havoc_Mastered}

(Screenshots are given in this directory)


Author: E. Srimani Teja