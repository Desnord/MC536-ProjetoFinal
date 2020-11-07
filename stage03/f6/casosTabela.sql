CREATE TABLE Casos
( 
  Estado VARCHAR(80) NOT NULL,
  Ano INTEGER NOT NULL, 
  Semana INTEGER NOT NULL,
  NumCasos INTEGER NOT NULL,
  PRIMARY KEY (Estado,Ano,Semana),
  FOREIGN KEY (Estado) REFERENCES Estado(Nome)
);