python -m venv venv

source venv/Scripts/activate

if [ -f requirements.txt ]; then
  pip install -r requirements.txt
else
  echo "The file requirements.txt does not exist. Installing Pillow and numpy by default."
  pip install Pillow numpy
fi

pip freeze > requirements.txt

echo "The virtual environment has been configured and the dependencies have been installed."

source venv/Scripts/activate

echo "Virtual environment activated."