# Docker Airflow container
*** download aifrflow docker-compose.yml *** `curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.0.1/docker-compose.yaml'`

**create app directories**<br>
`mkdir ./dags ./logs ./plugins`

**save configuration to env file**<br>
`mkdir ./dags ./logs ./plugins`

**initialize app**
`docker-compose up airflow-init`

**run containers**
`docker compose up` add `-d` to run in detach mode

**access airflow web interface**
`http://localhost:8080`
- login:`airflow`
- password:`airflow`