openssl req -new -sha256 -x509 -nodes -days 365 -newkey rsa:2048 -keyout ${1:-server}.key -subj "/C=IN/ST=KA/O=Cisco Systems/CN=seccon-ctf" -reqexts v3_ca -config <(cat /etc/ssl/openssl.cnf <(printf "[v3_ca]\nsubjectAltName=IP:10.203.48.183,DNS:ctf.captchaflag.com,DNS:ctf-2017-test.captchaflag.com,DNS:ctf-2017.captchaflag.com")) -out ${1:-server}.crt

