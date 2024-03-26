#!/bin/bash
iname='bdse33_g2_drin-kshop_prediction' # image name 
cname='drink-shop_pred' # container name
echo "Create new container ${cname}..."
docker stop ${cname} &>/dev/null
docker rm ${cname} &>/dev/null
docker run -d -p 5000:5000 --name ${cname} ${iname}

