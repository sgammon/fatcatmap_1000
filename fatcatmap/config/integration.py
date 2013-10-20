# -*- coding: utf-8 -*-

'''

    fatcatmap config: integration

    :author: Sam Gammon <sam@momentum.io>
    :copyright: (c) momentum labs, 2013
    :license: The inspection, use, distribution, modification or implementation
              of this source code is governed by a private license - all rights
              are reserved by the Authors (collectively, "momentum labs, ltd")
              and held under relevant California and US Federal Copyright laws.
              For full details, see ``LICENSE.md`` at the root of this project.
              Continued inspection of this source code demands agreement with
              the included license and explicitly means acceptance to these terms.

'''


## Globals
_config = {}


## Webapp2: Core
_config['webapp2'] = {
    'apps_installed': [
        "fatcatmap"
    ]
}

## Webapp2: Jinja
_config['webapp2_extras.jinja2'] = {

    'template_path': 'fatcatmap/templates/source',  # Root directory for template storage
    'compiled_path': 'fatcatmap.templates.compiled',  # Compiled templates directory
    'force_compiled': False,  # Force Jinja to use compiled templates, even on the Dev server

    'environment_args': {  # Jinja constructor arguments
        'optimized': True,   # enable jinja2's builtin optimizer (recommended)
        'autoescape': True,  # Global Autoescape. BE CAREFUL WITH THIS.
        'trim_blocks': False,  # Trim trailing \n's from blocks.
        'auto_reload': True,  # Auto-reload templates every time.
        'extensions': ['jinja2.ext.autoescape', 'jinja2.ext.with_', 'jinja2.ext.loopcontrols'],
    }

}

## Webapp2: Sessions
_config['webapp2_extras.sessions'] = {

    'secret_key': 'cjvnkmcpMPOM@(K_)(K_)@-81-0(_)(*@Y*(H*hoiuhnobvuehf8239h80380H**)!@(*J@)(jv8109812',
    'default_backend': 'securecookie',
    'cookie_name': 'fcm',
    'session_ttl': 172000000,
    'session_max_age': None,
    'cookie_args': {
        'name': 'fcm',
        'max_age': 172000000,
        #'domain':      '*',
        'path': '/'
        #'secure':      False,
        #'httponly':    False
    },
    'require_valid': True

}

## Google APIs
_config['google.apis'] = {
    
    'client_id': '399170674212-jkqs588siuji4ffkg7rdikje24hfb6fb.apps.googleusercontent.com',
    #'client_secret': private.oauth2_client_secret,
    'user_agent': 'Catnip/1.0',

    'scopes': [  # base scopes to request access to

        'https://www.googleapis.com/auth/drive.file',
        'https://www.googleapis.com/auth/freebase',
        'https://www.googleapis.com/auth/plus.me',
        'https://www.googleapis.com/auth/userinfo.profile'

    ]

}
