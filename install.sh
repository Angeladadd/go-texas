if [[ "$(uname)" == "Darwin" && "$(uname -m)" == "arm64" ]] ; then
    pip3 install --break-system-packages -r requirements.txt
else
    pip3 install -r requirements.txt
fi
python3 install_helper.py
sudo cp gotexas /usr/local/bin
sudo chmod +x /usr/local/bin/gotexas