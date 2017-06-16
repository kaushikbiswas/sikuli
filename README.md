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
-	Independent - Sikuli comes with own IDE. Projects can be created in the IDE and executed by themselves. After all it automates the screens
-	Ease of usage: There are options to drag and drop fill in information. Code changes can be set to minimal for simple problems
- Object oriented:  The classes and methods are extensive and cover most of the common functions

### Matching patterns 
Sikuli matches by various logic, such as: 

**Pattern**: Specify a consistent pattern to verify</br>
**String**: predefined text to match on the screen</br>
**Match**: A match from a previous find</br>
**Region** : A region object</br>
**Location**: location on the screen like coordinates</br>	

*The most commonly used is user defined patterns present on the screens*

Pattern contains a user defined image and information about the image, like size, similarity and target offset. An example *calcProj* is provided with the details. Also it is to be noted that Sikuli automates anything which is on the current screen. Anything in the page below the screen needs to be logically broght into view before automating. 

<place and example to be provided>


Further topics to be enhanced:

Conditional Automation
Conditional Looping

*<\*\*work in progress\*\*>*



## Practical Examples
There are 2 examples uploaded for explanation purposes. They include the properties I have provided above:</br></br>
**calcProj.sikuli** - This is an exmple where the script detects if calculator is open or not. If it is already open, the script clears it and starts adding 1's until the hotkey (*Ctrl+F1*) is pressed. If the calculator application is not open, it opens the applications and continues its operation as mentioned. </br></br>
**sendMail.sikuli** - This application opens an excel and extracts MailID, subject and mail body, composes a mail each in outlook and sends them to the individual recepients whose mail IDs are present. 
