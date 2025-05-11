# Building a Multi-tenant App with Django

## Want to learn how to build this?

Check out the [post](#).

## Want to use this project?

1. Fork/Clone

1. Spin up a [PostgreSQL](https://www.postgresql.org/) database using Docker:

   ```sh
   $ docker run --name sprinty-postgres -p 5432:5432 \
       -e POSTGRES_USER=sprinty -e POSTGRES_PASSWORD=complexpassword123 \
       -e POSTGRES_DB=sprinty -d postgres
   ```

1. Populate the database:
   
   ```sh
   $ python manage.py populate_db
   ```

1. Your tenants should be accessible at the following URLs:

   - `public`: [http://localhost:8000/api/](http://localhost:8000/api/)
   - `demo1`: [http://demo1.localhost:8000/api/](http://demo1.localhost:8000/api/) 
   - `demo2`: [http://demo2.localhost:8000/api/](http://demo2.localhost:8000/api/)

1. Tenant information including admin credentials, can be found in *[tenants.json](https://github.com/duplxey/django-multi-tenant/blob/master/tenants/data/tenants.json)* file.
