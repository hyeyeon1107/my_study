token: 

sudo apt update
sudo apt install -y python3-venv python3-pip git

git clone https://github.com/pasta1513/aws_practice.git
ls

cd aws_practice
python3 -m venv .venv
ls -a
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000

sudo tee /etc/systemd/system/fastapi.service > /dev/null << 'EOF'
[Unit]
Description=FastAPI aws_practice
After=network.target
[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/aws_practice
ExecStart=/home/ubuntu/aws_practice/.venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000
Restart=always
RestartSec=3
[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable --now fastapi
sudo systemctl status fastapi

curl localhost:8000