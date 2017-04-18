#!/bin/bash

# Dependencies:
# imagemagick
# i3lock
# scrot

FONT="InputMono"
IMAGE=/tmp/i3lock.png
TEXT=$(expand -t 2 <(fortune -s))
ICON="$HOME/.bin/icons/lock2.png"
scrot $IMAGE
convert -scale 10% -scale 1000% -font "$FONT" -pointsize 20 -gravity center -annotate +0+160 "$TEXT" "$ICON" -gravity center -composite "$IMAGE" $IMAGE $IMAGE
#convert "$IMAGE" -font "$FONT" -pointsize 20 -fill "$BW" -gravity center \
 #   -annotate +0+160 "$TEXT" "$ICON" -gravity center -composite "$IMAGE"
i3lock -i $IMAGE
rm $IMAGE