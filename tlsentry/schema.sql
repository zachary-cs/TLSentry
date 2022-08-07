DROP TABLE IF EXISTS tlsentry.certificates;
DROP TABLE IF EXISTS tlsentry.endpoints;

CREATE TABLE tlsentry.certificates (
	ID INT auto_increment NOT NULL,
	common_name VARCHAR(100) NOT NULL,
	peer_name varchar(100) NULL,
	alt_names VARCHAR(100) NULL,
	issuer VARCHAR(100) NOT NULL,
	not_before DATETIME NOT NULL,
	not_after DATETIME NOT NULL,
	thumbprint VARCHAR(100) NOT NULL,
	CONSTRAINT certificates_PK PRIMARY KEY (ID)
)

CREATE TABLE tlsentry.endpoints (
  id INT auto_increment NOT NULL,
  hostname varchar(100) NOT NULL,
  ip_addr varchar(100) NOT NULL,
  port INT NOT NULL,
  discovered DATETIME NOT NULL,
  last_scanned DATETIME NULL,
  cert_id INTEGER NOT NULL,
	CONSTRAINT certificates_PK PRIMARY KEY (ID),
  CONSTRAINT endpoints_FK FOREIGN KEY (id) REFERENCES tlsentry.certificates(id)
);