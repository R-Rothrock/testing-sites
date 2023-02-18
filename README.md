# Testing Sites
Various CTF-like _Flask_ applications and corresponding exploits. The directory
structure is in levels, with the intent that `level1` is easier than `level4`
and so on.

---

This project is still being developed. Feel free to watch this repository to be
notified of it's completion.

## Usage

Like any CTF, your goal is to find a key, which will be a long hex string. In
each `level` directory there will be two directories. The first one, `app`
holds the vulnerable code and a SHA256 representation of the key. In the second
directory, the `exploit` directory, there will be code and/or instructions on
how to get the key.
