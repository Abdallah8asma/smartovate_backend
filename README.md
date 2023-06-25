
# Caustaza

Welcome to Caustaza! This is a Django project containing the basic setup for now.

## Environment Setup

To set up your development environment, please follow these steps:

1. Clone the repository:

   ```bash
   git clone https://gitlab.com/caustaza_group/caustaza_backend.git` 

2.  Navigate to the `caustaza_backend` directory:
        
    `cd caustaza_backend` 
    
3.  Create a virtual environment (optional but recommended):
        
    `python3 -m venv env
    source env/bin/activate` 
    
4.  Install the dependencies:
        
    `pip install -r requirements.txt` 
    
5.  Ensure you have PostgreSQL 15 installed and running.
    

## Running the Project

To run the Caustaza project, follow these steps:

1.  Navigate to the root project directory:
        
    `cd caustaza` 
    
2.  Activate the virtual environment if you created one:
        
    `source ../env/bin/activate` 


3.  Follow the .example.env and create your own with the name : `.env`
        

4.  Run the Django necessary migrations:
        
    `python caustaza/manage.py migrate` 

5.  Run the Django development server:
        
    `python caustaza/manage.py runserver` 
    
    The server will start running locally at `http://localhost:8000/`.
    

## Contributing

We welcome contributions to Caustaza! If you'd like to contribute, please follow these steps:

1.  Clone the repository.
    
2.  Create a new branch for your feature or bug fix:
        
    `git checkout -b feature/new-feature` 
    
    Replace `feature/new-feature` with an appropriate name for your branch.
    
3.  Make your changes and commit them.
    
4.  Push your changes to your forked repository:
        
    `git push origin feature/new-feature` 
    
5.  Open a pull request against the `dev` branch of the original repository.
    
6.  Provide a detailed description of your changes and any relevant information.
    
7.  Wait for a code review and address any feedback.

## Dockerizing

 ### Rerequisites
Docker and Docker Compose should be installed on your machine.
 ### Steps to follow 
1. Navigate to the project directory:

  `cd caustaza_backend/caustaza` 

3. Build and Start the Containers

Run the following command to build and start the containers using Docker Compose:

  `docker-compose up --build` 

This command will build the necessary Docker images and start the containers defined in the docker-compose.yml file.

4. Access the Django Container Interface

Open your web browser and enter the following URL:

  'http://localhost:8000'

This will take you to the interface of your Django application running inside the Docker container.

5. Access the pgAdmin Interface

Open your web browser and enter the following URL:

  'http://localhost:5050'

This will open the pgAdmin interface, which allows you to manage and interact with the PostgreSQL database container.

That's it! You should now be able to access the Django container interface at http://localhost:8000 and the pgAdmin interface at http://localhost:5050 while running the application inside Docker containers.