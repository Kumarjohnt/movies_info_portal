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
    # Create a virtualenv named cefalo_test_venv
    virtualenv -p python3 venvs/cefalo_test_venv
    # Activate the created env
    source venvs/cefalo_test_venv/bin/activate
elif [[ "$os" == 'WINDOWS' ]]; then
    # Make a directory named venvs
    mkdir \venvs
    # Install virtualenv
    pip install virtualenv
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
cp -v example_env.py env.py

# Install required packages
pip install -r requirements.txt

# Make migrations
python manage.py makemigrations

# Migrate database
python manage.py migrate

# Run python shell to seed wiki data
python manage.py shell

# Run project
python manage.py runserver