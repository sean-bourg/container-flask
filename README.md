# Generate SSL Certs
```
# Generate SSL certs for site.
openssl req -x509 -nodes -days 365 \
    -newkey rsa:2048 \
    -keyout docker/proxy/ssl/private/site.key \
    -out docker/proxy/ssl/certs/site.crt
openssl dhparam -out docker/proxy/ssl/certs/site.pem 2048    
```