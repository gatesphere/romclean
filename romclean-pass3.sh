#!/bin/bash

# process kill list
echo "processing kill list..."
killfile="kill.lis"
while read line; do
  rm $line
done < $killfile
echo "done processing kill list."

# process error list
echo "processing error list..."
errorfile="error.lis"
while read line; do
  rm $line
done < $errorfile
echo "done processing error list."