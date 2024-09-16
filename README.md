Kaprekar Constant

I came across Kaprekar’s Constant (6174) while browsing thru Youtube. The video described what is called as Kaprekar’s Constant which is the number 6174.
This is how it goes. You take any 4 digit number, rearrange the digits to form a largest & smallest number from it. Subtract smaller number from larger number. Then repeat the process. Eventually, after few iterations, you will arrive at number 6174 which then keeps repeating no matter how many times you repeat the steps.
For example, take number 8361.

Step 1 : 8631 & 1368 are the largest & smallest number obtained by rearranging digits.
Step 2 : 8631 – 1368 = 6993
Repeat Step 1 & 2 on 6993.
9963 – 3699 = 6264
6642 – 2466 = 4176
7641 – 1467 = 6174
7641 – 1467 = 6174
…
So for number 8361 we reached to Kaprekar constant in 4th iteration. Except for few exceptions, like repeated digits – 1111,2222,…9999 this hold true for 
all 4 digit numbers. Most of them (99%) reaching to 6174 in 4 iterations.

This got me thinking, if this will hold true for other numbers, like 3 digit, 5 digit, 6 digit numbers. So, I wrote a Python script to cycle thru the integers and 
applying above steps to see if they converge to a constant. 

Following are the observations I made. The python script and relevant log files you can find at Git repository (Upload files · solcrypto65/Kaprekar (github.com)

![image](https://github.com/user-attachments/assets/9173e745-f223-40c7-8bbb-eaf5a51ac008)


