import zmq
import random
import argparse
import json
import random
import time
import sys


if __name__ == "__main__":

    # parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number", type=int, default=100,
        help="number of documents to send")
    parser.add_argument("-r", "--rate", type=float, default=10,
        help="data send rate in Hz")
    args = parser.parse_args()

    # send messages on this this socket
    context = zmq.Context()
    sender = context.socket(zmq.PUSH)
    sender.bind("tcp://*:5557")

    # pause until loggers have been started up and are ready
    print("press ENTER when loggers are ready")
    rv = input()
    print("sending documents to loggers")

    # load data payload
    with open("payload.json") as fd:
        data = json.load(fd)
    string_data = json.dumps(data)
    print("sending ~{} bytes of data".format(sys.getsizeof(string_data)))

    # send to loggers
    for doc in range(args.number):
        start_time = time.time()
        sender.send_string("{}".format(string_data))
        send_time = time.time() - start_time
        if send_time < (1/args.rate):
            # if we still have time before our interval is up
            time.sleep((1/args.rate) - send_time)
        else:
            print("fell behind while sending document {}".format(doc))

    # clean up
    sender.close()
context.destroy()