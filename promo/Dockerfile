FROM php:7.4-apache

RUN apt-get update -y
RUN apt-get upgrade -y

RUN apt-get install -y libonig-dev
RUN apt-get install -y libxml2-dev

RUN apt-get install -y zip 
RUN apt-get install -y curl
RUN apt-get install -y unzip 
RUN apt-get install -y git
RUN apt-get install -y nano 

RUN a2enmod rewrite

COPY . /var/www/html/