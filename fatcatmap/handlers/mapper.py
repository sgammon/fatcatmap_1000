# -*- coding: utf-8 -*-

'''

    fatcatmap handlers: mapper

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


# apptools
from apptools.util import decorators

# handlers
from fatcatmap import handlers, routing


@routing.rule('/', name='landing')
@decorators.config(debug=True, path='fatcatmap.handlers.mapper.Landing')
class Landing(handlers.WebHandler):

    ''' fatcatmap landing handler, serves the
        mapper frame. '''

    def get(self):

        ''' HTTP GET '''

        return self.render('mapper.html')
