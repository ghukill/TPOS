# original micropython board
echo "flashing pyboard"
rshell cp ./embedded/boot.py /flash/boot.py
rshell cp ./embedded/main.py /flash/main.py
rshell cp ./embedded/hcsr04.py /flash/hcsr04.py
echo "finis!"