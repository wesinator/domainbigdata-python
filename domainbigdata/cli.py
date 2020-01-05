#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""domainbigdata"""

import click
import domainbigdata
import json

from .__init__ import __version__ as VERSION


@click.command()
@click.option('--version', is_flag=True, help='Print the version of the package')
@click.option('--email', help='Lookup reverse WHOIS on an email address')
@click.option('--domain', help='Look up info (WHOIS registrant) on a domain')
def main(version, email, domain):
    """Command-line interface for domainbigdata"""

    out = ""

    if version:
        print("domainbigdata version: {}".format(VERSION))
    elif email:
        data = domainbigdata.email_lookup(email)
        out = json.dumps(data.__dict__, indent=4)
    elif domain:
        data = domainbigdata.domain_lookup(domain)
        out = json.dumps(data.__dict__, indent=4)
    print(out)

if __name__ == "__main__":
    main()
