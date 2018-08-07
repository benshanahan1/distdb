# DistDB

Distributed database example using ZeroMQ's PUSH/PULL pipelining pattern.

The logger instances each have a connection to the MongoDB database (and can concurrently write into it). The ventilator is a process that outputs messages via PUSH (over TCP). This fair-queues the messages among the logger clients that PULL the messages and then process them (concurrently write the received JSON structures into the MongoDB database).


## Install

```shell
pip install -r requirements.txt
```

Then install MongoDB community server on your machine (https://www.mongodb.com/download-center#community). On Ubuntu 16.04, you can install MongoDB with the following commands:

```shell
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.6 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.6.list
sudo apt -y update
sudo apt -y install mongodb-org
sudo service mongod start
```

For a nice MongoDB GUI tool on Linux, check out Robo3T (https://robomongo.org/download). This is not required.


## Usage

1. Run a bunch of instances of the logger: `./logger`
2. Run the ventilator and then press enter: `./ventilator`

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