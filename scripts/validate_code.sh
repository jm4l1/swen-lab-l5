#! /bin/bash

echo -n "Validating all TODOs have been removed: "
if grep -r --include="server.py" -n "TODO" . > /dev/null; then
    echo "❌ Fail: Found TODOs in code."
else
    echo "✅ Pass: No TODOS founds."
fi

echo -n "Validating Code Formatting: "
docker compose exec server black server.py  -v 1> /dev/null 2> /dev/null
if [[  ! $? -eq 0 ]]; then
    echo "😞 Awww: Code format check returned errors."
else
    echo "😎 Yea: Code format check returned no errors."
fi
