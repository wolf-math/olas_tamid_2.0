# -*- coding: UTF-8 -*-



import os
import sys
import codecs

if '--interactive' not in sys.argv[1:]:
    if sys.version_info[0] == 2:
        sys.stdout = codecs.getwriter('UTF-8')(sys.stdout, 'strict')
        sys.stderr = codecs.getwriter('UTF-8')(sys.stderr, 'strict')
    else:
        sys.stdout = codecs.getwriter('UTF-8')(sys.stdout.buffer, 'strict')
        sys.stderr = codecs.getwriter('UTF-8')(sys.stderr.buffer, 'strict')

if '/usr/share/texlive/texmf-dist/scripts/pythontex' and '/usr/share/texlive/texmf-dist/scripts/pythontex' not in sys.path:
    sys.path.append('/usr/share/texlive/texmf-dist/scripts/pythontex')
from pythontex_utils import PythonTeXUtils
pytex = PythonTeXUtils()

pytex.docdir = os.getcwd()
if os.path.isdir('.'):
    os.chdir('.')
    if os.getcwd() not in sys.path:
        sys.path.append(os.getcwd())
else:
    if len(sys.argv) < 2 or sys.argv[1] != '--manual':
        sys.exit('Cannot find directory .')
if pytex.docdir not in sys.path:
    sys.path.append(pytex.docdir)



pytex.id = 'py_default_default'
pytex.family = 'py'
pytex.session = 'default'
pytex.restart = 'default'

pytex.command = 'code'
pytex.set_context('python=python3')
pytex.args = ''
pytex.instance = '0'
pytex.line = '8'

print('=>PYTHONTEX:STDOUT#0#code#')
sys.stderr.write('=>PYTHONTEX:STDERR#0#code#\n')
pytex.before()


def neat():
^^Ireturn 'neat jeans'


pytex.after()
pytex.command = 'i'
pytex.set_context('python=python3')
pytex.args = ''
pytex.instance = '1'
pytex.line = '14'

print('=>PYTHONTEX:STDOUT#1#i#')
sys.stderr.write('=>PYTHONTEX:STDERR#1#i#\n')
pytex.before()

print(pytex.formatter(neat()))


pytex.after()


pytex.cleanup()
