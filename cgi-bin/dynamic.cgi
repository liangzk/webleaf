#!/bin/bash
echo "Content-type: text/html"
echo
echo "<html>"
echo "<head><title>Hello</title></head>"
echo "<body>"
echo "<h1>Hello</h1>"
echo $*    #print out information received from user via URL
echo "</body>"
echo "</html>"
