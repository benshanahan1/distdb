# DistDB

Distributed database example using ZeroMQ's PUSH/PULL pipelining pattern.


## Install

```shell
pip install -r requirements.txt
```


## Usage

1. Install MongoDB community server on your machine (https://www.mongodb.com/download-center#community)
2. Install requirements: `sudo pip install -r requirements.txt`
3. Open a bunch of instances of the logger: `./logger`
4. Open the ventilator and then press enter: `./ventilator`

To change the behavior of the ventilator process, run `./ventilator --help`:

```
$ ./ventilator.py --help
usage: ventilator.py [-h] [-n NUMBER] [-r RATE]

optional arguments:
  -h, --help            show this help message and exit
  -n NUMBER, --number NUMBER
                        number of documents to send
  -r RATE, --rate RATE  data send rate in Hz
```

For a nice MongoDB GUI tool on Linux, check out Robo3T (https://robomongo.org/download).


## What it does
The logger instances each have a connection to the MongoDB database (and can concurrently write into it). The ventilator is a process that outputs messages via PUSH (over TCP). This fair-queues the messages among the logger clients that PULL the messages and then process them (concurrently write the received JSON structures into the MongoDB database).