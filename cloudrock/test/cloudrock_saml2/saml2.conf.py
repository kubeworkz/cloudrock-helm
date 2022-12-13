import datetime
import saml2

# wiki: http://docs.cloudrock.ca/Identityproviders
CLOUDROCK_AUTH_SAML2.update({
    # used for assigning the registration method to the user
    'name': 'saml2',
    # full path to the xmlsec1 binary program
    'xmlsec_binary': '/usr/bin/xmlsec1',
    # required for assertion consumer, single logout services and entity ID
    'base_url': 'https://cloudrock.example.com',
    # set to True to output debugging information
    'debug': True,
    # IdPs metadata XML files stored locally
    'idp_metadata_local': [
        '/etc/cloudrock/saml2/metadata/edugain_metadata.xml',
    ],
    # IdPs metadata XML files stored remotely
    'idp_metadata_remote':
    [
    ],
    # logging
    # empty to disable logging SAML2-related stuff to file
    'log_file': '',
    'log_level': 'DEBUG',
    # Indicates if the entity will sign the logout requests
    'logout_requests_signed': 'true',
    # Indicates if the authentication requests sent should be signed by default
    'authn_requests_signed': 'true',
    # PEM formatted certificate chain file
    'cert_file': '/etc/cloudrock/saml2/credentials/sp.crt',
    # PEM formatted certificate key file -- a private copy of the file inside docker image
    'key_file': '/etc/cloudrock/saml2/credentials/sp.pem',
    'signature_algorithm': 'http://www.w3.org/2001/04/xmldsig-more#rsa-sha256',
    # SAML attributes that are required to identify a user
    'required_attributes': [
        'cn',
        'givenName',
        'surname',
        'mail',
        'schacPersonalUniqueID',
        'eduPersonPrincipalName',
    ],
    # SAML attributes that may be useful to have but not required
    'optional_attributes': [
        'schacHomeOrganization', 'preferredLanguage', 'eduPersonScopedAffiliation'
    ],
    # mapping between SAML attributes and User fields
    'saml_attribute_mapping': {
        'eduPersonPrincipalName': ['username'],
        'schacPersonalUniqueID': ['civil_number'],
        'cn': ['full_name'],
        'givenName': ['first_name'],
        'surname': ['last_name'],
        'mail': ['email'],
        'preferredLanguage': ['preferred_language'],
        'schacHomeOrganization': ['organization'],
        'eduPersonScopedAffiliation': ['_process_saml2_affiliations'],
    },
    # organization responsible for the service
    # you can set multilanguage information here
    'organization': {
        'name': [('Example', 'et'), ('Example', 'en'), ('Example', 'lt')],
        'display_name': [('Example', 'et'), ('Example', 'en'), ('Example', 'lt'),],
        'url': [('https://cloudrock.example.com/', 'et'), ('https://cloudrock.example.com/', 'en'), ('https://cloudrock.example.com/', 'lt')],
    },

    # eduGAIN CoCo settings
    'privacy_statement_url': 'https://cloudrock.example.com/views/policy/privacy-full.html',
    'display_name': 'Example Self-Service',
    'description': 'Self-service for users of Example',

    # mdpi attributes
    'registration_policy': 'http://reg.example.com/main/wp-content/uploads/Federation_Policy_1.3.pdf',
    'registration_authority': 'http://reg.example.com',
    'registration_instant': datetime.datetime(2017, 1, 1).isoformat(),
  'IDENTITY_PROVIDER_LABEL': 'CLOUDROCK',
})

SAML_ATTRIBUTE_MAPPING = CLOUDROCK_AUTH_SAML2['saml_attribute_mapping']

