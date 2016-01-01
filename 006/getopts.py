import sys
import getopt


print 'ARGV    :', sys.argv[1:]


filename = sys.argv[1]
options, remainder = getopt.getopt(sys.argv[2:], 'o:', ['option='])

print 'OPTIONS    :', options

for opt, arg in options:
    if opt in ('-o', '--option'):
        type = arg

print 'TYPE    :', type



