CREATE TABLE dados_trimestrais (
    DATA DATE,
    REG_ANS VARCHAR(255),
    CD_CONTA_CONTABIL VARCHAR(255),
    DESCRICAO TEXT,
    VL_SALDO_INICIAL TEXT,
    VL_SALDO_FINAL TEXT
);


COPY dados_trimestrais(DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, VL_SALDO_INICIAL, VL_SALDO_FINAL)
FROM '/tmp/1T2023.csv'
DELIMITER ';'
CSV HEADER;

COPY dados_trimestrais(DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, VL_SALDO_INICIAL, VL_SALDO_FINAL)
FROM '/tmp/2T2023.csv'
DELIMITER ';'
CSV HEADER;

COPY dados_trimestrais(DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, VL_SALDO_INICIAL, VL_SALDO_FINAL)
FROM '/tmp/3T2023.csv'
DELIMITER ';'
CSV HEADER;

COPY dados_trimestrais(DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, VL_SALDO_INICIAL, VL_SALDO_FINAL)
FROM '/tmp/4T2023.csv'
DELIMITER ';'
CSV HEADER;

COPY dados_trimestrais(DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, VL_SALDO_INICIAL, VL_SALDO_FINAL)
FROM '/tmp/1T2024.csv'
DELIMITER ';'
CSV HEADER;

COPY dados_trimestrais(DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, VL_SALDO_INICIAL, VL_SALDO_FINAL)
FROM '/tmp/2T2024.csv'
DELIMITER ';'
CSV HEADER;

COPY dados_trimestrais(DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, VL_SALDO_INICIAL, VL_SALDO_FINAL)
FROM '/tmp/3T2024.csv'
DELIMITER ';'
CSV HEADER;

COPY dados_trimestrais(DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, VL_SALDO_INICIAL, VL_SALDO_FINAL)
FROM '/tmp/4T2024.csv'
DELIMITER ';'
CSV HEADER;


UPDATE dados_trimestrais
SET vl_saldo_inicial = to_number(replace(vl_saldo_inicial, ',', '.'), '9999999999999.99'),
    vl_saldo_final = to_number(replace(vl_saldo_final, ',', '.'), '9999999999999.99');
    
ALTER TABLE dados_trimestrais
ALTER COLUMN vl_saldo_inicial TYPE NUMERIC USING vl_saldo_inicial::numeric;

ALTER TABLE dados_trimestrais
ALTER COLUMN vl_saldo_final TYPE NUMERIC USING vl_saldo_final::numeric;



CREATE TABLE operadoras_saude (
    Registro_ANS VARCHAR(255),
    CNPJ VARCHAR(14),
    Razao_Social TEXT,
    Nome_Fantasia TEXT,
    Modalidade VARCHAR(255),
    Logradouro TEXT,
    Numero VARCHAR(255),
    Complemento TEXT,
    Bairro TEXT,
    Cidade VARCHAR(255),
    UF VARCHAR(2),
    CEP VARCHAR(8),
    DDD VARCHAR(3),
    Telefone VARCHAR(20),
    Fax VARCHAR(20),
    Endereco_eletronico VARCHAR(255),
    Representante TEXT,
    Cargo_Representante TEXT,
    Regiao_de_Comercializacao INTEGER,
    Data_Registro_ANS DATE
);

COPY operadoras_saude(Registro_ANS, CNPJ, Razao_Social, Nome_Fantasia, Modalidade, Logradouro, Numero, Complemento, Bairro, Cidade, UF, CEP, DDD, Telefone, Fax, Endereco_eletronico, Representante, Cargo_Representante, Regiao_de_Comercializacao, Data_Registro_ANS)
FROM '/tmp/Relatorio_cadop.csv'
DELIMITER ';'
CSV HEADER;



-- Quais as 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OUAVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre?

SELECT
    os.Razao_Social,
    SUM(dt.VL_SALDO_FINAL) AS Total_Despesas
FROM
    public.operadoras_saude os
JOIN
    public.dados_trimestrais dt ON os.Registro_ANS = dt.REG_ANS
WHERE
    dt.DESCRICAO = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
    AND dt.DATA >= (SELECT MAX(DATA) FROM public.dados_trimestrais) - INTERVAL '3 months'
GROUP BY
    os.Razao_Social
ORDER BY
    Total_Despesas DESC
LIMIT 10;

-- Quais as 10 operadoras com maiores despesas nessa categoria no último ano?

SELECT
    os.Razao_Social,
    SUM(dt.VL_SALDO_FINAL) AS Total_Despesas
FROM
    public.operadoras_saude os
JOIN
    public.dados_trimestrais dt ON os.Registro_ANS = dt.REG_ANS
WHERE
    dt.DESCRICAO = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
    AND dt.DATA >= (SELECT MAX(DATA) FROM public.dados_trimestrais) - INTERVAL '1 year'
GROUP BY
    os.Razao_Social
ORDER BY
    Total_Despesas DESC
LIMIT 10;
