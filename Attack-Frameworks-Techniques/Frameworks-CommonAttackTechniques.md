## Attack Frameworks and Common Attack Techniques


*Based on Offensive Security's Threat Detection curriculum found at <https://offsec.com>.*

--------


Helpful Resources: 

Cyber Kill Chain
<https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html>


Mitre ATT&CK: <https://attack.mitre.org/> </br>
Mitre D3FEND: <https://d3fend.mitre.org/>


Diamond Model
<https://threatconnect.com/resource/the-diamond-model-intrusion-analysis/>

----------

### IOCs: Indicators of Compromise

Types:



-----------

### Common Attack Techniques

#### <span style="text-decoration: underline">Opportunistic Attacks</span>:

##### Phishing/Credential Stealing: 
Mass messages sent to variety of targets, typically through an email, that includes a malicious link that often impersonates familiar brands, agencies, and institutions.  the goal of the adversary is to trick the targets into clicking these links to trigger the exploitation. Usually, the attacker is looking to steal credentials from their targets. 
    * Smishing: phishing via sms 
    * Vishing:  phishing by phone call

</br>

##### Ransomware
Popular technique. The goal of a ransomware attack is financial gain.   The attacker encrypts the victim's files to make them inaccessible until the attacker receives the ransom demanded in exchange for the decryption key.  The attacker may exfiltrate the data to use the threat of the release of the victim's sensitive information as further leverage. This is called "double extortion".

</br>

##### DoS - Denial of Service

The attacker overwhelms the target resources with the goal of disrupting access to a web service.  This is done by sending a flood of traffic and requests to the target domain usually by exploiting TCP/IP protocol vulns.  This causes the target to consume excessive resources which makes attempts to handle incoming requests impossible.  

##### DDoS - Distributed Denial of Service

The goal is the same as DoS, but the attacker forms a botnet (network of compromised devices, often IoTs) and commonly uses
  TCP SYN and UDP floods as the vector in order to exploit the target. </p>

</br>

##### Automated Network Attacks:
The attacker leverages port scanners (like nmap) as an information gathering tool to look for open/insecure TCP ports on the target. Common ports are 22 (SSH), 80 (HTTP), and 443 (HTTPS). The attacker uses the information to move laterally across the target and opens target up to various kinds of exploits, like brute force attacks.  The goal is to compromise systems and networks.  

-----------
</br>

### *```(This section is a working draft)```* 

#### <span style="text-decoration: underline">Targeted Attacks</span>:

##### Initial Access
Social engineering, often in tandem with spear phishing. 

##### C2 and Persistence
Command and Control. 


##### Lateral Movement
Often targets Active Directory. 

##### Domain Persistence
The attacker gains the ability to impersonate any user without modifying password, minimizing detection. 
