sudo python3 manage.py runserver 192.168.0.107:80 &> ./logging/django_logger.log &
celery -A temp_website worker -l info -n worker1 &> ./logging/celery_worker1_logger.log &
celery -A temp_website worker -l info -n worker2 &> ./logging/celery_worker2_logger.log &