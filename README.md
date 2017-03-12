# Galung-Project
[<img src="https://www.python.org/static/opengraph-icon-200x200.png" title="Python.org"
align="right" width="50">](https://www.python.org/)

*Read this in other languages: [English](README.md), [Spanish](README.es.md).*


##### Description
Galung-Project it's a concept software to help organize your multimedia content, this program it's being developed mainly in python 2.7

Development of the assistance platform for xmbc enviroments where the application excells on helping you retrieve information about the
multimedia content, also known as metadata about public multimedia files using (http/https) requests and peer to peer protocols. It also
containts some aditional features such as sincronize reproduction of some content throught the network, re-codec and audio video aligment
on multimedia files .mkv and .mp4.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system


## Index of Contents


1. [Requirements](#installation)
 * [Dependencies](#dependencies)
 * [Installation](#installation)
2. [Plugins](#plugins)
  * [FileMapper][readme_fm_link]
3. [Usage](#usage)
4. [License](#license)

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
 
python-mal (0.1.7)
pandas (0.19.2)
pysrt (1.1.1)
requests (2.13.0)
beautifulsoup4 (4.5.3)
enum (0.4.6)
Cython (0.25.2)
IMDbPY (5.1.1)
langdetect (1.0.7)
logging (0.4.9.6)


```

### Plugins

Galung-Project it's currently developing this table of plugins 


| Pluguin       | Status        | Show | Movie | Anime |
|:-------------:|:-------------:|:-----------:|:------------:|:------------:|
| [FileMapper][readme_fm_link] | Developing | Yes | Yes |  |
| [ConstellationMapper][readme_cm_link] | Developing | - | - | - | - |
| [FFmpeg][readme_cm_link] | Developing | - | - | - | - |

**[Back to index of contents](#index-of-contents)**

### Usage

**[Back to index of contents](#index-of-contents)**

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