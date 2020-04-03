#!/bin/bash

# turn on bash's job control
set -m

# Start the primary process and put it in the background
/opt/density/etc/init.d/app_b.init start &

# Start the helper process
/opt/density/etc/init.d/app_a.init start

# the my_helper_process might need to know how to wait on the
# primary process to start before it does its work and returns


# now we bring the primary process back into the foreground
# and leave it there
fg %1
