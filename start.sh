#!/bin/bash
clear
echo "[BrinxBot]: Hello, $USER. I am BrinxBot and I help with ticketing issues!"

if [ $1 == "1" ]
then 
    vartype=itGlue
    echo [BrinxBot]: OK $USER! I will head over to: $vartype
    echo "[BrinxBot]: Running ..."
    python3 itg/gluegrab.py
fi

if [ $1 == "H" ]
then 
    clear
    echo  ----------------- Information -----------------------
    echo  OP1 is to run gluegrab.py...     ./start.sh 1      
    echo  -----------------------------------------------------
    echo  -----------------------------------------------------
    echo Above are the following arguments you can use with start.sh.
    echo After the above, is the correct way to pass an argument to start.sh
fi
echo "[BrinxBot]: EOL...Shutting Down..."