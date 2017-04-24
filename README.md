# django_citus
A sample django project over a distributed Postgres using Citus


## Run the dockerized project
### Prepare the five workers for the citus cluster
`docker-compose -p citus scale worker=5`
### Run the container
`docker-compose up`

## Distribute your table
1. `docker exec -it citus_master psql -U postgres`
2. `SELECT create_distributed_table('reviews_review', 'id');`

## Feed the DB with data using your django models
1. `docker exec -it citus_web_1 bash`
2. `./manage.py shell`
2. `from reviews.models import Review`
3. `for i in range(Review.objects.count(), Review.objects.count()+100): Review.objects.create(id=i)`


### Querry the DB
*   Using djnago shell
	1. `Review.objects.all().count()`
*   Using the master node
	1.  `docker exec -it citus_master psql -U postgres`
	2.  `select count(*) from reviews_review;`
