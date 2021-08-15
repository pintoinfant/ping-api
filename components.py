import subprocess
import os
from devices import *
from datetime import datetime

def time():
    update_time = (datetime.now())
    return update_time


hosts = device

status = {
    "updated time" : time() , 
    "device status" : []
}

def pinghost(host):
    cmd = f"ping {host} -c 1"
    result = subprocess.run(cmd,shell=True,capture_output=True,text=True)
    result_text =  (result.stdout)

    if "Request timed out" in result_text:
        return "offline"
    elif "Destination Host Unreachable" in result_text:
        return "offline"
    else:
        return "online"

def update_status():
    status["device status"] = []
    status["updated time"] = time()
    for host in hosts:
        devicestatus = {
            "host address" : host,
            "status" : pinghost(host)
        }
        status["device status"].append(devicestatus)