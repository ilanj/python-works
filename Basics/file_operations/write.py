import json

f=open("G:\workspace\pythontutorial\writefile.txt","w")
# f.write("qefefef\n")
# f.write("frfrfrf")
data="""We can’t connect to the server at pythonspot.com.

If that address is correct, here are three other things you can try:

    Try again later.
    Check your network connection.
    If you are connected but behind a firewall, check that Firefox has permission to access the Web."""
f.write(data)