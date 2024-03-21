#!/bin/bash

read -p "Width (mm) [72]: " width
width=${width:-72}

read -p "Height (mm) [115]: " height
height=${height:-115}

echo "Size in mm = ${width}x${height}";

res=23.622
width=$(bc <<< "$res * $width / 1")
height=$(bc <<< "$res * $height / 1")

echo "Size in pixels (600dpi) = ${width}x${height}";

read -p "File name (conference/00): " filename

convert -size ${width}x${height} xc:white -transparent white PNG8:${filename}.png
