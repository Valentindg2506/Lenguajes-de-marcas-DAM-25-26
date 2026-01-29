# En el shell (terminal):
# echo 'export NOMBRE="Valentin"' >> ~/.bashrc
# source ~/.bashrc
import os

print(os.environ.get("NOMBRE"))
