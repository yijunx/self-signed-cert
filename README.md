# self-signed-cert

- decide YOUR_DOMAIN_NAME and then generate self signed ssl key / cert and put into certs folder, and generate ca.crt in the root

- then run

    ```
    docker compose up --build
    ```

- then since this is running on localhost, so please add below line your /etc/hosts 

    ```
    127.0.0.1   YOUR_DOMAIN_NAME
    ```


- then you can edit the verification.py (replace YOUR_DOMAIN_NAME)

    ```
    export REQUESTS_CA_BUNDLE=ca.crt
    python verification.py
    ```

