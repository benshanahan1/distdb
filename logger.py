import zmq
import time
import json
import pymongo
import datetime


class Database():
    def __init__(self, database):
        try:
            self.client = pymongo.MongoClient(serverSelectionTimeoutMS=3000)
            self.client.server_info()  # force connection
        except pymongo.errors.ServerSelectionTimeoutError:
            print("MongoDB database could not be found. Please make sure that it is running.")
            exit(1)
        self.db = self.client[database]  # get MongoDB Database object


if __name__ == "__main__":
    # connect to MongoDB database
    db = Database("LoggerTestDB")

    # socket to receive messages on
    context = zmq.Context()
    receiver = context.socket(zmq.PULL)
    receiver.connect("tcp://localhost:5557")

    # process tasks forever
    while True:
        try:
            msg = receiver.recv()
        except Exception as ex:
            print("uh oh: {}".format(ex))
            exit(1)
        data = json.loads(msg.decode())
        db.db.mycoll.insert_one(data)
        print("{}: added document ({} bytes)".format(datetime.datetime.now(), len(msg)))

    # clean up
    receiver.close()
context.destroy()