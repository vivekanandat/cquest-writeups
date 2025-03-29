This is an interesting challenge where you are provided with a text file  and an audio file which is of morse code.
So you can decrypt the morse code by uploading the Audio.wav file in this 
site: 
https://morsecode.world/international/decoder/audio-decoder-adaptive.html

and you will get a cipher text.

Using the provide text file (you can just open it directly in Notepad/Notepad++) you can obtain the values
p = 223939690746282032692539535413320285341
q = 300338504290014435742959857096087515739
n = 67257711769906732313192328723869749100314309560813077584055717024951308481999

and you can get the cipher text from morse audio file as:
c = 1745367374812276391491162919649708583447060075052246847607586280214637444921

So these are the values which are used to perform RSA Decryption and p, q are two prime numbers and you can decipher this in this site of RSA Decoder : https://www.dcode.fr/rsa-cipher
There you go the flag is:

cquest{W0w_y0u_a4e_qu1t3_g00d}



Author: E. Srimani Teja


 