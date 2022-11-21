# Avangard

## Prerequisites

To build project and start development on host machine must be installed Linux (recommended) or MacOS and some required software:
latest version of `Docker (version 18.06.0+)` [https://docs.docker.com/install/]
and `docker-compose` [https://docs.docker.com/compose/compose-file/],
`Git`, and `Python 3.8+`.

## Installation

You should run commands below to install application correctly:

        docker-compose up --build

Next you can check services status:

        docker-compose ps

Default port mapping (see `.env` file):

        Name                             Command                     State                                      Ports                  
    ------------------------------------------------------------------------------------------------------------------------------------------
    rocketdata_2_celery_1     sh ./entrypoint_celery.sh              Up             0.0.0.0:5555->5555/tcp,:::5555->5555/tcp
    rocketdata_2_db_1         docker-entrypoint.sh postgres          Up             5432/tcp
    rocketdata_2_rabbit_1     docker-entrypoint.sh rabbi ...         Up             15671/tcp, 0.0.0.0:15672->15672/tcp,:::15672->15672/tcp,      
                                                                                    15691/tcp, 15692/tcp, 25672/tcp, 4369/tcp, 5671/tcp,          
                                                                                    0.0.0.0:5672->5672/tcp,:::5672->5672/tcp
    rocketdata_2_web_1        sh ./entrypoint.sh                     Up             0.0.0.0:8000->8000/tcp,:::8000->8000/tcp 