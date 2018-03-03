# WEA(K)CAPTCHA

This throws a random captcha to the user. Unfortunately the time given to solve the captcha is only a few seconds and it is humanly impossible to type all of it in due time. However the cookie carries the captcha text, with a simple encoding. To beat the captcha write a script that decodes the cookie and submits it instantly.

### Technical details

The server is stateless. So it sends a cookie image, and encodes the text in the image into a cookie alongwith an encoded timestamp. When response comes back, if the decoded timestamp is within limit and cookie matches the text we show the flag. There are very easy ways to cheat. 