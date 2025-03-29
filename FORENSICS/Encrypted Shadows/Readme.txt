This is a basic Steganography in Forensics and the flag here is divided into 3 parts and each part is encrypted in 3 different Cryptographic algorithms as follows:

flag_part_1 = St4ings         			use base-64 to decode                   U3Q0aW5ncw==
second = _St3g6n0gr4ph1c	use vigenere decoder 			_Cx3e6x0kp4zl1a
last_one = _Ch4ll3ng3			use ROT13 decoder			_Pu4yy3at3

you are provided with a text and you find the flag parts in the file in two ways:
Method 1:
Open the file directly in notepad search(Ctrl+F) for "flag" and remaining also you can find in same way 

Method 2:
Use strings command along with grep to find the flag.
Do this in Kali terminal with following command:
cmd: 
 1)  $ strings Steg.JPG | grep "flag"
result: flag_part_1 = U3Q0aW5ncw==

 2)  $ strings Steg.JPG | grep "second"
result: second = _Cx3e6x0kp4zl1a

 3)  $ strings Steg.JPG | grep "last"
result: last_one = _Pu4yy3at3


flag:  cquest{St4ings_St3g6n0gr4ph1c_Ch4ll3ng3}


Author: E. Srimani Teja