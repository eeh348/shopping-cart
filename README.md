# shopping-cart
Shopping cart application for local grocery store

## Prerequisites

+ Anaconda 3.7
+ Python 3.7
+ Pip

## Installation

Fork this repository under your own control, then clone or download the resulting repository onto your computer. Then navigate there from the command line:

```sh
cd robo-advisor-demo-2019
```

> NOTE: subsequent usage and testing commands assume you are running them from the repository's root directory.

Use Anaconda to create and activate a new virtual environment, perhaps called "stocks-env":

```sh
conda create -n stocks-env python=3.7 # (first time only)
conda activate stocks-env
```

From inside the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

## Setup

Ensure you have access to the following googlesheet:

https://docs.google.com/spreadsheets/d/1zfQIKuK8LW-7miV_YcVN98_YPS_GDBX-qNyJknNRWU0/edit#gid=0

1. Obtain an OAuth 2.0 key from Google API Console - https://developers.google.com/identity/protocols/OAuth2
2. Share sheet with email noted in JSON file
3. Save JSON file to repo as "my_cred.json"


