# self-signed-cert

- Setup, Suppose our domain name is cool.domain.yolo

    ```
    cd certs
    openssl genrsa > ssl.key
    openssl req -new -x509 -key ssl.key > ssl.pem
    ```

    with above 2 steps, you are a CA!, now create ca-signed certificate for our website.

    ```
    openssl genrsa -out cool.domain.yolo.key 2048
    openssl req -new -key cool.domain.yolo.key -out cool.domain.yolo.csr
    ```

    Now, we’ll create an X509 V3 certificate extension config file, 
    which is used to define the Subject Alternative Name (SAN) for the certificate. We’ll create a configuration file called cool.domain.yolo.ext, like below `certs/cool.domain.yolo.ext`

    ```
    authorityKeyIdentifier=keyid,issuer
    basicConstraints=CA:FALSE
    keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
    subjectAltName = @alt_names

    [alt_names]
    DNS.1 = cool.domain.yolo
    ```

    Finally we will link up the ssl.key/pem domain name!
    We’ll be running openssl x509 because the x509 command allows us to edit certificate trust settings.
    In this case we’re using it to <b>sign</b> the certificate in conjunction with the config file, which allows us to set the Subject Alternative Name.

    ```
    openssl x509 -req -in cool.domain.yolo.csr -CA ssl.pem -CAkey ssl.key -CAcreateserial -out cool.domain.yolo.crt -days 825 -sha256 -extfile cool.domain.yolo.ext
    ```

- then run it. Here we use nginx for TLS termination, please take a look at nginx/nginx.conf. The below 2 lines are the key..

    ```
    ssl_certificate /etc/my_certs/cool.domain.yolo.crt;
    ssl_certificate_key /etc/my_certs/cool.domain.yolo.key;
    ```

    Now spin up the servers!!
    ```
    docker compose up --build
    ```

- then since this is running on localhost, so please add below line your /etc/hosts 

    ```
    127.0.0.1   cool.domain.yolo
    ```


- Install the root cert

    If you are a real CA, you need to get your root certificate (`ssl.pem`) on all the devices in the world. But we don’t need to become a real CA. We just need to be a CA for the devices you own. We need to add the root certificate to any laptops, desktops, tablets, and phones that access your HTTPS sites. This can be a bit of a pain, but the good news is that we only have to do it once. Our root certificate will be good until it expires.

    ```
    # the install part is in the code..
    python verification.py
    ```

