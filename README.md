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


   
### Installation - Linux

1. Install java 
```bash
   sudo apt update
   sudo apt install python3
   ```

2. Clone the repo
```git clone https://github.com/kptriescoding/cn_el_scapy
   cd cn_el_scapy
   ```

3. Install the requirements 
```pip i -r requirements.txt
  ```

4. Run the application
```sudo python3 app.py
    
  ```



## Some Sample Commands Usages

### 1. mkdir

<p> mkdir is used to make a new directory<br/><br/>Usage</p>

   ```bash
    mkdir dirname
   ```

### 2. cd

<p> cd is a command can be used to change a directory <br/><br/>Usage</p>

   ```bash
   cd dirname
   ```
### 3. ls

<p> ls command is used to list all files of an directory <br/><br/>Usage</p>

   ```bash
   ls
   ```
<p align="center">or</p>

   ```bash
   ls dirname
   ```

### 4. touch

<p> touch is used to create a regular file <br/><br/>Usage</p>

   ```bash
   touch filename
   ```
### 5. cat

<p> cat is used to display contents of a file <br/><br/>Usage</p>

   ```bash
   cat filename
   ```

### 6. rmdir

<p> rmdir is used to delete a directory <br/><br/>Usage</p>

   ```bash
   rmdir filename
   ```

### 7. rm

<p> rm is used to delete a file <br/><br/>Usage</p>

   ```bash
   rm file
   ```
### 8. lnk

<p> link is used to create shortcuts of a file or directory<br/><br/>Usage</p>

   ```bash
   lnk srcname destname
   ```

### 9. mv

<p> mv is used to move a file from one location to another. If the srcname is the same as destname then it is similar to renaming<br/><br/>Usage</p>

   ```bash
   mv srcname destname
   ```

### 10. grep

<p> grep can be used for pattern matching <br/><br/>Usage</p>

   ```bash
   grep pattern text
   ```

### 11. Traversal through '/', '..', '.'

<p>Multilevel traversal is possible using '/' to specify the path as we go from each outer directory to inner directory. 
The name for the root folder is '/' which can be accessed from any folder. The parent can be accessed using '..' meanwhile
the current folder by '.' .This can be used for any command where path is used
<br/><br/>Some Example Usages </p>
1. Move to root

   ```bash
   cd /
   ```
2. Make a directory in parent directory

```bash
mkdir ../dirname
   ```
2. Make a in a inner directory from root (Note that all the directory except the outer ones must exist)

```bash
mkdir /dir1/dir2/dir3/dirname
   ```
### 12. Piping

<p> Piping can be used here to send the output of one command as a parameter to the next
one <br/><br/>Usage (Here the content of the file is given as the 2nd parameter to the grep command) </p>

   ```bash
   cat filename | grep pattern
   ```
