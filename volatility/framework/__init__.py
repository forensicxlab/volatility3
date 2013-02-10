###
#
# Libtool version scheme
#
# Current - The number of the current interface exported by the library
# Revision - The implementation number of the most recent interface exported by this library
# Age - The number of previous additional interfaces supported by this library
#
# 1. If the source changes, increment the revision
# 2. If the interface has changed, increment current, set revision to 0
# 3. If only additions to the interface have been made, increment age
# 4. If changes or removals of the interface have been made, set age to 0

_current = 3    # Number of releases of the library with any change
_revision = 0   # Number of changes that don't affect the interface
_age = 0        # Number of consecutive versions of the interface the current version supports

import volatility.framework.exceptions as exceptions

@property
def version():
    return _current - _age, _age, _revision

def require_version(*args):
    if len(args):
        if args[0] != version[0]:
            raise exceptions.VolatilityException("Framework version " + str(version[0]) + " is incompatible with required version " + str(args[0]))
        if len(args) > 1:
            if args[1] > version[1]:
                raise exceptions.VolatilityException("Framework version " + ".".join([str(x) for x in version[0:1]]) + " is an older revision than the required version " + ".".join([str(x) for x in args[0:2]]))



