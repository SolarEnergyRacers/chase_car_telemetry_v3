import time

from influxdb_client import InfluxDBClient, Point, WritePrecision
import requests
import logging as lg

from datainput import DataInput, CANFrame
from datapoint import DataPoint
import dataclasses

class DataHandler:
    def __init__(self, opt: dict):
        self.opt = opt

        try:
            self.client = InfluxDBClient(url="http://"+opt["influx"]["host"]+":"+str(opt["influx"]["port"]),
                                         token=opt["influx"]["token"],
                                         org=opt["influx"]["org"])
            self.write_api = self.client.write_api()
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
        for dp in datapoints:
            lg.debug(dp.__dict__)
            self.write_api.write(bucket=self.opt["influx"]["bucket"], org=self.opt["influx"]["org"], record = dp.__dict__)
