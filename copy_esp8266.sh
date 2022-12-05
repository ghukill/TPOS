export AMPY_PORT=/dev/ttyUSB0

echo "copy config.json"
ampy --port $AMPY_PORT put embedded/config.json

# copy sonar lib
echo "copying wifi libs"
ampy --port $AMPY_PORT put embedded/wifi.py

# NOTE: current not using
#echo "copying lib/micropython_ir/ir_rx"
#ampy --port $AMPY_PORT put embedded/lib/micropython_ir/ir_rx
#ampy --port $AMPY_PORT put embedded/lib/micropython_ir/ir_rx/test.py ir_rx/test.py

# copy sonar lib
echo "copying sonar libs"
ampy --port $AMPY_PORT put embedded/lib/hcsr04.py

echo "copying main.py"
ampy --port $AMPY_PORT put embedded/main.py

echo "rebooting"
ampy --port $AMPY_PORT reset