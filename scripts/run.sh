#!/bin/bash
echo $1
sudo python3 country_code.py $1
echo "Tor Service Restarting"
sudo service tor restart
echo "Tor Service Restarted"
echo "Flush toriptables"
sudo python toriptables2.py -f
python toriptables2.py -f
echo "Creating Secure Tor Connection"
sudo python toriptables2.py -l

