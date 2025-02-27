#!/bin/sh
superset db upgrade
superset init
superset run -p 8088 --host 0.0.0.0
