#!/bin/sh

sleep 3
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/tmp
/system/bin/webrtc_stream &
