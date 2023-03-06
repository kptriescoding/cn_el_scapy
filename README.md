<!-- PROJECT LOGO -->
<br />


  <h1 align="center">File System Simulator</h1>

  <p align="center">
    A Simple File System Simulator for people wanting to learn some basic linux commands
    <br/>
    By 
    <br />
    <a href="https://github.com/kptriescoding/FileSystemSimulator_USP_DAA_EL/issues">Report Bug</a>
    ·
    <a href="https://github.com/kptriescoding/FileSystemSimulator_USP_DAA_EL/issues">Request Feature</a>
  </p>
  
  <p class="text-center mb-3" align="center">
<a href="https://github.com/kptriescoding/cn_el_scapy/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/kptriescoding/cn_el_scapy?style=for-the-badge"></a>
<a href="https://github.com/kptriescoding/cn_el_scapy/fork"><img alt="GitHub forks" src="https://img.shields.io/github/forks/kptriescoding/cn_el_scapy?style=for-the-badge"></a>
<a href="https://github.com/kptriescoding/cn_el_scapy/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/kptriescoding/cn_el_scapy?style=for-the-badge"></a>
</p>



<!-- ABOUT THE PROJECT -->
## About The Project

Hello, this is a simple packet sniffer made using scapy.

### Built With
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

* [Python](https://www.python.org/)
* [PyQt5](https://pypi.org/project/PyQt5/)
* [Scapy](https://scapy.net/)


<!-- GETTING STARTED -->
## Getting Started


   
### Installation 

1. Install java 
```bash
   sudo apt update
   sudo apt install python3
   ```

2. Clone the repo
```bash
   git clone https://github.com/kptriescoding/cn_el_scapy
   cd cn_el_scapy
   ```

3. Install the requirements 
```bash
   pip i -r requirements.txt
  ```

4. Run the application
```bash
   sudo python3 app.py
    
  ```



## Various Features

### 1. Send and Recieve Packets

This section of “ Smart Sniff ” involves creation of packets , sending it to some host and
finally receiving packets sent .This contains 2 layer where filters can be applied , “ Network
Layer” the later , the “Transport Layer”. The following are the options available in this layout of
the application through which packets headers are constructed finally packets are created and
sent-recieved
1. Protocol: Although various protocols are provided in the scapy framework we have
considered only the IP protocol for simplicity
2. Source: User is prompted to enter the source address(IP address) from which the packet
is to be sent
3. Destination: User is also prompted to enter the destination address(IP address) to which
the packet is to be sent in the network
4. Destination Port: User is supposed to write port number(dport) of destination machine
so that the destination machine can direct packets correctly
5. Timeout: This value is by default set to 10 mS and user can change the value, typically
used to tell source to wait for the acknowledgement of the packet it sent to the destination
IP
6. Stop Sniffing: This option stops sniffing packets from the network .
7. Enter Data: Used to append the information to the packet, which is to be sent to the
destination .Text input option is available ,while sniffing we get the same information
back (discussed in section 2.2)
8. Create: Using all the above information provided layers are stacked and packet is created
and the packet info is displayed to the user
9. Send: On clicked the created packet is then sent into the network to reach desired host
10. Generate PDF: This button when clicked generates PDF of 2D graphical visualization
of all the packets sniffed from the network interface .A screenshot of the same is pasted
in “Chapter 3”
11. Raw Data: When clicked displays the raw data the packet contains
12. Hex Data: When clicked displays the data the packet contains in hex format

### 2. cd

<p> cd is a command can be used to change a directory <br/><br/>Usage</p>

   ```bash
   cd dirname
   ```
### 3. ls


