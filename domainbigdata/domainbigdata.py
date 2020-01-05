#!/usr/bin/env python3

# Modified from https://github.com/crits/crits_services/blob/3dff56e7111439c4156a8408f178fd484df76feb/domainbigdata_service/domainbigdata.py
#Author: Lionel PRAT - Original author: Roberto Sponchioni - <rsponchioni@yahoo.it> @Ptr32Void
#Modified source code: https://github.com/Ptr32Void/OSTrICa/blob/master/ostrica/Plugins/DomainBigData/__init__.py
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

import requests
from bs4 import BeautifulSoup

class DomainBigDataResult:
    base_url = "https://domainbigdata.com"

    def __init__(self, url='', name='', registrant={}):
        self.url = url
        self.name = name
        self.registrant = registrant

# EmailWhois subresult, with list of domain data (domain reg info)
class DomainBigDataReverseWhois(DomainBigDataResult):
    def __init__(self, url, name, registrant, domains=[]):
        DomainBigDataResult.__init__(self, url, name, registrant)
        self.domains = domains


# request URL, return contents (utf-8)
def request(url):
    print(url)
    r = requests.get(url)
    status = r.status_code
    if status == 200:
        content = r.text.encode('utf8')
        return content
    else:
        print(status)
        return None


def email_lookup(email):
    # query domainbigdata and parse result HTML
    query = '/email/%s' % (email)
    url = "%s%s" % (DomainBigDataResult.base_url, query) # double slash will have different results

    content = request(url)

    domains = extract_domains(content)
    registrant_info = collect_registrant_information(content)

    # registrant email usually not given, add email input
    if registrant_info["registrant_email"] == '':
        registrant_info["registrant_email"] = email

    return DomainBigDataReverseWhois(url, email, registrant_info, domains)


def extract_domains(email_whois_page):
    domains = []

    soup = BeautifulSoup(email_whois_page, 'html.parser')
    domains_table = soup.findAll('table', {'class': 't1'})

    if domains_table:
        site_entries = domains_table[0].tbody.findAll('tr')
        for site_entry in site_entries:
            site_data = {
                    'domain': '',
                    'creation_date': '',
                    'registrar': ''
            }

            site_fields = site_entry.findAll('td')
            for i in range(0, len(site_fields)):
                field = site_fields[i]

                # domain
                if i == 0:
                    domain = field.get_text()
                    site_data["domain"] = domain

                    # creation date
                elif i == 1:
                    creation_date = field.get_text()
                    site_data["creation_date"] = creation_date

                    # registrar
                elif i == 2:
                    registrar = field.get_text()
                    site_data["registrar"] = registrar

            domains.append(site_data)

    return domains


def domain_lookup(domain):
    url = "%s/%s" % (DomainBigDataResult.base_url, domain)
    content = request(url)
    domain_registrant = collect_registrant_information(content)

    return DomainBigDataResult(url, domain, domain_registrant)


def collect_registrant_information(content):
    soup = BeautifulSoup(content, 'html.parser')
    registrant_field = soup.findAll('div', {'id':'MainMaster_divRegistrantIDCard'})

    registrant = {
        "registrant_org": "",
        "registrant_email": "",
        "registrant_name": "",
        "registrant_city": "",
        "registrant_country": "",
        "registrant_phone": "",
    }

    if registrant_field:
        org_soup = registrant_field[0].findAll('tr', {'id':'MainMaster_trRegistrantOrganization'})
        email_soup = registrant_field[0].findAll('tr', {'id':'trRegistrantEmail'})
        name_soup = registrant_field[0].findAll('tr', {'id':'trRegistrantName'})
        city_soup = registrant_field[0].findAll('tr', {'id':'trRegistrantCity'})
        country_soup = registrant_field[0].findAll('tr', {'id':'trRegistrantCountry'})
        phone_soup = registrant_field[0].findAll('tr', {'id':'trRegistrantTel'})

        if org_soup:
            registrant_org = extract_information_from_registrant(org_soup[0])
            registrant['registrant_org'] = registrant_org

        if email_soup:
            registrant_email = extract_information_from_registrant(email_soup[0])
            registrant['registrant_email'] = registrant_email

        if name_soup:
            registrant_name = extract_information_from_registrant(name_soup[0])
            registrant['registrant_name'] = registrant_name

        if city_soup:
            registrant_city = extract_information_from_registrant(city_soup[0])
            registrant['registrant_city'] = registrant_city

        if country_soup:
            registrant_country = extract_information_from_registrant(country_soup[0])
            registrant['registrant_country'] = registrant_country

        if phone_soup:
            registrant_phone = extract_information_from_registrant(phone_soup[0])
            registrant['registrant_phone'] = registrant_phone

    return registrant


def extract_information_from_registrant(soup):
    soup = soup.findAll('td')
    if len(soup) == 3:
        soup_img = soup[1].findAll('img')
        if len(soup_img) == 1:
            return soup[0].contents[0]
        else:
            return soup[1].string
    elif len(soup) == 2:
        return soup[1].string

    return ''
