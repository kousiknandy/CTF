# 2-way

## This is how we can implement 2-way SSL

So we have a simple HTTPS server that authenticates the client not by our
username and password, but a certificate. It accepts self-signed certificate,
but the "CN" of the certificate must be matching that of the server (though
no hint is given about that).