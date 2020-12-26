PATH=$WORKSPACE/venv/bin:$HOME/.local/bin:$PATH

if [ ! -d "venv" ]; then
		pip install virtualenv --user
        virtualenv venv
fi
. venv/bin/activate
pip install -r requirements.txt
pytest -s -v --html=./Reports/report.html testCases/ --browser chrome