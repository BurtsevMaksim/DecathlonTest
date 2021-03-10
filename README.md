# DecathlonTest
Testing task with Django+REST+Docker

To build:

    cd /project_folder
    sudo docker-compose build
    sudo docker-compose up 
Application will be available on http://127.0.0.1:8000 

Username:maksim Password:1

To upload athletes through cls go http://127.0.0.1:8000/uploads/athlete/
To GET list of all athletes go http://127.0.0.1:8000/athletes/
All standart REST methods are also supported
Decathlon.pdf is a required algorithm chart
