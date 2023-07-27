# Basic Android RE 1!

## Description

* A simple APK, reverse engineer the logic, recreate the flag, and submit!
* [Attachement](https://ctflearn.com/challenge/download/962)

## Solution

1. Using `DIE` or `jadx`, we can analys it


![Imgur](https://i.imgur.com/aCiOZ7t.png)


2. Using https://www.md5online.org/md5-decrypt.html to figure out what password is

![Imgur](https://i.imgur.com/gyXbB0f.png)

* Flag:

```
CTFlearn{Spring2019_is_not_secure!}
```