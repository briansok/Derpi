# Derpi

## Installation

For the installation of Derpi you first need all the dependencies installed. For the the webserver we use Daphne and Nginx as a reverse proxy. 
To manage all the processes we created a supervisor to log all data and status. 

## Apps

* Sensors
* Categories 
* Controllers 
* Notifications

## Dependencies

- Django
- Daphne
- Nginx
- Pygments
- Django Rest Framework
- Markdown
- Django-filter
- Channels
- Asgi_redis
- Mysqlclient
- Django-websocket-redis
- Luatool
- Esptool
- Superivord

## Configs

All configs can be found in the "configs" folder. Including the supervisor

## Usage

Webserver start 

`sudo service nginx start`

`supervisorctl start worker`

`supervisorctl start daphne`

`redis-server`


Create migrations

`python manage.py makemigrations app`

`python manage.py migrate`


Start development server

`python manage.py runserver`


Create Admin User

`python manage.py createsuperuser`



Flasing Nodemcu

`./esptool.py --port /dev/ttyUSB0  write_flash --flash_mode dio 0x00000 nodemcu-master-8-modules-2017-03-20-13-38-04-integer.bin`

`./luatool.py --port /dev/ttyUSB0 --src main.lua --dest main.lua --verbose`

## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## Credits
Sytze Koster, Brian Sok

## License
Opensource biatch
