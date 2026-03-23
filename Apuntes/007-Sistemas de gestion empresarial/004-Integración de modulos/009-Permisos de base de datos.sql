CREATE USER 
'microtienda'@'localhost' 
IDENTIFIED  BY 'Microtienda123$';


GRANT USAGE ON *.* TO 'microtienda'@'localhost';

ALTER USER 'microtienda'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON microtienda.* 
TO 'microtienda'@'localhost';


FLUSH PRIVILEGES;
