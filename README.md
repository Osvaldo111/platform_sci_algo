# platform_sci_algo

Run the program by executing the following command (according your python version): 

```
 python file.py
```


Note: You should have Python installed in your machine. Also, you can update the txt files respectively (drivers, addresses). 

## What this program is doing?

The top-secret algorithm is:
* If the length of the shipment's destination street name is even, the base suitability score (SS) is the number of vowels in the driver’s name
multiplied by 1.5.
* If the length of the shipment's destination street name is odd, the base SS is the number of consonants in the driver’s name multiplied by 1.
* If the length of the shipment's destination street name shares any common factors (besides 1) with the length of the driver’s name, the SS is
increased by 50% above the base SS.

For example, if provided a driver file with Daniel Davidson on one line and an address file with 44 Fake Dr., San Diego, CA 92122 on
a line, that pairing’s suitability score would be 9.
Write an application in the language of your choice that assigns shipment destinations to drivers in a way that maximizes the total SS over the set
of drivers. Each driver can only have one shipment and each shipment can only be offered to one driver. Your program should run on the
command line and take as input two newline separated files, the first containing the street addresses of the shipment destinations and the second
containing the names of the drivers. The output should be the total SS and a matching between shipment destinations and drivers. You do not
need to worry about malformed input, but you should certainly handle both upper and lower case names.