pip uninstall -y bunyafinder
rm -rf bunyafinder.egg-info
rm -rf dist
python setup.py sdist
pip install dist/bunyafinder-1.0.tar.gz
