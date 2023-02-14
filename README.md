Deprem.Market
=================

Deprem.Market is a RESTful API that enables people to offer what they have and request what they need in case of earthquakes. It is designed to facilitate a collective effort to help one another during an earthquake disaster.

```
Please note that Deprem.Market is an alpha software, which means that it is currently in a very early stage of development. While some parts of the application have been completed, there are still many features that need to be added. As such, the software is not yet ready for production use. We appreciate your interest and support and we welcome any feedback or suggestions you may have as we continue to improve and expand the functionality of the application.

We urgently need to build a frontend for the API. 
```

Installation
------------

1.  Make sure you have [Docker](https://www.docker.com/) installed.
2.  Clone this repository to your local machine.
3.  Create a `.env` file based on the `api/.env.example` file, and update the values to match your environment.
4.  In the project root directory, run the following command to start the Docker containers: `docker-compose up -d`.
5.  Optionally run the following command to update the database schema: `docker-compose run --rm api python manage.py migrate`. You can find the automated version of this in the api/scripts/entrypoint.sh file.
6.  Optionally create a superuser account by running the following command and following the prompts: `docker-compose run --rm api python manage.py createsuperuser`. You can find the automated version of this in the api/scripts/entrypoint.sh file.

Usage
-----

After installation, you can access the API through the following endpoints:

- `/api/v1/auth/`: This endpoint provides user authentication and authorization. Users can obtain a JWT token by providing their credentials. 
  - `/api/v1/auth/token/`
  - `/api/v1/auth/token/verify/`
  - `/api/v1/auth/token/refresh/`
- `/api/v1/users/`: This endpoint allows admins to manage accounts, and users to register new accounts using the registration action:
  - `/api/v1/users/register/`: Registration action
- `/api/v1/listings/`: This endpoint allows users to create new listings (offer or request) and view existing ones.
- `/api/v1/categories/`: This endpoint allows users to view existing categories, and allows admins to create new categories and update existing ones.
*   `/admin/`: This is the admin panel for managing all content.

The API is also **browsable**, allowing for easy exploration and testing of the endpoints.

Tech Stack
----------

*   Django: Python web framework used for building the API.
*   Nginx: High-performance web server used as a reverse proxy to handle client requests.
*   PostgreSQL: Relational database management system used for storing data.
*   Redis: In-memory data structure store used for caching and handling real-time data.
*   JWT: Token-based authentication and authorization method used for securing API endpoints.

Contributing
------------

If you would like to contribute to this project, please follow these steps:

1.  Fork this repository.
2.  Create a new branch with a descriptive name (`feature/new-endpoint`).
3.  Make your changes.
4.  Run tests: `docker-compose run --rm api python manage.py test`
5.  Commit your changes with a clear and concise message.
6.  Push your changes to your forked repository.
7.  Create a pull request and describe your changes.

**Important Notice:**  

This project is intended to be a community-driven initiative. It is not meant to be owned by a single individual but rather to be a collaborative effort where everyone is encouraged to contribute. Given the urgent need to prepare for earthquakes and other natural disasters, it is crucial that we work together to build effective tools to help those in need. As an earthquake victim myself, I may not have sufficient time to maintain this project alone. Therefore, interested individuals and organizations are encouraged to step forward and help move this project to a community organization where it can continue to be developed and maintained with the help of everyone's support and contributions.

In my research on earthquake-related projects, I noticed that very few people are using Django and Python for such initiatives. As a result, I believe there is a significant opportunity for Python developers to get involved in a meaningful and impactful way by contributing to this project. Not only will this project help those affected by earthquakes, but it will also enable Python developers to channel their skills and expertise towards a socially valuable cause. By building a strong community around such projects, we can work together to make a meaningful impact and help those who need it most.

License
-------

This project is licensed under the GPL-3.0 License. See the [LICENSE](LICENSE) file for more information.

