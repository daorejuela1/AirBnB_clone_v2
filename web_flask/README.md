![](https://storage.googleapis.com/twg-content/original_images/why-airbnb-takes-a-customer-centric-approach-to-adwords_case-studies_lg.png)

# 0x02. [AirBnB](https://www.airbnb.com) clone - MySQL

## Background Context
Welcome to the [AirBnB clone project Second Part](https://intranet.hbtn.io/concepts/74)! (The Holberton B&B)
Before starting, please read the AirBnB concept page and watch [this video](https://youtu.be/fb2zxES7ROU) from [Bobby Yang](https://twitter.com/bobstermyang), talking about how HBNB project abstracts the storage part: FileStorage and DBStorage.

In this project we must do::

* Replace the file storage by a Database storage
* Map your models to a table in database by using an O.R.M.

<p>
<img src="https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/images/AirBnb_DB_diagramm.jpg" width="80%" height="80%">
</p>

This repository contains the second stage of a student project to build a clone of the AirBnB website. 

Environment variables will be your best friend for this project!

* HBNB_ENV: running environment. It can be “dev” or “test” for the moment (“production” soon!)
* HBNB_MYSQL_USER: the username of your MySQL
* HBNB_MYSQL_PWD: the password of your MySQL
* HBNB_MYSQL_HOST: the hostname of your MySQL
* HBNB_MYSQL_DB: the database name of your MySQL
* HBNB_TYPE_STORAGE: the type of storage used. It can be “file” (using FileStorage) or db (using DBStorage)

See to the following picture:

<p>
<img src="https://github.com/mfcrespo/AirBnB_clone/blob/master/images/Airbnb%20clone%20website.png" width="80%" height="80%">
</p>

AirBnb Clone is a project that consists of several stages linked together, which will be developed step by step:

* The Console
* Web Static
* MySQL storage
* Web framework - templating
* RESTful API
* Web dynamic

### Diagram AirBnB  clone (MySQL storage)
![](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/images/AirbnbMySql.png)

## Storage

Persistency is really important for a web application. It means: every time your program is executed, it starts with all objects previously created from another execution. Without persistency, all the work done in a previous execution won’t be saved and will be gone.

In this project, you will manipulate 2 types of storage: file and database. For the moment, you will focus on file.

Why separate “storage management” from “model”? It’s to make your models modular and independent. With this architecture, you can easily replace your storage system without re-coding everything everywhere.

You will always use class attributes for any object. Why not instance attributes? For 3 reasons:

* Provide easy class description: everybody will be able to see quickly what a model should contain (which attributes, etc…)
* Provide default value of any attribute
* In the future, provide the same model behavior for file storage or database storage

### Files in This Repository:

| File | File Hierarchy | Description |
| :---: | :---: | :---: |
| `console.py` | [console.py](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/console.py) | The main console file |
| `amenity.py` | [models/amenity.py](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/models/amenity.py) | The amenity subclass |
| `base_model.py` | [models/base_model.py](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/models/base_model.py) | The base model superclass |
| `city.py` | [models/city.py](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/models/city.py) | The city subclass | 
| `place.py` | [models/place.py](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/models/place.py) | Te place subclass |
| `review.py` | [models/review.py](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/models/review.py) | Te review subclass |
| `state.py` | [models/state.py](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/models/state.py) | Te state subclass |
| `user.py` | [models/user.py](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/models/user.py) | Te user subclass |
| `file_storage.py` | [models/engine/file_storage.py](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/models/engine/file_storage.py) | The file storage class |
| `db_storage.py` | [models/engine/db_storage.py](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/models/engine/db_storage.py) | The DB storage class |
| `test_amenity.py` | [tests/test_amenity.py](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/tests/test_models/test_amenity.py) | The unittest module for amenity |
| `test_base_model.py` | [tests/base_model.py](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/tests/test_models/test_base_model.py) | The unittest module for base model |
| `test_city.py` | [tests/city.py](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/tests/test_models/test_city.py) | The unittest module for city |
| `test_place.py` | [tests/place.py](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/tests/test_models/test_place.py) | The unittest module for place |
| `test_review.py` | [tests/review.py](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/tests/test_models/test_review.py) | The unittest module for review |
| `test_state.py` | [tests/state.py](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/tests/test_models/test_state.py) | The unittest module for state |
| `test_user.py` | [tests/user.py](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/tests/test_models/test_user.py) | The unittest module for user |
| `test_file_storage.py` | [tests/test_models/test_engine/test_file_storage.py](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/tests/test_models/test_engine/test_file_storage.py) | The unittest module for file storage |
| `test_db_storage.py` | [tests/test_models/test_engine/test_db_storage.py](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/tests/test_models/test_engine/test_db_storage.py) | The unittest module for DB storage |
| `test_console.py` | [tests/console.py](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/tests/test_console.py) | The unittest module for console |
| `setup_mysql_test.sql` | [setup_mysql_test.sql](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/setup_mysql_test.sql) | Create database and test user |
| `setup_mysql_dev.sql` | [setup_mysql_dev.sql](https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/setup_mysql_dev.sql) | Create database |


### Usage
### Basic usage of The Console

| Command | Usage | Example | Functionality |
| :---: | :---: | :---: | :---: |
| `help` | `help` | help | displays a list of the commands |
| `create` | `create <class>` | create BaseModel | Create a new instance |
| `show` | `show <class> <id>` | show BaseModel 787fds-fdf665-fdf843a1 | Shows a specific instance |
| `destroy` | `destroy <class> <id>` | destroy BaseModel 787fds-fdf665-fdf843a1 | Deletes a specific instance |
| `all` | `all` or `all <class>` | all BaseModel | Shows all instance or class |
| `update` | `update <class> <id> <attribute> <value>` | update BaseModel 787fds-fdf665-fdf843a1 name Maria | Update an attribute in an instance |
| `quit` | `quit` | quit | Quits the console |


### Installation:
```python
$ git clone git@github.com:mfcrespo/AirBnB_clone_v2.git
$ ./console.py
```

# Welcome to Holberton Console
[HBNHB - MySQL](https://youtu.be/fb2zxES7ROU)

#### Follow us

| Authors | GitHub | Twitter | Linkedin |
| :---: | :---: | :---: | :---: |
| Maria Fernanda Crespo | [mfcrespo](https://github.com/mfcrespo) | [@mafe_crespo](https://twitter.com/mafe_crespo) | [mariafernandacrespo](https://www.linkedin.com/in/mariafernandacrespo) |
| David Orejuela | [daorejuela1](https://github.com/daorejuela1) | [DavidOrejuela14](https://twitter.com/DavidOrejuela14) | [davidorejuela14](https://www.linkedin.com/in/davidorejuela14/) |

<p>
<img src="https://github.com/mfcrespo/AirBnB_clone_v2/blob/master/images/DavidOrejuela.jpg" width="20%" height="20%">
</p>

[David Orejuela](https://twitter.com/DavidOrejuela14)

<p>
<img src="https://pbs.twimg.com/profile_images/1116938743968149504/0TQ4K4r3_400x400.jpg" width="20%" height="20%">                                                       
</p>

[Maria Fernanda Crespo](https://twitter.com/mafe_crespo)

##### Holberton School - Foundations - Higher-level programming  AirBnB clone
##### August 13, 2020. Cali, Colombia
