# Cisco DNA Center Healthcheck Device Netconf

*Cisco DNA Center Healthcheck over Netconf-Yang from Console*

This script verifies connectivity between Cisco DNA Center and the Network Device.

## Demo

![Demo](./demo.gif)

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
git clone <todo>
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

## Authors & Maintainers

- Robert Csapo <rcsapo@cisco.com>

## License

This project is licensed to you under the terms of the [Cisco Sample
Code License](./LICENSE).
