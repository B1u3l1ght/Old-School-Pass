# Old-School-Pass
Zero Trust Password created in the Old School fashion way.

This small project relies on couple of GNU/Linux core utils like echo,shuf, cat, tr.

Here we'll try to explain the importance of a strong backbone pattern of a password even many consider every password in order to be strong has to be trully random. After this not so argumented idea people tried to find the perfect source of a trully random generated string like wheather patterns or background cosmic noise, whales underwater sounds and other crazy stuff like that. Here we'll gonna be pragmatic and create a password chassis that will natively give:
1) The biggest amount of arrangements - ensuring your password 'needle' gonna be blended behind big enough haystak to make it unfeasable to break it even by clusters of supercomputers
2) Highest Entropy - elements of the password will never be repeated needlessly thinking you need to make a memorable pass or trying tricky strategies to make a compromise between memorable and strength, no here we are aiming for close to perfection passwords.
3) In order to achive the no. 1 step were gonna need math.

For our close to perfection password we are gonna use good old 94 characters (knowing some websites not allow spaces) and we'll split them inot 4 fileds:
1) Symbols and special characters  ! " # $ % & ' ( ) * + , - ] . / : ; < } = | { > ? @ \ ^ ` ~ _ [         32 symbols
2) Low cap leters a-z  26 chars
3) Captial letters A-Z 26 chars
4) Numbers 0-9, 10 numbers

On short we can represent our 94 search space depth like this 32|26|26|10 (horizontaly) or vertically 

32
26
26
10

Now that we arbitrarily split our 94 chars into 4 fileds we gonna choose a password length good enough to make any quantum computer cry therefor we'll gonna choose a 63 chars length password to be generated out of those 94 total available chars. But we will not use any repetion of chars since we need the best entropy. The reason is a hacker would need all elements you put in your password otherwise his cracking attempt will fail while repeating a character would decrease pass entropy and make hacker life a much easy job since he can mix less elements even that way would give bigger amount of posibilities 63^94 vs only A(94,63) (arrangements of 94 elements taken by 63) which is 94!/31!
So we will sacrifice the bigger haystack in exchange of the better entropy. Even at first this seems to be worse the 63 chars length of the password is long enough to rule out any form of brute force and in the same time in exchange of loosing a bit of haystack numbers we gain more valuable arrangements.

To obtain the best chassis for out pattern we need to know desired pass length in our case 63 and so we have to remove from total 94 chars 31 chars. Having our 4 fields talked previously 32|26|26|10 we have to subtract from each filed approximately the same amount of chars in order to not influence negatively arrangements that can form inside each filed
Therefor for a 94 total chars from each field 32|26|26|10 we must subtract ~ 8 or 7 chars not more not less and we will have for a 63 pass a chasis like 

32|26|26|10
24|18|18| 3
-------------
 8  8  8  7
 
So from the first filed we subtract 8 from second 8 from third 8 and from fort 7. This is just an example this pattern can suffer minor changes but respecting the above rule of thumb where we must subtract an even number from each filed.

To see why this 24|18|18| 3 pass chasis is better than others we must calculate the arrangements  A(32,34)xA(26,18)xA(26,18)xA(10,3) and we will see that the highest number of arrangements without repetition is represented by the above pass chasis or simmilar enough.

The last step but not least after we randomly choose from each field 24|18|18| 3 we must mix de result so our password would not look like first special chars, low caps, cap letter and numbers so we must mix all those 4 fields symbols/az/AZ/09 but in the amount determined at previous step (24|18|18| 3) so we blend our pass into the A(94,63) which gives aprox 1,32×10¹¹²

Due to the best chassis chosen we will have a native superstrong pass impossible to break by anything. Also must be noted that the majority of 100% random based password generators produces lower quality chassis that gives 10/100/1000 or even worse less arrangements. If still not yet convinced generate couple of what we know to be a good password generator at Gibson 'prefect password' generator here https://www.grc.com/passwords.htm and test their chassis here https://www.grc.com/haystack.htm you'll gonna see all chassis prouced by GRC are usually 5x 10x 100x or worse than the chassis proposed by our model here.

So now that we figured out the science we now have to call some great tools to help us achive the best result but in the Old School Fashion.
Tools that helped are: shuf, echo, cat, tr
