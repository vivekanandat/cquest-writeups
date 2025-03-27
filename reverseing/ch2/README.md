![image](https://github.com/user-attachments/assets/310f9077-4082-430f-8c7b-30e643ae2520)![image](https://github.com/user-attachments/assets/87d48df1-361a-4578-a0bb-a8c31eea3cac)

ok here we have to give some input so now we need to analyze it but lets just run strings just in case

![image](https://github.com/user-attachments/assets/62d6d0a1-7ca9-4757-94a1-b5755e94ed68)

ok we get nothing so lets move on

now to open a binary file u need disassemblers(they disassemble the binary file and show it to us in assembley code).im using ida for this

![image](https://github.com/user-attachments/assets/9fecec65-74b8-4205-9f50-3a4020f0dc0e)

nothing important here so lets go to the get_flag() function

![image](https://github.com/user-attachments/assets/26040ce4-5a9d-4c92-99e3-f025c7122fd9)

![image](https://github.com/user-attachments/assets/53c398f8-5fd5-420c-b0b4-4ef22c59d054)

here the program checks if the len of input is equal to 0A(10 in hexadecimal) if its true then it proceeds to next step

![image](https://github.com/user-attachments/assets/77e4ec36-bfb1-4e98-b775-7312c4452df4)

after that check the program goes through a series of if conditions and calls the print_flag() function

![image](https://github.com/user-attachments/assets/cf7a72ed-1e24-4213-9712-45d953e66d34)

if u look at the if conditions each box has a letter 'l','e','t','m','e','i','n','n','o','w'
we can kind of guess that the password is letmeinnow (and it has 10 letters) so lets try that

![image](https://github.com/user-attachments/assets/260da07f-9d5b-4ddc-b185-fe64a7b92e5b)

and we got our flag
