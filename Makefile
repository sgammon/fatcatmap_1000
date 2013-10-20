
#
#    fcm: makefile
#
#    :author: Sam Gammon <sam@momentum.io>
#    :copyright: (c) momentum labs, 2013
#    :license: The inspection, use, distribution, modification or implementation
#              of this source code is governed by a private license - all rights
#              are reserved by the Authors (collectively, "momentum labs, ltd")
#              and held under relevant California and US Federal Copyright laws.
#              For full details, see ``LICENSE.md`` at the root of this project.
#              Continued inspection of this source code demands agreement with
#              the included license and explicitly means acceptance to these terms.
#

all: build

build: develop
	@echo "Building SASS..."
	@bin/compass compile --force --output-style=compressed

	@echo "=== Build complete. ==="

package: develop
	@echo "Making buildroot..."
	@mkdir -p dist/

	@echo "Building source package..."
	@bin/python setup.py sdist

	@echo "Building egg..."
	@bin/python setup.py bdist_egg

	@echo "=== fatcatmap distribution built. ==="

develop: .develop
	@echo "Updating source dependencies..."
	@git submodule update --init

	@echo "Ready to develop for fcm! ^.^"

test:
	@pip install nose
	@echo "Running testsuite..."
	@nosetests fcm_tests --no-byte-compile

coverage:
	@pip install nose
	@echo "Running testsuite (with coverage)..."
	@nosetests fcm_tests --with-coverage \
						 --cover-package=fatcatmap \
						 --cover-html-dir=.develop/coverage_html \
						 --cover-xml-file=.develop/coverage.xml \
						 --no-byte-compile;

deploy:
	@echo "Deployment is not currently supported from dev. Check back later."

clean:
	@echo "Cleaning object files..."
	@find . -name "*.pyc" -exec rm -f {} \;
	@find . -name "*.pyo" -exec rm -f {} \;

	@echo "Cleaning SASS cache..."
	@rm -fr .sass-cache

distclean: clean
	@echo "Cleaning development state..."
	@rm -fr .develop

	@echo "Cleaning gemroot..."
	@rm -fr .Gems

	@echo "Cleaning virtualenv..."
	@rm -fr .Python bin/ include/ lib/ config.rb .env .develop

forceclean: distclean
	@echo "Resetting codebase..."
	@git reset --hard

	@echo "Clearing libraries..."
	@rm -fr assets/js/source/apptools fatcatmap/lib/apptools fatcatmap/lib/appfactory

	@echo "Cleaning untracked files..."
	@git clean -df

### === dirs === ###
bin: .env
lib: .env

### === defs === ###
.develop: bin lib config.rb .env
	@echo "Installing brew dependencies..."
	@brew install libevent

	@echo "Installing development dependencies..."
	@bin/pip install -r ./requirements.txt

	@echo "Creating development sandbox..."
	@mkdir .develop
	@chmod -R 777 .develop

.env:
	@echo "Initializing virtualenv..."
	@pip install virtualenv
	@virtualenv . --prompt=" (^.^) "

	@echo "Symlinking toolchain..."
	@ln -s $(PWD)/scripts/fcm $(PWD)/bin/fcm
	@ln -s $(PWD)/scripts/fatcatmap $(PWD)/bin/fatcatmap
	@chmod +x $(PWD)/scripts/fcm $(PWD)/scripts/fatcatmap
	@echo "$(PWD)/fatcatmap/lib" > lib/python2.7/site-packages/fatcatmap-lib.pth
	@echo "$(PWD)/fatcatmap" > lib/python2.7/site-packages/fatcatmap.pth
	@echo "$(PWD)/.." > lib/python2.7/site-packages/fcm.pth

	@echo "Overriding standard Google paths..."
	@echo "" > lib/python2.7/site-packages/protobuf-2.5.0-py2.7-nspkg.pth
	@rm -fr lib/python2.7/site-packages/webapp2_extras

	@touch .env
	@echo "Virtualenv is ready."

config.rb:
	@echo "Installing compass..."
	@gem install compass --install-dir ./.Gems

	@echo "Configuring compass..."
	@compass init -x sass --prepare --environment development --relative-assets \
		--sass-dir=$(PWD)/assets/style/source \
		--css-dir=$(PWD)/assets/style/static/compiled \
		--images-dir=$(PWD)/assets/img/static \
		--javascripts-dir=$(PWD)/assets/js/static \
		--fonts-dir=$(PWD)/assets/ext/static/fonts;

	@echo "Symlinking Compass binaries..."
	@ln -s $(PWD)/.Gems/bin/compass $(PWD)/bin/compass
	@ln -s $(PWD)/.Gems/bin/sass $(PWD)/bin/sass
	@ln -s $(PWD)/.Gems/bin/scss $(PWD)/bin/scss
	@ln -s $(PWD)/.Gems/bin/sass-convert $(PWD)/bin/sass-convert

	@echo "Cleaning junk..."
	@rm -fr ./stylesheets ./sass

	@echo "Compass is ready."
