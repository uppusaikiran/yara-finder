# Yara-Finder
A simple tool to yara match the file against various yara rules to find the indicators of suspicion.

<img src="https://travis-ci.org/uppusaikiran/yara-finder.svg?branch=master">


# Usage:

### Clone the Repo and install and run the command `pip install -r requirements.txt'

```
admin@cuckoo /tmp % git clone git@github.com:uppusaikiran/yara-finder.git
Cloning into 'yara-finder'...
remote: Counting objects: 577, done.
remote: Compressing objects: 100% (533/533), done.
remote: Total 577 (delta 46), reused 567 (delta 36), pack-reused 0
Receiving objects: 100% (577/577), 1.43 MiB | 580.00 KiB/s, done.
Resolving deltas: 100% (46/46), done.
Checking connectivity... done.
admin@cuckoo /tmp % cd yara-finder
admin@cuckoo /tmp/yara-finder
 % pip install -r requirements.txt

```
### To the Run the program

```
admin@cuckoo /tmp/yara-finder
 % python app.py
Compiling rules from /tmp/yara-finder/rules
 * Running on http://0.0.0.0:7777/ (Press CTRL+C to quit)

```

#### Here the App will be listening.Now we can submit the files to get the yara_matches.

```
admin@cuckoo /tmp/yara-finder/tests
 %  curl  -X POST -F file=@test.pdf http://0.0.0.0:7777/yara
{
  "match": [
    "domain",
    "Big_Numbers1",
    "multiple_versions",
    "url",
    "contentis_base64",
    "multiple_versions",
    "Big_Numbers1"
  ],
  "status": "success"
}

```

## Docker Usage:
```
docker pull uppusaikiran/yara-finder
docker run -p 7777:7777 --rm -it yara-finder
admin@cuckoo /tmp/yara-finder/tests
 %  curl  -X POST -F file=@test.pdf http://0.0.0.0:7777/yara
{
  "match": [
    "domain",
    "Big_Numbers1",
    "multiple_versions",
    "url",
    "contentis_base64",
    "multiple_versions",
    "Big_Numbers1"
  ],
  "status": "success"
}

