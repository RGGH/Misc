## Adding a new Database

    sudo mysql -u root -p -h localhost

    DROP DATABASE IF EXISTS newz;
    CREATE DATABASE newz;

    GRANT ALL PRIVILEGES ON newz.* TO 'pi'@'localhost';

    FLUSH PRIVILEGES;
