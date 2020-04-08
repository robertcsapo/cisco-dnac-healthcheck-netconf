# Cisco DNA Center Healthcheck Device Netconf

*Cisco DNA Center Healthcheck over Netconf-Yang from Console*

This script verifies connectivity between Cisco DNA Center and the Network Device.
 
If Discovery fails on Netconf-yang (on Cisco DNA Center UI) for Network Device, then this script could verify that netconf-yang (port 830) is reachable from the maglev console (Cisco DNA Center).
If it's not reachable, then there will be error logs with details from the ncclient module in python (timeout, credentials, port, etc.)
 
This script is used as an advanced troubleshooting tool, for the experienced DNA Center administrator.

## Demo

![Demo](./demo.gif)

## YANG model used in this script
```
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <hostname>
  </hostname>
  <version>
  </version>
</native>
```

## Requirements

* Cisco DNA Center Console access (_ssh maglev@<dnac-ip-address> -p 2222_)
* Internet Connectivity on DNA Center (Cloud Enabled)
  - DNA Center downloads this container image from Public Docker Registry (docker.io)



## Usage

Login to Cisco DNA-C
* ```ssh maglev@<dnac-ip-address> -p 2222```

Run script
* ```docker run -it --rm robertcsapo/cisco-dnac-healthcheck-netconf && docker rmi robertcsapo/cisco-dnac-healthcheck-netconf```

Enter Cisco Device hostname (then hit ENTER)
* ```host: device.example.tld```
* ```username: demo```
* ```password: Netconf2020```

### Automation

Run script with host flag
* ```docker run -it --rm robertcsapo/cisco-dnac-healthcheck-netconf -host device.example.tld -username demo -password Netconf2020 && docker rmi robertcsapo/cisco-dnac-healthcheck-netconf```

## Installation

If you need to manually build the script on the host.   
```
git clone https://github.com/robertcsapo/cisco-dnac-healthcheck-netconf
```

### Build
* ```cd cisco-dnac-healthcheck-netconf```
* ```docker build -t robertcsapo/cisco-dnac-healthcheck-netconf .```

## Technologies & Frameworks Used

**Cisco Products & Services:**

- Cisco DNA Center
- Cisco IOS-XE

**Tools & Frameworks:**

- Python 3
- ncclient

## Authors & Maintainers

- Robert Csapo <rcsapo@cisco.com>

## License

This project is licensed to you under the terms of the [Cisco Sample
Code License](./LICENSE).
