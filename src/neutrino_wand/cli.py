# -*- coding: utf-8 -*-
""" Command Line Interface.
"""
# Copyright © 2014 Jürgen Hermann
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import absolute_import, with_statement

import sys
import logging

from neutrino_wand import pkg_info


class NeutrinoWand(object):
    """ The main `wand` command line application.
    """

    log = logging.getLogger(__name__)

    def __init__(self):
        """Set up main command."""
        project = pkg_info()
        #super(NeutrinoWand, self).__init__(
        #    description=project["description"],
        #    version='0.1', # TODO: need to get version at runtime
        #)


def run(argv=None):
    """Main CLI entry point."""
    cli = NeutrinoWand()
    #return cli.run(sys.argv[1:] if argv is None else argv)
    return 1 # Not implemented


if __name__ == "__main__":
    # When started via "python -m"
    sys.exit(run())
