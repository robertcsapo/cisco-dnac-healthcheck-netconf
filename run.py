"""cisco-dnac-healthcheck-netconf  Console Script.

Copyright (c) 2020 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""

__author__ = "Robert Csapo"
__email__ = "rcsapo@cisco.com"
__version__ = "1.0"
__copyright__ = "Copyright (c) 2020 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"

from ncclient import manager
from ncclient.transport import AuthenticationError, SessionCloseError
import xmltodict
import logging
import argparse
import sys


def healthcheck(config):
    result = {}
    try:
        with manager.connect(
                            host=config["host"],
                            port=830,
                            username=config["username"],
                            password=config["password"],
                            hostkey_verify=False
                            ) as m:
            device = """
                <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                    <hostname>
                    </hostname>
                    <version>
                    </version>
                </native>
                    """

            data = m.get(("subtree", device))
    except AuthenticationError as e:
        logging.error("ncclient: {}".format(e))
        result["success"] = False
        return result
    except SessionCloseError as e:
        logging.error("ncclient: {}".format(e))
        result["success"] = False
        return result
    except Exception as e:
        logging.error("ncclient: {}".format(e))
        result["success"] = False
        return result

    data = str(data)
    parse = xmltodict.parse(data.encode())
    result["hostname"] = parse["rpc-reply"]["data"]["native"]["hostname"]
    result["version"] = parse["rpc-reply"]["data"]["native"]["version"]
    result["success"] = True
    return result


if __name__ == "__main__":
    config = {}
    if len(sys.argv) == 1:
        print("Cisco DNA Center Healthcheck Netconf Prompt\n")
        config["host"] = input("host: ")
        config["username"] = input("username: ")
        config["password"] = input("password: ")
    else:
        print("args")
        parser = argparse.ArgumentParser(
            description="Cisco DNA Center Healthcheck Netconf",
            formatter_class=argparse.ArgumentDefaultsHelpFormatter
            )
        parser.add_argument("-host", type=str, required=True,
                            help="Host (device)")
        parser.add_argument("-username", type=str, required=True,
                            help="Username")
        parser.add_argument("-password", type=str, required=True,
                            help="Password")
        args = parser.parse_args()
        config["host"] = args.host
        config["username"] = args.username
        config["password"] = args.password

    logging.basicConfig(
            format='%(asctime)s %(levelname)-8s %(message)s',
            level=logging.INFO,
            datefmt='%Y-%m-%d %H:%M:%S')
    result = healthcheck(config)
    if result["success"] is True:
        logging.info("SUCCESS: Hostname: {} Version: {}".format(
                    result["hostname"],
                    result["version"]
                    ))
