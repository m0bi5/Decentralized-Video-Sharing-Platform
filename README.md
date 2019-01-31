# Decentralized Video Sharing Platfrom

### Introduction

YouTube has undoubtedly become the biggest free video sharing platform on the internet since its inception in 2005. To promote content creation, the founders introduced a partnership program. To be eligible for the program certain criteria must be met and officials at YouTube must review your channel. Once enrolled, the content creators earn 55% of the revenue generated by ads embedded in their videos. On January 2018, the criteria were set so that the content creators needed at least 4000 hours of playback within the past 12 months and 1000 subscribers. This criteria changes from time to time and has been a hindrance to many smallscale content creators. Unless the content creators have other revenue streams, they are at mercy of YouTube. 

The main aim of this project is to shift the above-mentioned power from conglomerates to the viewers of the content. All videos uploaded onto the platform will be stored in a Peer-to-Peer network.


-----

### Technologies used 

- IPFS
- Python 3.6
- JavaScript

-----

### Running instructions

Download the ipfs daemon from <a href='https://dist.ipfs.io/#go-ipfs'>here</a>

Once downloaded, unzip the folder and perform installation

```
sudo ./install.sh
```

Initialize an IPFS repository

```
ipfs init
```

Install dependencies

```
pip install -r requirements.txt
```

Run the django webserver

```
python manage.py runserver
```