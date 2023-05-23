# self-signed-cert

- decide YOUR_DOMAIN_NAME and then generate self signed ssl key / cert and put into certs folder, and generate ca.crt in the root

    ```
    cd certs
    openssl genrsa > ssl.key
    openssl req -new -x509 -key ssl.key > ssl.pem

    # with above 2 steps, you are a CA!
    # now create ca-signed certificate for dev sites
    # suppose our domain name is cool.domain.yolo

    openssl genrsa -out cool.domain.yolo.key 2048
    openssl req -new -key cool.domain.yolo.key -out cool.domain.yolo.csr

    # Finally, we’ll create an X509 V3 certificate extension config file, 
    # which is used to define the Subject Alternative Name (SAN) for the certificate. 
    # In our case, we’ll create a configuration file called cool.domain.yolo.ext

    # like below
    authorityKeyIdentifier=keyid,issuer
    basicConstraints=CA:FALSE
    keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
    subjectAltName = @alt_names

    [alt_names]
    DNS.1 = cool.domain.yolo

    # We’ll be running openssl x509 because the x509 command allows us to edit certificate trust settings.
    # In this case we’re using it to sign the certificate in conjunction with the config file,
    # which allows us to set the Subject Alternative Name.

    openssl x509 -req -in cool.domain.yolo.csr -CA ssl.pem -CAkey ssl.key -CAcreateserial -out cool.domain.yolo.crt -days 825 -sha256 -extfile cool.domain.yolo.ext

    ```

- then run

    ```
    docker compose up --build
    ```

- then since this is running on localhost, so please add below line your /etc/hosts 

    ```
    127.0.0.1   cool.domain.yolo
    ```


- then you can edit the verification.py (replace YOUR_DOMAIN_NAME)

    ```
    export REQUESTS_CA_BUNDLE=ca.crt
    python verification.py
    ```

