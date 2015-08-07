# Novus BC

This document contains information about installation and execution of the bc sample
for Novus. The rest of this section covers the prerequisite dependencies.

To use bc one should have Python 3.4 or later installed; earlier versions may work, but
 have not been tested and are not explicitly supported. [Click here for Python 3.4 
 installation instructions](https://www.python.org/download/releases/3.4.1/).

For Windows users, powershell or command.exe are sufficient, but we recommend configuring
[GitBash](https://msysgit.github.io/) as the usage example does not cover syntax differences
between UNIX style CLI and Windows Native/Powershell.


#Specification details
 
The goal is to implement a simple version of the Unix utility ‘bc’.  The 
command ‘bc ‘ performs arithmetic on the command prompt.  For this sample the 
functionality will be limited to the four basic arithmetic operators (+,-,*,/) and 
should observe order of operations.  The default ‘bc’ command has a repl but it is not 
necessary for your sample to have this behavior. 
 
Here are sample inputs for your program:
``` 
>bc “1+4”
5
>bc “5/2”
2
>bc “5*4+2”
22
 ```
 
*Note the default rounding behavior.  It is recommended that you sample ‘bc’ to 
confirm any assumptions you make.
 
## Installation

Installation is straight forward. Simply open the CLI utility of choice and run 
the following command. Note that due to the specification the name of the command
'bc' was chosen, and may cause a naming conflict with existing programs.

```
pip3 install bc1
```

On Windows, from GitBash, you can run the following.

```
/c/Python34/Scripts/pip3.exe install bc1
```

## Example Usages

Or to get the repl do the following.

```
LOSX-JPERCENT:bc jpercentpip3 install bc1
LOSX-JPERCENT:bc jpercent$ which bc
/Library/Frameworks/Python.framework/Versions/3.4/bin/bc
LOSX-JPERCENT:bc jpercent$ /Library/Frameworks/Python.framework/Versions/3.4/bin/bc
bc .1
Copyright 2015 Syndetic Logic, LLC
All rights reserved
>5+2
7
>3*5/2+2                                
9
```

To kill the repl type ctr-c or enter erroneous input. Note, only basic testing of the
functionality was completed.

Here is a non-repl example that uses the full path installed on an OSX system.
```
LOSX-JPERCENT:bc jpercent$ /Library/Frameworks/Python.framework/Versions/3.4/bin/bc 3*5/2+2
9
```

For windows users the path to the BC program will be

```
/c/Python34/Scripts/bc
```


