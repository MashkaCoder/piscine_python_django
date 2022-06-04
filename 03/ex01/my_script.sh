LOG_FILE="pip_install.log"
PYTHON_PATH="python3"
PATH_PY_URL="https://github.com/jaraco/path.git"
VENE_DIR="../local_lib"
SMALL_PROGRAM="my_program.py"

# setup venv
$PYTHON_PATH -m venv $VENE_DIR
source $VENE_DIR/bin/activate

# pip version
python -m pip --version

# pip install
python -m pip install --log $LOG_FILE --force-reinstall git+$PATH_PY_URL

# execute
python $SMALL_PROGRAM
