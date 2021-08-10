PRAGMA foreign_keys = ON;

CREATE TABLE loterias (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT NOT NULL,
	numero_concurso TEXT NOT NULL, 
    data_concurso TEXT NOT NULL, 
    data_concurso_milliseconds TEXT NOT NULL, 
    local_realizacao TEXT NOT NULL, 
    rateio_processamento DECIMAL NOT NULL, 
    acumulou TEXT NOT NULL, 
    valor_acumulado DECIMAL NOT NULL, 
    arrecadacao_total DECIMAL NOT NULL, 
    data_proximo_concurso TEXT NOT NULL, 
    data_proximo_concurso_milliseconds TEXT NOT NULL, 
    valor_estimado_proximo_concurso DECIMAL NOT NULL, 
    valor_final_concurso_acumulado DECIMAL NOT NULL, 
    numero_final_concurso_acumulado DECIMAL NOT NULL, 
    valor_acumulado_especial DECIMAL NOT NULL, 
    nome_acumulado_especial TEXT NOT NULL
    FOREIGN KEY(dezena_id) REFERENCES dezenas(id) ON DELETE CASCADE
    FOREIGN KEY(premiacao_id) REFERENCES premiacao(id) ON DELETE CASCADE
    FOREIGN KEY(local_ganhadores_id) REFERENCES local_ganhadores(id) ON DELETE CASCADE
);

CREATE TABLE dezenas (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
    numero_concurso TEXT NOT NULL, 
	dezena INTEGER NOT NULL,
);

CREATE TABLE premiacao (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL, 
    numero_concurso TEXT NOT NULL, 
    quantidade_ganhadores INTEGER NOT NULL, 
    valor_total DECIMAL NOT NULL, 
    acertos INTEGER NOT NULL,

);

CREATE TABLE local_ganhadores (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
    numero_concurso TEXT NOT NULL, 
    local TEXT NOT NULL, 
    cidade TEXT NOT NULL, 
    uf TEXT NOT NULL, 
    quantidade_ganhadores INTEGER NOT NULL, 
    canal_eletronico TEXT NOT NULL,

);