import time

from influxdb import InfluxDBClient
import requests
import logging as lg

from datainput import DataInput, CANFrame
from datapoint import DataPoint
import dataclasses

class DataHandler:
    def __init__(self, opt: dict):
        self.opt = opt

        try:
            self.client = InfluxDBClient(host=opt["influx"]["host"], port=opt["influx"]["port"])
            dbs = self.client.get_list_database()

            if not {'name' : self.opt["influx"]["db_name"]} in dbs:
                self.client.create_database(self.opt["influx"]["db_name"])

            self.client.switch_database(self.opt["influx"]["db_name"])
            self.available = True

        except (requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout, ConnectionRefusedError) as err:
            self.available = False
            lg.error(err)
            lg.error("Connection to Influx DB failed")
            lg.error("host=" + opt["influx"]["host"])
            lg.error("port=" + str(opt["influx"]["port"]))

    def handle_new_input(self, input_val):
        di = CANFrame(self.opt, input_val)
        self.uploadDataInput(di)

    def uploadDataInput(self, di: DataInput):
        lg.debug("uploading Datapoints")
        self.uploadDatapoints(di.asDatapoints())

    def uploadDatapoints(self, datapoints: list[DataPoint]):
        self.client.write_points([dp.__dict__ for dp in datapoints], time_precision='s')