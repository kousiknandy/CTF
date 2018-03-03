#!/usr/bin/python3
import subprocess
from http import cookies
import datetime
import base64
import os
import cgi
from pathlib import Path
import codecs

def encode_function(cookie):
    return codecs.getencoder('rot-13')(cookie)[0]

def sxor(s1,s2="sixteencharacter"):
        return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

def obfuscate(t1):
    return (t1 * 16764)

given_time = 2
ontime = False
flagprint = False
expiration = datetime.datetime.now() + datetime.timedelta(seconds=given_time)
timestamp = expiration.timestamp()
timestamped = expiration.timestamp()
form = cgi.FieldStorage()
captchatext = form.getvalue('captchatext')
actualtext = ""
prev_cookie = cgi.escape(os.environ['HTTP_COOKIE'])
if prev_cookie:
    prev_session = prev_cookie.split("=")[1]
    extractcookie = encode_function(prev_session)
    actualtext = extractcookie[:6]
    timestamped = extractcookie[7:]
    try:
        if (float(timestamped) + obfuscate(given_time)) > obfuscate(timestamp):
            ontime = True
        if actualtext == captchatext:
            flagprint = True
    except:
        pass
    
cp = subprocess.run(["./cgi-bin/captcha", "-m", "both"], stdout=subprocess.PIPE, cwd=".") 
filename = cp.stdout.rstrip().decode('UTF-8')
image = Path(filename).read_bytes()
inlineimage = base64.b64encode(image).decode('ASCII')
cookie = cookies.SimpleCookie()
Path(filename).unlink()
filename = filename.split("/")[2]
cookie["session"] = encode_function(filename.split('.')[0] + "_" + str(obfuscate(timestamp)))
cookie["session"]["path"] = "/"
cookie["session"]["expires"] = expiration.strftime("%a, %d %b %Y %H:%M:%S UTC")

print("Content-type: text/html")
print(cookie)
print()
print("<html><head></head><body>")
if flagprint:
    if ontime:
        print("flag{sCrIpt_paSSed_TurIng_TeSt}")
        print("</body></html>")
        exit()
    else:
        print("Answer was correct but you have to solve it faster (in", given_time, "seconds) <br/>")
#print("<h4>Last submission", captchatext, "vs", actualtext, "@", timestamped, "vs", obfuscate(timestamp), ontime, flagprint, "</h4>")
print("<form action=\"/cgi-bin/catchme.py\" method=\"POST\">")
print("<img src=\"data:image/png;base64,", inlineimage, "\" alt=\"\"/>", sep='')
print(""" <script type="text/javascript">
var timeleft = 2;
var downloadTimer = setInterval(function(){
  document.getElementById("progressBar").value = 2 - --timeleft;
  if(timeleft <= 0)
    clearInterval(downloadTimer);
},1000);
</script>
<progress value="0" max="2" id="progressBar"></progress>
""")
print("<br/>Enter captcha text above: <input type=\"text\" name=\"captchatext\"/>  <input type=\"submit\" value=\"Submit\">")
print("</form>")
#print("<pre>")
#for k in sorted(os.environ.keys()):
#        print("%s\t%s" % (cgi.escape(k), cgi.escape(os.environ[k])))
#print("</pre>")
print("</body></html>")
