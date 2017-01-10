# FileMapper
[<img src="https://www.python.org/static/opengraph-icon-200x200.png" title="Python.org"
align="right" width="50">](https://www.python.org/)

*Read this in other languages: [English](README.md), [Spanish](README.es.md).*

##### Description
FileMapper software to help organize your stuff developed mainly in python 2.7

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system

## Index of Contents

1. [Requirements](#installation)
 * [Dependencies](#dependencies)
 * [Installation](#installation)
2. [Usage](#usage)
3. [License](#license)
4. [Galung-Project][galung_project_link]

## Requirements
Galung-Project requires [python 2.7.x][python_download_link]  and [pip installer][pip_installer_link] installed in your machine to be able to run install.sh. 

### Dependencies

* [pysrt][pysrt_link]
* [langdetect][langdetect_link]
* [pandas][pandas_link]
* [numpy][numpy_link]
* [tvdb_api][tvdb_api_link]

### Installation

Go to the /path/path and run install.sh, this will donwload all the modules required for the software to run propperly

Install the dependencies to be able to start the software.

```sh
$ 
$ pip install pysrt
$ pip install langdetect
$ pip install pandas
$ pip install numpy
$ pip install tvdb_api
$ pip install 
$
```

**[Back to index of contents](#index-of-contents)**

### Modules
FileMapper it's currently developing this table of plugins 


|     | Status        | Show | Movie | Anime |
|:-------------:|:-------------:|:-----------:|:------------:|:------------:|
| FileMapper |  Still Developing| YES | YES | YES |

### Recognized Formats

Anime Format:

**[_< Uploader >_ ]** : **_< Anime Name >_** : **_< (Episode | Ep | E | x | - ) 000 >_** : **_< Episode Name >_** : **_< Quality >_**

Movie Format:

 **_< Movie Name >_** : **_< ( Year ) >_** : **_< Movie Flag >_** : **_< Quality >_**

Show Format:
 
  **_< Show Name >_** : **_< E00S00 >_** : **_< Episode Name >_** : **_< Quality >_**


## Usage

```python
import filemapper as fm

def main():
 return
```

#### TreeRoot Structure
******************
[<img src="https://s28.postimg.org/5xne6f7st/Untitled_Diagram_1.png" title="TreeRoot"
align="center" height="325" width="550">](https://s28.postimg.org/5xne6f7st/Untitled_Diagram_1.png)


### License

**[Back to index of contents](#index-of-contents)**


[readme_fm_link]: <https://github.com/AsiganTheSunk/galung-project/blob/master/trunk/filemapper/README.md>
[readme_cm_link]: <https://github.com/AsiganTheSunk/galung-project/blob/master/trunk/filemapper/README.md>

[pip_installer_link]: <https://pip.pypa.io/en/stable/installing/>
[python_download_link]: <https://www.python.org/downloads/>

[tvdb_api_link]: <https://github.com/dbr/tvdb_api>
[pysrt_link]: <https://github.com/byroot/pysrt>
[langdetect_link]: <https://github.com/Mimino666/langdetect>
[pandas_link]: <http://pandas.pydata.org/>
[numpy_link]: <http://www.numpy.org/>

[galung_project_link]: <https://github.com/AsiganTheSunk/galung-project/blob/master/README.md>

