# Yara-Finder
A simple tool to yara match the file against various yara rules to find the indicators of suspicion.

<img src="https://travis-ci.org/uppusaikiran/yara-finder.svg?branch=master">


# Usage:

### Clone the Repo and install and run the command `pip install -r requirements.txt`

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
### use case for malicious sample

```
curl  -X POST -F file=@e336f967802da8342f724d56dadb1e54200840f681927ba6b3d0a5a1dab3e3c2 http://0.0.0.0:7777/yara
{
  "match": [
    "domain",
    "anti_dbg",
    "win_mutex",
    "win_registry",
    "win_files_operation",
    "VC8_Microsoft_Corporation",
    "Microsoft_Visual_Cpp_8",
    "IsPE32",
    "IsWindowsGUI",
    "HasDebugData",
    "HasRichSignature",
    "Advapi_Hash_API",
    "BASE64_table",
    "maldoc_find_kernel32_base_method_1",
    "VC8_Microsoft_Corporation",
    "Microsoft_Visual_Cpp_8",
    "anti_dbg",
    "win_mutex",
    "win_registry",
    "win_files_operation",
    "IsPE32",
    "IsWindowsGUI",
    "HasDebugData",
    "HasRichSignature",
    "System_Tools",
    "Dropper_Strings",
    "Misc_Suspicious_Strings",
    "contentis_base64",
    "maldoc_find_kernel32_base_method_1",
    "Advapi_Hash_API",
    "BASE64_table"
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
```

## Features:

* Easy to Deploy and simple to use.
* Ability to extend the yara rules with custom and third-party rules simply adding them in the rules folder.
* Uses multiple layered scanning for finding yara matches including zip file extraction,applying yara on internal files as well.
* Frequent Yara-rules updation to the repo.
