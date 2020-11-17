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

RUN apt-get install -y nodejs
RUN apt-get install -y npm

RUN docker-php-ext-install bcmath
RUN docker-php-ext-install ctype
RUN docker-php-ext-install fileinfo
RUN docker-php-ext-install json
RUN docker-php-ext-install mbstring
RUN docker-php-ext-install pdo pdo_mysql
RUN docker-php-ext-install tokenizer
RUN docker-php-ext-install xml

RUN docker-php-ext-install mysqli
RUN docker-php-ext-install pdo 
RUN docker-php-ext-install mysqli 
RUN docker-php-ext-install mysqli pdo_mysql

# Install yarn
RUN npm -g install yarn

# No idea what this does
ENV APACHE_DOCUMENT_ROOT /var/www/authentication/public
RUN sed -ri -e 's!/var/www/html!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/sites-available/*.conf
RUN sed -ri -e 's!/var/www/!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/apache2.conf /etc/apache2/conf-available/*.conf

RUN a2enmod rewrite

# Get composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

COPY . /var/www/