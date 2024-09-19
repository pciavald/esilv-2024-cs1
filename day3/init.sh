which python3

python3 -m venv .venv

# PATH=/Users/peac/.gvm/bin:/Users/peac/.nvm/versions/node/v16.20.0/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/local/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/appleinternal/bin:/Library/TeX/texbin:/Applications/iTerm.app/Contents/Resources/utilities:/Users/peac/go/bin:/opt/homebrew/opt/go@1.19/libexec/bin

source .venv/bin/activate

# PATH=/Users/peac/Documents/work/esilv-2024-cs1/day3/.venv/bin:/Users/peac/.gvm/bin:/Users/peac/.nvm/versions/node/v16.20.0/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/local/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/appleinternal/bin:/Library/TeX/texbin:/Applications/iTerm.app/Contents/Resources/utilities:/Users/peac/go/bin:/opt/homebrew/opt/go@1.19/libexec/bin

which python3
# /Users/peac/Documents/work/esilv-2024-cs1/day3/.venv/bin/python

echo "matplotlib" > requirements.txt
pip install -r requirements.txt 

echo "numpy" >> requirements.txt
pip install -r requirements.txt 

du -hs .venv
