#!/usr/bin/env python
r"""A JSON syntax validator and formatter tool.

Requires demjson module.

"""
__author__ = "Deron Meranda <http://deron.meranda.us/>"
__homepage__ = "http://deron.meranda.us/python/demjson/"
__date__ = "2014-12-22"
__version__ = "2.2.4"
__credits__ = """Copyright (c) 2006-2015 Deron E. Meranda <http://deron.meranda.us/>

Licensed under GNU LGPL (GNU Lesser General Public License) version 3.0
or later.  See LICENSE.txt included with this software.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>
or <http://www.fsf.org/licensing/>.

"""

import sys

try:
    import demjson3
except ImportError:
    sys.stderr.write("Can not import the demjson Python module.\n")
    sys.stderr.write("Try running:  pip install demjson\n")
    sys.exit(1)


def main():
    lint = demjson3.jsonlint(program_name=sys.argv[0])
    rc = lint.main(sys.argv[1:])
    sys.exit(rc)


if __name__ == "__main__":
    main()
