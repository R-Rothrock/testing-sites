# Testing Sites
Various CTF-like _Flask_ applications and corresponding exploits. The directory
structure is in levels, with the intent that `level1` is easier than `level4`
and so on.

---

This project is still being developed. Feel free to watch this repository to be
notified of it's completion.

## Usage

Like any CTF, your goal is to find a key, which will be a long hex string. In
each `level` directory there will be two directories and two files. The first
one, `app` holds the vulnerable code. The second one, `exploit` hold an explanation
and/or exploit code to the vulnerability. As for the two files, one is called `start`
and should be run as `source start` to activate the server. The other one is a sha256
representation of the key.

Don't look at anything in the `app` directory. That's cheating.
