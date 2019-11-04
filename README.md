# ftp_path_py
delete and upload path for ftp server by python

# use

## delete ftp path

``` python
>>> from ftp_path_operate import FTPPath
>>> ftp = FTPPath('ftphost', 'user', 'password')
>>> ftp.delete_path('test')
```

## upload path to ftp server
``` python
>>> from ftp_path_operate import FTPPath
>>> ftp = FTPPath('ftphost', 'user', 'password')
>>> ftp.upload_path('test')
```
