## GENERATE NEW ONE:

1. openssl genrsa -out depremmarket.key 2048
<!-- openssl req -new -sha256 -key depremmarket.key -out csr.csr -->
2. openssl req -x509 -sha256 -days 365 -key depremmarket.key -in csr.csr -out depremmarket.crt
3. openssl req -in csr.csr -text -noout | grep -i "Signature.*SHA256" && echo "All is well"
