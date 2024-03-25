CREATE DATABASE incubeta_ads;
CREATE USER 'incubeta_ads'@'%' IDENTIFIED BY 'incubeta_ads';
GRANT ALL PRIVILEGES ON incubeta_ads.* TO 'incubeta_ads'@'%';


CREATE TABLE incubeta_ads.fare_prices(
    id INT NOT NULL AUTO_INCREMENT,
    route VARCHAR(15) NOT NULL,
    org_country_code VARCHAR(3) NOT NULL,
    org_country_name VARCHAR(100) NOT NULL,
    org_station_code VARCHAR(5) NOT NULL,
    org_station_code2 VARCHAR(5) NOT NULL,
    org_city_name VARCHAR(100) NOT NULL,
    dst_country_code  VARCHAR(3)NOT NULL,
    dst_country_name  VARCHAR(100)NOT NULL,
    dst_station_code  VARCHAR(5)NOT NULL,
    dst_station_code2 VARCHAR(5) NOT NULL,
    dst_city_name VARCHAR(100) NOT NULL,
    currency_code  VARCHAR(3) NOT NULL,
    lowest_fare_economy_oneway INT NOT NULL DEFAULT 0,
    lowest_fare_premium_oneway INT NOT NULL DEFAULT 0,
    lowest_fare_economy_return INT NOT NULL DEFAULT 0,
    lowest_fare_premium_return INT NOT NULL DEFAULT 0,
    destination_url_economy_oneway VARCHAR(255) NOT NULL,
    destination_url_premium_oneway VARCHAR(255) NOT NULL,
    destination_url_economy_return VARCHAR(255) NOT NULL,
    destination_url_premium_return VARCHAR(255) NOT NULL,
    destination_city_image_url VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);