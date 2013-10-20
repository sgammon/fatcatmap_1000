# -*- coding: utf-8 -*-

'''

    fatcatmap config: layer9

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


## AppFactory
_config['layer9.appfactory'] = {

    'enabled': True,
    'logging': False,

    'headers': {
        'full_prefix': 'X-AppFactory',
        'compact_prefix': 'XAF',
        'use_compact': True
    }

}

## Upstream layer
_config['layer9.appfactory.upstream'] = {

    'debug': False,
    'enabled': True,

    'preloading': {
        'gather_assets': True,
        'enable_spdy_push': False,
        'enable_link_fallback': False
    },

    'spdy': {

        'push': {

            'assets': {
                'force_priority': False,
                'default_priority': 7
            }

        }

    }

}

## Frontline + Controller
_config['layer9.appfactory.frontline'] = {'debug': False, 'enabled': True}
_config['layer9.appfactory.controller'] = {'debug': False, 'enabled': False}
