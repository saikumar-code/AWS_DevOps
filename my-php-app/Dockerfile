# Use Nginx image from Docker Hub
FROM nginx:latest

# Install PHP and supervisor
RUN apt-get update && apt-get install -y php-fpm php-mysql

# Remove the default server definition
RUN rm /etc/nginx/conf.d/default.conf

# Copy custom Nginx config
COPY default.conf /etc/nginx/conf.d/

# Copy PHP script
COPY index.php /usr/share/nginx/html/index.php

# Expose port 80
EXPOSE 80

# Start Nginx and PHP-FPM on container startup
CMD service php7.4-fpm start && nginx -g 'daemon off;'
