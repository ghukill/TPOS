export AMPY_PORT=/dev/ttyUSB0

echo "copying main.py"
ampy --port $AMPY_PORT put embedded/main.py

echo "copying lib/micropython_ir/ir_rx"
ampy --port $AMPY_PORT put lib/micropython_ir/ir_rx

echo "rebooting"
ampy --port $AMPY_PORT reset