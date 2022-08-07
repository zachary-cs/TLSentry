# TLSentry
Finally, an open source web app to monitor your websites!


# Modules

## Network Scanner
* Checks endpoints for SSL Certificate Data

## Scheduler
Creates, verifies, and saves Schedule records. These are crontab format entries.

## Reporter
Checks for expiring Certificates on a schedule, posts messages to the Webapp, and emails admins of those Certificates.

## Database Connector
Connection to the Database. Runs queries, returns results, and manages DB state.


# Models

## Endpoints
A simple Hostname and Port is all you need to define an endpoint. This represents one IP address, which could be an external or internal network interface of your service.

## Certificate
SSL Certificates gathered by the scanner subsystem. These are collected by the scanner process when an endpoint is entered, and also checked periodically based on a user defined schedule.

## Schedules
Crontab schedules, which simply define how often certificate checks should be running

# Application Flow

* Endpoint entered into the system
* Scanner module obtains the IP address, SSL Certificate, etc from the Endpoint
* Scanner checks if the SSL Certificate exists in the DB already
* * If so, link the endpoint to that certificate
* * If not, create new Certificate entry, and link to that
* More to come soon!


# Server install

TODO
## Prerequisites
Install them with `pip3 install -r requirements.txt`


