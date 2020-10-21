FROM php:7.4-apache

WORKDIR /var/www/html

RUN apt-get update -y
RUN apt-get upgrade -y

RUN apt-get install -y libonig-dev
RUN apt-get install -y libxml2-dev

RUN apt-get install -y zip 
RUN apt-get install -y curl
RUN apt-get install -y unzip 
RUN apt-get install -y git
RUN apt-get install -y nano 

RUN docker-php-ext-install bcmath
RUN docker-php-ext-install ctype
RUN docker-php-ext-install fileinfo
RUN docker-php-ext-install json
RUN docker-php-ext-install mbstring
RUN docker-php-ext-install pdo
RUN docker-php-ext-install tokenizer
RUN docker-php-ext-install xml

# Get composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

COPY . .