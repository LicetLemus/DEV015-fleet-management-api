CREATE TABLE taxis (
    id INT PRIMARY KEY NOT NULL,
    plate VARCHAR(10)
);

CREATE TABLE trajectories (
    id SERIAL PRIMARY KEY,
    taxi_id INT,
    date TIMESTAMP,
    latitude FLOAT,
    longitude FLOAT,
    FOREIGN KEY (taxi_id) REFERENCES taxis(id)
);


SELECT * FROM trajectories;
SELECT * FROM taxis; 

SELECT taxi_id, date FROM trajectories WHERE latitude = 116.34386 and longitude = 39.8967;
