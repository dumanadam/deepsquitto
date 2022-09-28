#!/usr/bin/env python3
import secrets

RTSPINPUT = secrets.RTSPINPUT      # No default, so it's *REQUIRED*
RTSPOUTPUTPORTNUM = '8554'
RTSPOUTPUTPATH = '/ds'
CODEC = 'H264'
BITRATE = '4000000'
ARCH = 'arm64'                                                  # No default, so it's *REQUIRED*
IPADDR = secrets.IPADDR
SHOW_FRAMES = 'yes'
OUTPUT_WIDTH = 800
OUTPUT_HEIGHT = 450
