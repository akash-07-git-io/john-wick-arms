FROM php:8.2-apache

# Install mysqli & pdo_mysql extensions
RUN docker-php-ext-install mysqli pdo pdo_mysql && docker-php-ext-enable mysqli pdo_mysql

# Enable apache rewrite
RUN a2enmod rewrite

# Copy project files into webroot
COPY . /var/www/html/

# Set proper permissions
RUN chown -R www-data:www-data /var/www/html

EXPOSE 80
CMD ["apache2-foreground"]
