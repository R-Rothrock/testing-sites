# Testing Sites
Various CTF-like _Flask_ applications and corresponding exploits. The directory
structure is in levels, with the intent that `level1` is easier than `level4`
and so on.

---

This project is still being developed. Feel free to watch this repository to be
notified of it's completion.

## Usage

Like any CTF, your goal is to find a key, which will be a long hex string. In
each `level` directory, you will find the following files:

- `__init__.py` run this to initialize the server.
- `requirements.txt` the requirements of the `__init__.py` script.
- `sha256.txt` a SHA256 representation of the key.

You will also find the following directories:

- `static` where all static files are stored.
- `exploit` where a description and/or exploit code is stored. Only if you're
stumped.

### Note
Accessing the `static` directory is cheating, and only read `__init__.py` as a
hint.

## Also, FYI
If you're curious about the security of this code, take a look at
[SECURITY.md](https://github.com/R-Rothrock/testing_sites/blob/main/SECURITY.md).
Hint; not very secure.

If that doesn't do it, this software is licensed under the _Unlicense_.

