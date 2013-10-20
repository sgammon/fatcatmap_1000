#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

    fcm: entrypoint

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


# stdlib
import sys

sys.path.insert(0, 'app')
sys.path.insert(0, 'app/lib')

## apptools!
from apptools import dispatch
from apptools.rpc import mappers
from apptools.rpc import dispatch as rpc

## stdlib wsgi server
from wsgiref.simple_server import make_server

## fcm! :)
from fatcatmap.services import data, graph, media


def run(args):

    '''  '''

    try:
      if len(sys.argv) > 1 and sys.argv[1] == 'services':
        app, port, label = rpc.initialize(), 8081, 'services'
      else:
        app, port, label = dispatch.gateway, 8080, 'app'

      httpd = make_server('', port, app)

      print "Serving fcm %s on port %s..." % (label, port)
      httpd.serve_forever()
      return 0
    except Exception as e:
      print "Encountered exception: %s" % e
      return 1


if __name__ == '__main__': sys.exit(run(sys.argv))
