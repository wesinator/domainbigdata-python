# domainbigdata-python
Pull search results from DomainBigData (no API available)

### Usage
```python
from domainbigdata import DomainBigData

d = DomainBigData()
email = "dns-admin@google.com"

d.email_information(email, None)
print(d.intelligence)
#print(d.intelligence_list)
```