SAML_CONFIG.update({
    'xmlsec_binary': CLOUDROCK_AUTH_SAML2['xmlsec_binary'],
    'entityid': CLOUDROCK_AUTH_SAML2['base_url'] + '/' + '/api-auth/saml2/metadata/',
    'attribute_map_dir': CLOUDROCK_AUTH_SAML2['attribute_map_dir'],
    'name': CLOUDROCK_AUTH_SAML2['display_name'],
    'extensions': {
        'mdrpi': {
            'RegistrationInfo': {
                'registration_policy': {
                    'lang': 'en',
                    'text': CLOUDROCK_AUTH_SAML2['registration_policy'],
                },
                'registrationAuthority': CLOUDROCK_AUTH_SAML2['registration_authority'],
                'registrationInstant': CLOUDROCK_AUTH_SAML2['registration_instant'],
            },
        },
    },
    'contact_person': [
        {
            'email_address': 'mailto:cloudrock@example.com',
            'contact_type': 'technical',
            'given_name': 'Administrator',
        },
    ],
    'service': {
        'sp': {
            # for compatibility with older IdPs. See also https://github.com/IdentityPython/pysaml2/issues/490
            'want_response_signed': False,
            'logout_requests_signed': CLOUDROCK_AUTH_SAML2['logout_requests_signed'],
            'authn_requests_signed': CLOUDROCK_AUTH_SAML2['authn_requests_signed'],
            'endpoints': {
                'assertion_consumer_service': [
                    (CLOUDROCK_AUTH_SAML2['base_url'], '/api-auth/saml2/login/complete/',
                     saml2.BINDING_HTTP_POST),
                ],
                'single_logout_service': [
                    (CLOUDROCK_AUTH_SAML2['base_url'], '/api-auth/saml2/logout/complete/',
                     saml2.BINDING_HTTP_REDIRECT),
                    (CLOUDROCK_AUTH_SAML2['base_url'], '/api-auth/saml2/logout/complete/',
                     saml2.BINDING_HTTP_POST),
                ],
            },
            'allow_unsolicited': True,  # NOTE: This is the cornerstone! Never set to False
            'extensions': {
                'mdui': {
                    'UIInfo': {
                        'display_name': {
                            'lang': 'en',
                            'text': CLOUDROCK_AUTH_SAML2['display_name'],
                        },
                        'description': {
                            'lang': 'en',
                            'text': CLOUDROCK_AUTH_SAML2['description'],
                        },
                        'privacy_statement_url': {
                            'lang': 'en',
                            'text': CLOUDROCK_AUTH_SAML2['privacy_statement_url'],
                        },
                        'logo': {
                            'text': 'https://cloudrock.example.com/login-logo.png',
                        },
                    },
                },
                'mdrpi': {
                    'RegistrationInfo': {
                        'registration_policy': {
                            'lang': 'en',
                            'text': CLOUDROCK_AUTH_SAML2['registration_policy'],
                        },
                        'registrationAuthority': CLOUDROCK_AUTH_SAML2['registration_authority'],
                        'registrationInstant': CLOUDROCK_AUTH_SAML2['registration_instant'],
                    },
                }
            },
            'required_attributes': CLOUDROCK_AUTH_SAML2['required_attributes'],
            'optional_attributes': CLOUDROCK_AUTH_SAML2['optional_attributes'],
        },
    },
    'metadata': [
        {
            'class': 'cloudrock_auth_saml2.utils.DatabaseMetadataLoader',
            'metadata': [('cloudrock_auth_saml2.utils.DatabaseMetadataLoader',)],
        },
    ],
    'organization': CLOUDROCK_AUTH_SAML2['organization'],
    'debug': int(CLOUDROCK_AUTH_SAML2['debug']),
    'key_file': CLOUDROCK_AUTH_SAML2['key_file'],
    'cert_file': CLOUDROCK_AUTH_SAML2['cert_file'],
    # keys are required in order to be able to decrypt encrypted messages from IdPs
    'encryption_keypairs': [{"key_file": CLOUDROCK_AUTH_SAML2['key_file'], "cert_file": CLOUDROCK_AUTH_SAML2['cert_file']}],
})

if CLOUDROCK_AUTH_SAML2['log_file'] != '':
    level = CLOUDROCK_AUTH_SAML2['log_level'].upper()
    LOGGING['handlers']['file-saml2'] = {
        'class': 'logging.handlers.WatchedFileHandler',
        'filename': CLOUDROCK_AUTH_SAML2['log_file'],
        'formatter': 'simple',
        'level': level,
    }

    LOGGING['loggers']['djangosaml2'] = {
        'handlers': ['file-saml2'],
        'propagate': True,
        'level': level,
    }

    LOGGING['loggers']['saml2'] = {
        'handlers': ['file-saml2'],
        'propagate': True,
        'level': level,
    }

SAML_CONFIG['encryption_keypairs'] = [{
    'key_file': CLOUDROCK_AUTH_SAML2['key_file'],
    'cert_file': CLOUDROCK_AUTH_SAML2['cert_file'],
}]

for remote in CLOUDROCK_AUTH_SAML2['idp_metadata_remote']:
    SAML_CONFIG['metadata'].append({
        'class': 'saml2.mdstore.MetaDataExtern',
        'metadata': [(remote['url'], remote['cert'])]
    })