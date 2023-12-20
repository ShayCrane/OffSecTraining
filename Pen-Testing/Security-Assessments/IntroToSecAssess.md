## Introduction to Security Assessments

*The following are personal notes taken while completing the Pen-Testing curriculum found at https://portal.offsec.com.*

-------
## Resources


### Risk
definition </br>
What you are trying to prevent from happening.


### Threat
definition here </br>
WHO would do it.


### Vulnerability
a flaw that, when exploited, will compromise the confidentiality, integrity, or availability of a given system. </br>
The CONDITIONS that allow for the attack.

### Exploit
software is used to take advantage of a vulnerability.

</br></br>

-------

### Anti-Exploit Tools: 
- *[Data Execution Prevention (DEP)](https://en.wikipedia.org/wiki/Executable_space_protection#Windows)*</br>
- *[Address Space Layout Randomization (ASLR)](https://en.wikipedia.org/wiki/Address_space_layout_randomization).*

</br>

-------
</br>

## The CIA Triad
#### *Categories of compromise.*
</br>

### Confidentiality 
Can actors who should not have access to the system or information access the system or information?
</br>

### Integrity 

Can the data or the system be modified in some way that is not intended?
</br>

### Availability 

Are the data or the system accessible when and how it is intended to be?
</br>

--------
</br>

***Attacks will often fall under more than one category.*** </br></br>
***For example, an SQL injection vulnerability puts all three at risk of exploitation:***

- First the attacker obtains full shell access to the host running the target web app

- Using the full shell access, the attacker is able to extract, read (**Confidentiality**), and alter (**Integrity**) all data contained in the web app. With this access and data, attackers can destroy the web app (**Availability**).
  
</br></br>

---------


## Using Kali Linux in an Assessment

#### *Your assessment work must be repeatable and fully documented.  The integrity of your report will be compromised by using anything other than a brand new, clean, and working installation.*

#### *Should you re-use an installation for a new assessment, one or more of the many granular changes you made during a previous assessment may still be in effect.*
---------


### Best Practices

- Prepare as much in advance and under the assumption that internet access will not be easily accessible or available

- Use an [encrypted installation](https://portal.offsec.com/courses/pen-103/books-and-videos/modal/modules/installing-kali-linux/step-by-step-installation-on-a-hard-drive/installation-on-a-fully-encrypted-file-system)

- [Nuke the decryption key](https://portal.offsec.com/courses/pen-103/books-and-videos/modal/modules/advanced-usage/adding-persistence-to-the-live-iso-with-a-usb-key/the-persistence-feature:-explanations) (after sending encrypted copy of key to co-worker in the office)

- Double-check list of installed packages based on what will be needed for the assessment ahead
    - kali-tools-wireless metapackage for a wireless security assessment
    - kali-tools-web metapackage for web app assessment
    - kali-tools-forensic metapackage in forensics mode doesn't automatically mount disks or use a swap partition. this is a tool for you to preserve the integrity of the assessed system.


- [Review your network settings](https://portal.offsec.com/courses/pen-103/books-and-videos/modal/modules/configuring-kali-linux#sect.configuring-the-network); especially [DHCP and listening services](https://portal.offsec.com/courses/pen-103/books-and-videos/modal/modules/securing-and-monitoring-kali-linux/securing-network-services/securing-network-services) on your IP address.

</br>

### *See [Building Custom Kali Live ISO Images](https://github.com/ShayCrane/OffSecTraining/tree/main/Pen-Testing/Security-Assessments/osInstallationOnHardDrive.md)* and *[Unattended Installations](https://github.com/ShayCrane/OffSecTraining/tree/main/Pen-Testing/Security-Assessments/osInstallationOnHardDrive.md) for more information on how to configure a pre-customized version of the OS for automated installation.*

</br></br>
------------

## Types of Assessments

### Vulnerability Assessments


- When performing a vulnerability assessment, the objective is to create a simple inventory of discovered vulnerabilities within the target environment, while staying within the scope of the client's target network and objectives.
</br>

- All vulnerabilities must be treated as exploitable, even when no known exploit exists.
</br></br>

### **Vulnerability Types**
----------

*[OffSec](https://portal.offsec.com) provides the following list of the most common vulnerability types:*
</br>

#### File Inclusion (in web applications)
- Allows you to include the contents of a local or remote file into the computation of a program. For example, a web application may have a "Message of the day" function that reads the contents of a file and includes it in the web page to display it to the user. 

- When this type of feature is programmed incorrectly, it can allow an attacker to modify their web request to force the site to include the contents of a file of their choosing.
</br></br>

#### SQL Injection
- An attack where the input validation routines for the program are bypassed, allowing an attacker to provide SQL commands for the targeted program to execute. This is a form of command execution that can lead to potential security issues.
</br></br>

#### Buffer Overflow
- A vulnerability that bypasses input validation routines to write data into a buffer's adjacent memory. In some cases, that adjacent memory location may be critical to the operation of the targeted program and control of code execution can be obtained through careful manipulation of the overwritten memory data.
</br></br>

    
#### Race Conditions
- A vulnerability that takes advantage of timing dependencies in a program. In some cases, the workflow of a program depends on a specific sequence of events to occur. If you can alter this sequence of events, that may lead to a vulnerability.

</br>

--------

