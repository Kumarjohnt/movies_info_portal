# Get OS type
os=""
case "$OSTYPE" in
 solaris*) os=SOLARIS ;;
 darwin*)  os=OSX ;;
 linux*)   os=LINUX ;;
 bsd*)     os=BSD ;;
 msys*)    os=WINDOWS ;;
 *)        os=unknown: $OSTYPE ;;
esac
 
if [[ "$os" == 'LINUX' ]]; then
   # Make a directory named venvs
   mkdir venvs
   # Install virtualenv
   pip3 install virtualenv --user
   # Install virtualenv globally
   sudo apt install virtualenv
   # Create a virtualenv named cefalo_test_venv
   virtualenv -p python3 venvs/cefalo_test_venv
   # Activate the created env
   source venvs/cefalo_test_venv/bin/activate
elif [[ "$os" == 'WINDOWS' ]]; then
   # Make a directory named venvs
   mkdir \venvs
   # Install virtualenv
   pip install virtualenv
   pip install virtualenvwrapper-win
   # Create a virtualenv named cefalo_test_venv
   virtualenv \venvs\cefalo_test_venv
   # Activate the created env
   \venvs\cefalo_test_venv\Scripts\activate
fi
 
# Clone project from git
git clone https://github.com/tssovi/movies_info_portal.git
 
# Go to project directory
cd movies_info_portal
 
# Copy example_env.py as env.py
cp -v movie_portal/example_env.py movie_portal/env.py
 
echo Please Provide Your Existing Database Name:
read db_name
sed -i -- "s/test_db/$db_name/g" movie_portal/env.py

echo Please Provide Your Existing Database Username:
read db_user
sed -i -- "s/test_db_username/$db_user/g" movie_portal/env.py
 
echo Please Provide Your Existing Database Password:
read db_pass
sed -i -- "s/test_db_password/$db_pass/g" movie_portal/env.py
 
# Install required packages
pip install -r requirements.txt
 
# Make migrations
python manage.py makemigrations
 
# Migrate database
python manage.py migrate
 
# Run python shell to seed wiki data
python manage.py data-scraper
 
# Run project
python manage.py runserver
