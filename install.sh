virtualenv ../ENV
source ../ENV/bin/activate
pip install -r requirements.txt
pip install https://github.com/hiidef/oauth2app/tarball/master django-test-coverage
./manage.py syncdb
./manage.py runserver 0.0.0.0:8001
