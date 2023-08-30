
# replace 'flagkernel' with the actual flag kernel found by solving the challenge where flagkernel is given by CTFlearn{flagkernel}

openssl enc -d -v -aes-256-cbc -pbkdf2 -in DuneSource.zip.enc -out DuneSource.zip -k flagkernel

