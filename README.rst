CPN
===

CPN is a server-side client for [Charzeh Pull Notification](http://cpn.charzeh.com) system. Using CPN you can send pull notifications to apps and register new devices.

## Instalation

You can install cpn using pip:

`pip install git+https://github.com/amirmd76/cpn.git`

Or you can manually download the source code.


## Usage

```python
from cpn import Client as CPNClient

client = CPNClient("XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX")	# App token

new_device_token = client.obtain_token()

send_notification(new_device_token, "this is just a test notification")
send_json_notification(new_device_token, {"type": "warning", "message": "Let's do it", "name" = "Jon Doe"})
```
