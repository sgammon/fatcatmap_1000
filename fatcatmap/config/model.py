# -*- coding: utf-8 -*-

'''

    fatcatmap config: model

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


# Redis Adapter
_config['apptools.model.adapters.redis.Redis'] = {

    'debug': True,  # debug messages

    'servers': {

        'default': 'local',

        # Redis Instances
        'local': {'unix_socket_path': '/tmp/redis.sock'}

    }

}

# Memcache Adapter
_config['apptools.model.adapters.memcache.Memcache'] = {

    'debug': True,  # debug messages

    'servers': {
        'local': {'host': '127.0.0.1', 'port': 11211, 'unix': '/ns/runtime/sock/memcache.sock'}
    }

}

