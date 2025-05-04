echo "[*] Installing ASCII TRANSLATOR"
sudo apt update && sudo apt install tor python3-pip libatlas-base-dev -y

echo "[*] Installing Python requirements..."
pip3 install -r requirements.txt

echo "[*] Setup complete."
echo "[*] To run the script, use the command: python3 ascii_converter.py"