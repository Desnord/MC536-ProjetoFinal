drop TABLE if EXISTS Voo;
drop TABLE if EXISTS Cidade;

CREATE TABLE Estado
(
  UF VARCHAR(2) NOT NULL,
  Nome VARCHAR(80) NOT NULL,
  PRIMARY KEY (UF)
);

CREATE TABLE Cidade
(
  Nome VARCHAR(80) NOT NULL,
  Estado VARCHAR(2) NOT NULL,
  PRIMARY KEY (Nome,Estado),
  FOREIGN KEY (Estado) REFERENCES Estado(UF)
);

CREATE TABLE Aeroporto
(
  Sigla VARCHAR(4) NOT NULL,
  Descricao VARCHAR(80) NOT NULL,
  Cidade VARCHAR(80) NOT NULL,
  PRIMARY KEY (Sigla),
  FOREIGN KEY (Cidade) REFERENCES Cidade(Nome)
);


CREATE TABLE Voo
(
    VooID int AUTO_INCREMENT NOT NULL,
    Origem varchar(2) NOT NULL,
    Destino varchar(2) NOT NULL,
    Partida datetime NOT NULL,
    Chegada Datetime NOT NULL,
    PRIMARY KEY (VooID),
    FOREIGN KEY (Origem) REFERENCES Aeroporto(Sigla)
    FOREIGN KEY (Destino) REFERENCES Aeroporto(Sigla)
);