#!/bin/bash
iname='bdse33_g2_drin-kshop_prediction' # image name
cname='drink-shop_pred' # container name
docker build -t ${iname} .
docker run -d -p 5000:5000 --name ${cname} ${iname}

