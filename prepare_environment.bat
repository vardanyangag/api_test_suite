if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

echo Activating virtual environment...
call venv\Scripts\activate


echo Installing required libraries...
pip install requests
pip install pytest
pip install pytest-html

echo Environment setup completed.
