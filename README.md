# fb_freinds
This application allows user to register via facebook end save user friens names on table UserFriends.

To start the application:
# Install mysql:
 ```bash
 sudo apt-get install python-dev mysql-server libmysqlclient-dev
 ```
 
# Create database
```bash
mysql -u root -p
CREATE DATABASE fbusers CHARACTER SET UTF8;
CREATE USER djangoadmin@localhost IDENTIFIED BY '52044Inn';
GRANT ALL PRIVILEGES ON djangoadmin.* TO fbusers@localhost;
FLUSH PRIVILEGES;
exit
```

# Install requirements
```python
sudo pip install -r requiremets.txt
```

# Perform migration
```python
python manage.py makemigrations
python manage.py migrate
```

# Start
```python
python manage.py runserver
```
