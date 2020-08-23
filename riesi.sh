#!/usr/bin/env bash

echo "Riesi: False"
echo -n "Riesi?"
read input

if [ "$input" = "y" ]
then
    riesi="True"
else
    riesi="False"
fi

echo "Riesi: $riesi"
