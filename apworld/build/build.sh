#!/usr/bin/env bash

set -xe

APWORLD_NAME="peaks_of_yore"
SRC_DIR="../src/"

cp -r "$SRC_DIR" "$APWORLD_NAME/"
zip -r "$APWORLD_NAME.apworld" "$APWORLD_NAME/"
rm -rf "$APWORLD_NAME/"
