# domainbigdata-python
Pull search results from DomainBigData (no API available)

Adopted from https://github.com/crits/crits_services/blob/3dff56e7111439c4156a8408f178fd484df76feb/domainbigdata_service/domainbigdata.py


### Usage
```python
from domainbigdata import DomainBigData

d = DomainBigData()
email = "dns-admin@google.com"

d.email_information(email, None)
print(d.intelligence)
#print(d.intelligence_list)
```
