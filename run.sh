source ./env/bin/activate
pip freeze > requirements.txt
pip install -r requirements.txt

./script_book.sh
