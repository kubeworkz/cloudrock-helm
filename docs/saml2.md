# SAML2 configuration

To configure SAML2 for Cloudrock:

1. Enable SAML2 support in `values.yaml`:
    add `SAML2` string into `cloudrock.authMethods` list
1. Set source directory in `cloudrock.saml2.dir`
1. Place necessary files in the directory
    with the following manner (`.` is the source directory root):
    - `sp.crt` -> `./`
    - `sp.pem` -> `./`
    - `saml2.conf.py` -> `./`
