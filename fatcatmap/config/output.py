# -*- coding: utf-8 -*-

'''

    fatcatmap config: output

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


## Template loader settings
_config['apptools.project.output.template_loader'] = {

    # Template Loader Config

    'force': True,              # Force enable template loader even on Dev server
    'debug': False,             # Enable dev logging
    'use_memory_cache': False,  # Use handler in-memory cache for template source
    'use_memcache': False,      # Use Memcache API for template source

}

## Output layer settings
_config['apptools.project.output'] = {

    # Output Configuration

    'debug': False,
    'minify': False,       # whether to minify page output or not
    'optimize': True,     # whether to use the async script loader or not
    'standalone': False,  # whether to render only the current template, or the whole context (ignores "extends")

    'analytics': {  # Analytics Settings
        'enable': False,              # whether to insert analytics code
        'multitrack': True,          # whether to enable support for multiple trackers
        'anonymize': False,          # whether to anonymize IPs before analytics
        'account_id': {
            'fcm': ''   # main yoga analytics tracking
        },
        'sitespeed': {
            'enable': True,           # enable google analytics' site speed tracking
            'sample': 100            # set the sitespeed sample rate
        },
        'webclient': {
            'dev': 'https://ssl.google-analytics.com/u/analytics_debug.js',
            'http': 'https://ssl.google-analytics.com/u/analytics_debug.js',
            'https': 'https://ssl.google-analytics.com/u/analytics_debug.js'
        }
    },

    'appcache': {  # HTML5 appcaching
        'enable': False,                       # whether to enable
        'manifest': 'scaffolding-v1.appcache'  # manifest to link to
    },

    'assets': {  # Asset API
        'minified': False,       # whether to switch to minified assets or not
        'serving_mode': 'local',  # 'local' or 'cdn' (CDN prefixes all assets with an absolute URL)
        'cdn_prefix': ['']
        # ^^ CDN prefix/prefixes - a string is used globally, a list of hostnames is selected from randomly for each
    },

    'headers': {  # Default Headers (only supported headers are shown)
        'Cache-Control': 'no-cache,no-store',  # default to not caching dynamic content
        'X-Powered-By': 'Apptools/v1',
        'XAF-Origin': 'AppHosting/fatcatmap/1.0',

        ## /*****/ CORS /*****/ ##
        'Access-Control-Allow-Origin': None,
        'Access-Control-Allow-Methods': 'GET, POST',
        'Access-Control-Allow-Headers': ','.join([
            'Content-Type', 'Content-Length', 'XAF-Session', 'XAF-Token', 'XAF-Channel',
            'XAF-Socket', 'X-ServiceTransport', 'X-ServiceClient']),
        'Access-Control-Expose-Headers': ','.join([
            'Content-Type', 'Content-Length', 'XAF-Session', 'XAF-Token', 'XAF-Channel',
            'XAF-Socket', 'X-ServiceTransport', 'X-ServiceClient'])
    }

}

## Meta tag information
_config['apptools.output.meta'] = {

    'icon': 'https://alpha.fatcatmap.com/favicon.ico',
    'logo': 'https://alpha.fatcatmap.com/favicon.png',
    'author': 'momentum labs',
    'publisher': 'momentum labs',
    'copyright': 'momentum labs (c) 2013',
    'robots': 'noindex,nofollow',  # 'index,follow',
    'revisit': '7 days',

    'description': 'fatcatmap staging.',

    'application-name': 'fatcatmap',
    'viewport': 'width=device-width,initial-scale=1,user-scalable=yes,height=device-height',
    'revisit-after': '7 days',

    'keywords': [
        'transparency',
        'politics',
        'open source',
        'open data',
        'wall street'
    ],

    'opengraph': {

        'title': '^.^ fatcatmap alpha: welcome!',
        'type': 'website',
        'determiner': 'a',
        'locale': 'en_US',
        'url': 'https://alpha.fatcatmap.com',
        'site_name': 'fatcatmap',
        'description': 'staging: coming soon',
        'image': '',

        'location': {
            'enable': False,

            'latitude': '',
            'longitude': '',
            'address': '1168 Folsom Street',
            'locality': 'San Francisco',
            'region': 'California',
            'zipcode': '94103',
            'country': 'United States of America',
            'email': 'fcm@momentum.io',
            'phone': ''
        },

        'facebook': {
            'app_id': '393123227378006',  # @TODO(sgammon): add fb app id
            'admins': ['642005650']
        }

    },

    'apple': {

        'touch_icon': 'https://alpha.fatcatmap.com/favicon.png',
        'precomposed': '',
        'startup_icon': '',
        'status_bar_style': 'translucent-black',
        'app_capable': 'yes'

    },

    'google': {
        'site_verification': ''
    }

}
