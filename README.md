# Galung-Project
[<img src="https://www.python.org/static/opengraph-icon-200x200.png" title="Python.org"
align="right" width="50">](https://www.python.org/)

*Read this in other languages: [English](README.md), [Spanish](README.es.md).*


## Description

Galung-Project it's a concept software to help organize your multimedia content, this program it's being developed mainly in python 2.7 focusing on building a robust platform.

The main focus of this project it's the development of the assistance platform for xmbc enviroments, where the application excels on helping you retrieve information, also known as 
metadata, about the multimedia content you already have in your computer, and in some cases it will allow the user to get new content from the public domain. The retrieval of information will come using (http/https) requests and peer to peer protocols.

This software also containts some aditional features such as aligment of multiple audio streams in diferent languages and then join them in one common container, supported formats will be .mkv or .mp4, sincronize reproduction over the network and re-codec video and audio using h265.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 


## Index of Contents

1. [Requirements](#installation)
 * [Dependencies](#dependencies)
 * [Installation](#installation)
2. [Plugins](#plugins)
  * [FileMapper][readme_fm_link]
3. [Usage](#usage)
4. [License](#license)


## Requirements

The basic requirements for galung-project are [python 2.7.x][python_download_link]  and [pip installer][pip_installer_link]. Once you already had installed those requirements then next step it's to 
install the depencies. 


### Dependencies

The following list of libraries are needed to make galung-project work.

* [pysrt][pysrt_link]
* [langdetect][langdetect_link]
* [enum][enum_link]
* [pandas][pandas_link]
* [numpy][numpy_link]
* [cython][cython_link]
* [imdbpy][imdbpy_link]
* [python_mal][python_mal_link]
* [tvdb_api][tvdb_api_link]
* [logging][logging_link]
* [beautifulsoap4][beautifulsoap4_link]
* [requests][requests_link]


### Installation

Go to the main folder of galung-project and run setup.py. This will download and install all the dependecies found on the requirements.txt, so the sotfware can function propperly.

```
pysrt==1.1.1
langdetect==1.0.7
enum==0.4.6
pandas==0.19.2
Cython==0.25.2
IMDbPY==5.1.1
python-mal==0.1.7
tvdb_api==1.10
logging==0.4.9.6
beautifulsoup4==4.5.3
requests==2.13.0

```

### Plugins

Galung-Project will integrate this plugins with an Xmbc Interface. 


| Plugin       | Status        | Show | Movie | Anime |
|:-------------:|:-------------:|:-----------:|:------------:|:------------:|
| [FileMapper][readme_fm_link] | Yes | Yes | Yes |  |
| [ConstellationMapper][readme_cm_link] | Developing | - | - | - | - |
| [FFmpeg][readme_ffmpeg_link] | Developing | - | - | - | - |

#### FileMapper

##### Recognized Formats

Anime Format:

 **[_< Uploader >_ ]** : **_< Anime Name >_** : **_< (Episode | Ep | E | x | - ) 000 >_** : **_< Episode Name >_** : **_< Quality >_**

Movie Format:

 **_< Movie Name >_** : **_< ( Year ) >_** : **_< Movie Flag >_** : **_< Quality >_**

Show Format:

  **_< Show Name >_** : **_< E00S00 >_** : **_< Episode Name >_** : **_< Quality >_**

**[Back to index of contents](#index-of-contents)**


### Usage

```python

from main import filemapper as fm


```

**[Back to index of contents](#index-of-contents)**


### License

**[Back to index of contents](#index-of-contents)**


[readme_fm_link]: <https://github.com/AsiganTheSunk/galung-project/blob/master/trunk/filemapper/README.md>
[readme_cm_link]: <https://dummy_link.com>
[readme_ffmpeg_link]: <https://dummy_link.com>

[pip_installer_link]: <https://pip.pypa.io/en/stable/installing/>
[python_download_link]: <https://www.python.org/downloads/>

[pysrt_link]: <https://github.com/byroot/pysrt>
[langdetect_link]: <https://github.com/Mimino666/langdetect>
[pandas_link]: <http://pandas.pydata.org/>
[numpy_link]: <https://dummy_link.com>
[enum_link]: <https://dummy_link.com>
[logging_link]: <https://dummy_link.com>
[cython_link]: <https://dummy_link.com>
[imdbpy_link]: <https://dummy_link.com>
[python_mal_link]: <https://dummy_link.com>
[tvdb_api_link]: <https://github.com/dbr/tvdb_api>
[logging_link]: <https://dummy_link.com>
[beautifulsoap4_link]: <https://dummy_link.com>
[requests_link]: <https://dummy_link.com>