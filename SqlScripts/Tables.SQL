DROP DATABASE IF EXISTS FastFood;

CREATE DATABASE FastFood;

USE FastFood;
 
CREATE TABLE `login`(
    user_id VARCHAR(10) NOT NULL,
    password_hash VARCHAR(64) NOT NULL
);


CREATE TABLE  `user`(
    `user_id` VARCHAR(10) NOT NULL,
    `user_name` VARCHAR(50) NOT NULL,
    `email` VARCHAR(100) NOT NULL,
    `phone` VARCHAR(10),
    `user_role` INT(1) NOT NULL,
    PRIMARY KEY (`user_id`)
);

CREATE TABLE `owns`(
    `admin_id` VARCHAR(10) NOT NULL,
    `shop_id` VARCHAR(10) NOT NULL
);

CREATE TABLE `works_for`(
    `chef_id` VARCHAR(10),
    `shop_id` VARCHAR(10)
);


CREATE TABLE `chef_orders`(
    `chef_id` VARCHAR(10) NOT NULL,
    `oder_id` VARCHAR(10) NOT NULL
);


CREATE TABLE `shop`(
    `shop_id` VARCHAR(10) NOT NULL,
    `location` VARCHAR(10) NOT NULL,
    `shop_name` VARCHAR (20) NOT NULL,
    `shop_description` VARCHAR(100),
    PRIMARY KEY(`shop_id`)
);



CREATE TABLE `payments`(
    `payment_id` VARCHAR(10) NOT NULL,
    `user_id` VARCHAR(10) NOT NULL,
    `shop_id` VARCHAR(10) NOT NULL,
    `amount` INT(4) NOT NULL,
    `order_id` VARCHAR(10) NOT NULL,
    `status` INT(1) NOT NULL,
    PRIMARY KEY(`payment_id`)
);



CREATE TABLE `order`(
    `order_id` VARCHAR(10) NOT NULL,
    `user_id` VARCHAR(10) NOT NULL,
    `order_status` INT(1) NOT NULL,
    `notes` VARCHAR(100),
    `order_date` DATE NOT NULL,
    `order_time` TIME NOT NULL,
    `delivery_date` DATE NOT NULL,
    `delivery_time` TIME NOT NULL,
    `payment_id` NOT NULL,
    PRIMARY KEY(`order_id`)
);


CREATE TABLE `order_items`(
    `order_id` VARCHAR(10) NOT NULL,
    `food_item_id` VARCHAR(10) NOT NULL,
    `item_count` INT(2) NOT NULL
);


CREATE TABLE `food_item`(
    `item_id` VARCHAR(10) NOT NULL,
    `shop_id` VARCHAR(10) NOT NULL,
    `price` FLOAT(4) NOT NULL,
    `name` CHAR(50) NOT NULL,
    `status` INT(1) NOT NULL,
    `image_url` VARCHAR(100) NOT NULL,
    `category` CHAR(50),
    PRIMARY KEY(`item_id`)
);


CREATE TABLE `off_days`(
    `shop_id` VARCHAR(10) NOT NULL,
    `date`  DATE NOT NULL,
    `start_time` TIME NOT NULL,
    `end_time` TIME NOT NULL,
    PRIMARY KEY(`shop_id`)
);