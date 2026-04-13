import json
import logging
import os

from pymongo import MongoClient

from flask_authnz import FlaskAuthnz, MongoDBRoles, UserGroups

logger = logging.getLogger(__name__)

__author__ = 'mshankar@slac.stanford.edu'

# Application context.
app = None


def __read_from_file__(envname, varname, theenv):
    if envname in os.environ and os.path.exists(os.environ[envname]):
        with open(os.environ[envname], "r") as f:
            theenv[varname] = f.read().strip()
    else:
        raise Exception(f"File for {varname} not found")

calibdbenv = {}
__read_from_file__("CALIBDB_URL_FILE", "CALIBDB_URL", calibdbenv)
__read_from_file__("ROLEDB_URL_FILE",  "ROLEDB_URL",  calibdbenv)

# Set up the Mongo connection.
CALIBDB_URL=calibdbenv.get("CALIBDB_URL", None)
if not CALIBDB_URL:
    print("Please use the enivironment variable CALIBDB_URL to configure the calibration database connection.")    
mongoclient = MongoClient(host=CALIBDB_URL, tz_aware=True)

ROLEDB_URL=calibdbenv.get("ROLEDB_URL", None)
roledbclient = mongoclient
if ROLEDB_URL:
    print("Using a different database for the roles")
    roledbclient = MongoClient(host=ROLEDB_URL, tz_aware=True)
else:
    print("Using the same database for the roles")

# Set up the security manager
usergroups = UserGroups()
roleslookup = MongoDBRoles(roledbclient, usergroups)
security = FlaskAuthnz(roleslookup, "LogBook")
