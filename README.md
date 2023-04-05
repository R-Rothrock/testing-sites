# Testing Sites

This is a repository of various Python Flask applications designed similar to CTF
challenges. They are categorized by level (`level1`, `level2`, etc.) with the intent that
higher levels are more difficult.

## Uage

The manifest for each level directory:
 - `app.py` the flask server itself
 - `requirements.txt` the requirements of the flask server.
 - `sha256.txt` a SHA256 representation of the key for key verification.
 - `templates/` where all the static files are stored (looking in here is cheating).
 - `exploit/` contains a description and instructions in case you're stumped.

First, confirm the requirements in `requirements.txt` are fufilled. Then, simply run
`app.py` to initialize the server. It should be accessable at `localhost:5001`.
