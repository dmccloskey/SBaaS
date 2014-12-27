from ConfigParser import SafeConfigParser
import os as __os
from os.path import split as __split, join as __join, abspath as __abspath, \
    isfile as __isfile
from sys import modules

self = modules[__name__]

config = SafeConfigParser()
# set the default settings
config.add_section("DATABASE")
config.set("DATABASE", "host", "localhost:5432")
config.set("DATABASE", "database", "metabolomics")
config.set("DATABASE", "password", "18dglass")
config.set("DATABASE", "schema", "public")
config.set("DATABASE", "user", "postgres")

# save options as variables
self.host = config.get("DATABASE", "host")
self.database = config.get("DATABASE", "database")
self.password = config.get("DATABASE", "password")
self.schema = config.get("DATABASE", "schema")
self.user = config.get("DATABASE", "user")