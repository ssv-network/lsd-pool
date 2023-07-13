
@REM Prerequisites (install first)
@REM Git, NPM, Yarn and Pip

@echo off

npm install
npm install yarn
if exist "ssv-keys" (
    echo ssv-keys directory already there
) else (
    echo cloning ssv-keys
    git clone https://github.com/bloxapp/ssv-keys.git
    cd ssv-keys
    git fetch -a
    git checkout main
    cd ..
    del ssv-keys\package.json
    copy ssv\package.json ssv-keys\package.json
    yarn --cwd ssv-keys install 
    yarn --cwd ssv-keys package-win
    copy ssv-keys\bin\win\ssv-keys.exe ssv\ssv-cli.exe
)

echo setup for ssv keys cli done
echo downloading dependencies for python
pip install -r requirements.txt
