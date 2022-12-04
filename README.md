# TPOS

## esp32

picocom repl:
```shell
picocom /dev/ttyUSB0 -b115200
```

copy file to board:
```shell
ampy --port /dev/ttyUSB0 put ssd1306.py
```

## esp8266

https://docs.micropython.org/en/latest/esp8266/tutorial/network_basics.html

picocom repl:
```shell
picocom /dev/ttyUSB0 -b115200
```

rshell:
```shell
rshell --buffer-size=30 -p /dev/ttyUSB0 -a
```

## Jupyter Micropython Kernel

https://www.instructables.com/Micropython-on-ESP-Using-Jupyter/

1. install kernel
2. start notebook and use kernel
3. set first line `%serialconnect to --port=/dev/ttyUSB0 --baud=115200`
4. get it!

## adafruit ampy

```text
Usage: ampy [OPTIONS] COMMAND [ARGS]...

  ampy - Adafruit MicroPython Tool

  Ampy is a tool to control MicroPython boards over a serial connection.
  Using ampy you can manipulate files on the board's internal filesystem and
  even run scripts.

Options:
  -p, --port PORT    Name of serial port for connected board.  Can optionally
                     specify with AMPY_PORT environment variable.  [required]
  -b, --baud BAUD    Baud rate for the serial connection (default 115200).
                     Can optionally specify with AMPY_BAUD environment
                     variable.
  -d, --delay DELAY  Delay in seconds before entering RAW MODE (default 0).
                     Can optionally specify with AMPY_DELAY environment
                     variable.
  --version          Show the version and exit.
  --help             Show this message and exit.

Commands:
  get    Retrieve a file from the board.
  ls     List contents of a directory on the board.
  mkdir  Create a directory on the board.
  put    Put a file or folder and its contents on the board.
  reset  Perform soft reset/reboot of the board.
  rm     Remove a file from the board.
  rmdir  Forcefully remove a folder and all its children from the board.
  run    Run a script and print its output.
```

```shell
export AMPY_PORT=/dev/ttyUSB0
ampy ls
```

## networking

https://docs.micropython.org/en/latest/esp8266/tutorial/network_basics.html
https://tttapa.github.io/ESP8266/Chap05%20-%20Network%20Protocols.html

## Possible approach
  * esp8266mod sensors (Sl, Sr, Sc) send POST requests to central  

## IR

### receiver

```shell
G - Ground, R - Red, positive Voltage, Y - Signal
```