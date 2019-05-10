# excel-app
Requirements :
  1. Ubutu 16.04 LTS
  2. python2      :: https://tecadmin.net/install-python-2-7-on-ubuntu-and-linuxmint/
  3. python pip   :: sudo apt install python-pip
  4. virtualenv   :: pip install --user virtualenv
  
Install Modules for the application
  1. create virtual environment :: virtualenv venv
  2. activate the environment   :: source venv/bin/activate
  3. install modules            :: pip install -r requirements.txt

At this point all the pre-quisites for the app are ready lets move to the launch of the app on the development server ( localhost:8000 )

Run the application
  1. goto the application code             :: cd excel_viewer
  2. make any SQL migration/changes if any :: python manage.py makemigrations
  3. migrate the migrations to the DB      :: python manage.py migrate
  4. run the application server            :: python manage.py runserver
  5. open browser ( chrome pref )          :: localhost:8000
  
  
  
