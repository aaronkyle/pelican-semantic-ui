#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from invoke import run, task

import os
import sys
import shutil
import socketserver

from pelican.server import ComplexHTTPRequestHandler

DEPLOY_PATH = 'output'

# Port for `serve`
PORT = 8000

@task
def clean():
    """Remove generated files"""
    if os.path.isdir(DEPLOY_PATH):
        shutil.rmtree(DEPLOY_PATH)
        os.makedirs(DEPLOY_PATH)

@task
def build():
    """Build local version of site"""
    run('pelican -s pelicanconf.py')

@task
def production_build():
    run('pelican -s publishconf.py')

@task
def serve():
    """Serve site at http://localhost:8000/"""
    os.chdir(DEPLOY_PATH)

    class AddressReuseTCPServer(socketserver.TCPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(('', PORT), ComplexHTTPRequestHandler)

    sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
    server.serve_forever()

def gh_pages():
    """Publish to GitHub Pages"""
    clean()
    production_build()

    run("ghp-import -b gh-pages demo/output")
    run("git push origin  gh-pages")