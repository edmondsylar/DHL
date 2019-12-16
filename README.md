# DHL | File Upload

### Preinstalled

Before you can run the API  
* make sure you have git installed.  
  for Debian:  
  > sudo apt-get update  
  > sudo apt-get install git  

  for windows:  
  * Download git from official site  
  [download git and or git bash](https://git-scm.com/download/win)  

* Make sure you have python installed  
  for Linux:  
  * python comes preinstalled on the system at least (version 2)  
    but to upgrade python to get the updated version  
    > sudo apt-get update  
    >sudo apt-get upgrade  

  for windows:  
    * You will need to download the latest version of python from the python website  
      [Python download here.. ](https://www.python.org/downloads/)  
      * The page had multiple option and python versions and you can download the one that  best suits you but i would recommend the most recent version.  

* Install virtualenv
  1. For Linux:  
    > sudo apt-get update  
    > sudo apt-get install virtualenv  

  2. For windows:  
    __after installing python and pip__  
     > pip install virtualenv

## Installation  

* clone the project to your local machine  
  > git clone https://github.com/edmondsylar/DHL.git  

* installation  
  1. creata a virtualenv  
    * For Linux:  
      > virtualenv env -p python3  

    * For windows:  
      > virtualenv env -p python3  
      **OR**  
      > python -m virtualenv env p python3  

    __you can use whichever works for you depending on how you installed your virtualenv__  

  2. Activate virtualenv  
    * Linux:  
    > source env/bin/activate  

    * Windows  
    > source env/Scripts/activate  

  3. install requirements file  
    > pip install -r requirements.txt  
