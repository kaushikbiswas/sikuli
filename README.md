# sikuli (\*\*work in progress\*\*)

## Introduction

### What is Sikuli
Automation software that primarily uses image recognition to identify and control UI components
Automates what is visually present in the screen
Uses Python
Built in Java so it is multi platform

## Setup
### Preqrequisites
-	Sikuli uses Python for scripting (Jython)
-	Any scripting skills like JavaScript, Ruby or Python 

### Steps to setup on your machine

-	Verify that JVM is installed in your machine
-	Go to the [sikuli site](http://www.Sikulix.com)
-	Download *sikulixsetup.jar*
-	Run the jar (logically this should be Pack 1)
-	IDE and all relevant packages would be installed

## Basics</br>
### Sikuli interface
-	Sikuli comes with own IDE
-	Projects can be created in the IDE and executed by themselves. After all it automates the screens
-	Its mostly drag and drop



### Matching patterns 
Pattern: Specify a consistent pattern to verify  
String: predefined text to match on the screen
Match: A match from a previous find
Region : A region object
Location: location on the screen like coordinates	

Most commonly used are user defined patterns on the screens


Pattern contains a user defined image and information about the image, like size, similarity and target offset
<place and example>




Conditional Automation
Conditional Looping

<(\*\*work in progress\*\*)>



## Practical Examples
There are 2 examples uploaded for explanation purposes. They include the properties I have provided above:
**calcProj.sikuli** - This is an exmple where the script detects if calculator is open or not. If it is already open, the script clears it and starts adding 1's until the hotkey (*Ctrl+F1*) is pressed. If the calculator application is not open, it opens the applications and continues its operation as mentioned. 
**sendMail.sikuli** - This application opens an excel and extracts MailID, subject and mail body, composes a mail each in outlook and sends them to the individual recepients whose mail IDs are present. 
