![image](https://github.com/user-attachments/assets/de3aeaf9-af4f-46d4-a322-a84ecc5a5e4d)

ok that doesnt help us
the description says its similar to the last one . so lets try the same steps

![image](https://github.com/user-attachments/assets/55d12f49-1e53-460e-acb4-90425f2ee75d)

we have a similar if conditions in check_flag() funciton

lets add a breakpoint and check whats happening

![image](https://github.com/user-attachments/assets/02648714-53bd-4182-809e-28806f2d4064)

here the rax register points to a string of alphabet 'abc....z'

and 4 is added tot he pointer so it means 'e'

and then 'n'(0D in decimal is 13.14the value in alphabet is n)(we take 14 instead of 13 is because the value of 'a' is 0.for the same reason 4 is mapped to 'e' and not 'd')

so if we convert all the values form hexadecimal to decimal and convert them into alphabet using the string we get

'enter_flag'

so now lets give it the input

![image](https://github.com/user-attachments/assets/a2ccdc56-c466-4129-9aa9-dd74c25fee81)

and thats our flag
