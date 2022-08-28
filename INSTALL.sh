#!/usr/bin/env bash
clear
chmod +x mogroth.py
cp mogroth.py /usr/bin/mogroth
echo "# Installing.."
echo -ne '>>>                       [20%]\r'
sudo pip install requests
sudo pip install getopt
sudo pip install threading
sudo pip install bs4

sleep 2
echo -ne '||||||||                   [40%]\r'
# some task
sleep 2
echo -ne '||||||||||||||             [60%]\r'
# some task
sleep 2
echo -ne '|||||||||||||||||||||||    [80%]\r'
# some task
sleep 2
echo -ne '|||||||||||||||||||||||||||[100%]\r'
echo -ne '\n'
