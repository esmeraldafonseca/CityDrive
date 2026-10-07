CREATE DATABASE IF NOT EXISTS citydrive CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE citydrive;

CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    telefone VARCHAR(30) NOT NULL
);

CREATE TABLE estacoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    morada VARCHAR(200) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    hora_abertura TIME NOT NULL,
    hora_fecho TIME NOT NULL,
    ativa BOOLEAN NOT NULL DEFAULT TRUE,
    CONSTRAINT chk_estacao_horario CHECK (hora_abertura < hora_fecho)
);

CREATE TABLE categorias_viatura (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL UNIQUE,
    descricao VARCHAR(255)
);

CREATE TABLE viaturas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    matricula VARCHAR(20) NOT NULL UNIQUE,
    marca VARCHAR(50) NOT NULL,
    modelo VARCHAR(50) NOT NULL,
    categoria_id INT NOT NULL,
    ano SMALLINT NOT NULL,
    estacao_id INT NOT NULL,
    ativa BOOLEAN NOT NULL DEFAULT TRUE,
    CONSTRAINT fk_viatura_categoria FOREIGN KEY (categoria_id) REFERENCES categorias_viatura(id),
    CONSTRAINT fk_viatura_estacao FOREIGN KEY (estacao_id) REFERENCES estacoes(id),
    CONSTRAINT chk_viatura_ano CHECK (ano >= 1900)
);

CREATE TABLE reservas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT NOT NULL,
    viatura_id INT NOT NULL,
    inicio DATETIME NOT NULL,
    fim DATETIME NOT NULL,
    estado VARCHAR(20) NOT NULL DEFAULT 'CONFIRMADA',
    criada_em DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_estacoes_cidade ON estacoes(cidade);
CREATE INDEX idx_viaturas_estacao ON viaturas(estacao_id);
CREATE INDEX idx_reservas_viatura_periodo ON reservas(viatura_id, inicio, fim);
CREATE INDEX idx_reservas_cliente ON reservas(cliente_id);
