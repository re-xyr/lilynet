#!/bin/sh
mkdir -p /etc/bird
curl -sfSLR -o /etc/bird/roa_dn42.conf -z /etc/bird/roa_dn42.conf https://dn42.burble.com/roa/dn42_roa_bird2_4.conf
curl -sfSLR -o /etc/bird/roa_dn42_v6.conf -z /etc/bird/roa_dn42_v6.conf https://dn42.burble.com/roa/dn42_roa_bird2_6.conf
rc-service bird reload || echo "Failed to reload BIRD service"
