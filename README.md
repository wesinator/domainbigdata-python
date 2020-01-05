# domainbigdata-python
Pull search results from DomainBigData (no API available)

Adopted from https://github.com/crits/crits_services/blob/3dff56e7111439c4156a8408f178fd484df76feb/domainbigdata_service/domainbigdata.py

### Installation
```sh
pip install --user domainbigdata
```

### Usage
```python
import domainbigdata
import json

email = "dns-admin@google.com"
email_registrations = domainbigdata.email_lookup(email)
json.dumps(email_registrations.domains)

# domains may not always have full registrant info
domain = "example.com"
domain_reg = domainbigdata.domain_lookup(domain)
json.dumps(domain_reg.registrant_info)
```
