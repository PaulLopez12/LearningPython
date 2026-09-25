cd Frontend/link_bio
python -m venv .venv
. .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
rm -rf public
reflex init
REFLEX_SSR=false REFLEX_API_URL=https://primera-web-mouredev.up.railway.app/ reflex export --frontend-only
unzip frontend.zip -d public
rm -f frontend.zip
deactivate