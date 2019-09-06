# domainbigdata-python
Pull search results from DomainBigData (no API available)

Adopted from https://github.com/crits/crits_services/blob/3dff56e7111439c4156a8408f178fd484df76feb/domainbigdata_service/domainbigdata.py


### Usage
```python
from domainbigdata import DomainBigData
import json

d = DomainBigData()
email = "dns-admin@google.com"

d.email_lookup(email)

#print(d.intelligence_list)
data = d.intelligence

json.dumps(data)
```
