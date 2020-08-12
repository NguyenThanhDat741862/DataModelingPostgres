# Sparkify Postgres ETL

## Table of Contents

- [Introduction](#introduction)
- [Context](#context)
- [Schema](#schema)
- [Structure](#structure)
- [Usage](#usage)
- [Run](#run)
- [Result](#result)

## Introduction

This project is based on the first project in [Udacity Data Engineering Nanodegree Program](https://www.udacity.com/course/data-engineer-nanodegree--nd027) course.

The aims of this project are:

- Practice doing data modeling with "Star Schema".

- Learn how to build a simple ETL pipeline using Python.

- Learn how to setup RDS using boto3.

## Context

A startup company providing music streaming, named Sparkify, want to analyst their collected user data to make better business decisions.

The application data are available and stored in the format of JSON ( 🠊 in data folder ).

They need a database which is designed to optimize queries for their analysis ( 🠊 the goal of this project ).

## Schema

![alt text](./attachment/schema.png)

## Structure

```
📦DataModelingPostgres
 ┣ 📂attachment
 ┃ ┗ 📜schema.png
 ┣ 📂aws
 ┃ ┣ 📜delete_rds_instance.py
 ┃ ┣ 📜setup_rds_instance.py
 ┃ ┗ 📜__init__.py
 ┣ 📂config
 ┃ ┣ 📜config.py
 ┃ ┗ 📜__init__.py
 ┣ 📂data
 ┃ ┣ 📂log_data
 ┃ ┗ 📂song_data
 ┣ 📂db
 ┃ ┣ 📂connection
 ┃ ┃ ┣ 📜connection.py
 ┃ ┃ ┣ 📜execute_sql.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂queries
 ┃ ┃ ┣ 📜create_tables.py
 ┃ ┃ ┣ 📜drop_tables.py
 ┃ ┃ ┣ 📜insert_tables.py
 ┃ ┃ ┣ 📜select_queries.py
 ┃ ┃ ┣ 📜setup_db.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📜create_db.py
 ┃ ┣ 📜create_schema.py
 ┃ ┣ 📜insert_db.py
 ┃ ┣ 📜select_song.py
 ┃ ┗ 📜__init__.py
 ┣ 📂etl
 ┃ ┣ 📜etl.py
 ┃ ┣ 📜process_log_file.py
 ┃ ┣ 📜process_song_file.py
 ┃ ┗ 📜__init__.py
 ┣ 📂logger
 ┃ ┣ 📜logger.py
 ┃ ┗ 📜__init__.py
 ┣ 📂logs
 ┃ ┗ 📜.gitkeep
 ┣ 📜.gitignore
 ┣ 📜config.template.ini
 ┣ 📜main.py
 ┣ 📜Pipfile
 ┣ 📜Pipfile.lock
 ┣ 📜README.md
 ┣ 📜requirements.txt
 ┗ 📜result.ipynb
```

## Usage

1. Clone repository

```
  git clone https://github.com/NguyenThanhDat741862/DataModelingPostgres.git
```

2. Cd into directory

```
  cd DataModelingPostgres
```

3. Install dependencies using npm

```
  pip install -r requirements.txt
```

## Run

```
  python ./main.py
```

## Result

- Can be found in logs folder ( logs/log.log ).

- Open result.ipynb file and run all.