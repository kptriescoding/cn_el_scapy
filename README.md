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
back 
8. Create: Using all the above information provided layers are stacked and packet is created
and the packet info is displayed to the user
9. Send: On clicked the created packet is then sent into the network to reach desired host
10. Generate PDF: This button when clicked generates PDF of 2D graphical visualization
of all the packets sniffed from the network interface .
11. Raw Data: When clicked displays the raw data the packet contains
12. Hex Data: When clicked displays the data the packet contains in hex format

### 2. Packet Sniffing and related options

For sniffing packets through Scapy we need not explicitly send any data but various other
filters can be applied . “sniff()” is the command used to sniff packets using Scapy . The following
are the different options given for the user to enter .Further we have displayed screenshots of this
page in “Chapter 3” with all the below options provided
1. Count: If entered This number and specific count option is selected (another option is
unlimited which sniffs packets as soon as it is received through the network interface) is
used to sniff only given number of packets from the network interfaces .
“sniff(count=10)” is an example of applying this filter
2. Protocol: User can enter the particular protocol from which he needs to sniff packets ,by
default it sniffs from all protocols if not mentioned explicitly. For example “tcp” “udp”
are some of the options
3. Network Interface: By default packets are sniffed from all network interfaces but we
can explicitly select any particular interface detected by scapy .For example “sniff(iface=
“wl0” )” which sniffs from LAN .Loop Back( lo) is another option where in packets sent
are received by the same IP address that of sender
4. Sniff Packets: This option starts sniffing packets according to the filters applied and
starts displaying packet info into a table visible to the user. Each row of the table contains
information related to a single packet sniffed which are source, destination, time at which
the packet was sent, type of IP address (IPV4 /IPV6) , length , the information recieved
5. Stop Sniffing: This option stops sniffing packets from the network
6. Empty Table: Used to empty the table to make UI more readable
7. Generate PDF: This button when clicked generates PDF of 2D graphical visualization
of all the packets sniffed from the network interface .
8. Raw Data: When clicked displays the raw data the packet contains
9. Hex Data: When clicked displays the data the packet contains in hex format

### 3. 3-way Handshake and related option
The first and the only thing required to do a 3-way handshake is the Destination host which the
user wants to have a connection. As discussed earlier there are three packets to be sent called
“SYN”, “SYN-ACK”, “ACK” of which first and last is sent by the user and the destination does
the later. Below are the options provided in this section
1. Destination Host: User is supposed to enter the destination address (DNS address) with
which he wants to establish a connection with.
2. Create: This initializes /starts the connection establishment process using 3-way
handshake
3. SYN: On clicked displays information about syn packet sent to the destination address
4. SYN-ACK: On clicked displays information about syn-ack packet sent by the destination
address to the sender after receiving a connection request which it received through syn
packet
5. ACK: On clicked displays information about ack packet sent to the destination address
after receiving syn-ack packet from the destination IP which will establish a successful
connection after which both can send and receive packets
6. Generate PDF: This button when clicked generates PDF of 2D graphical visualization
of all the packets sniffed from the network interface .
7. Raw Data: When clicked displays the raw data the packet contains
8. Hex Data: When clicked displays the data the packet contains in hex format


