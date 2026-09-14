-- ===============================
--      BANCO DE DADOS HERO MANAGER
-- ===============================

CREATE DATABASE IF NOT EXISTS heromanager CHARACTER SET utf8mb4;
USE heromanager;

-- ===============================
--      TABELA USUARIO
-- ===============================
CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    cpf VARCHAR(20) UNIQUE,
    senha VARCHAR(255),
    planeta VARCHAR(50)
);

-- ===============================
--      TABELA CLASSE
-- ===============================
CREATE TABLE classe (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50)
);

-- ===============================
--      TABELA HEROI
-- ===============================
CREATE TABLE heroi (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    classe_id INT,
    nivel INT,
    imagem_url VARCHAR(255),
    habilidades TEXT,
    forca INT,
    defesa INT,
    velocidade INT,
    descricao TEXT,
    FOREIGN KEY (classe_id) REFERENCES classe(id)
);

-- ===============================
--      TABELA USUARIO_HEROI
-- ===============================
CREATE TABLE usuario_heroi (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    heroi_id INT,
    local ENUM('equipe','base'),
    FOREIGN KEY (usuario_id) REFERENCES usuario(id),
    FOREIGN KEY (heroi_id) REFERENCES heroi(id)
);

-- ===============================
--      INSERIR CLASSES PADRÃO
-- ===============================
INSERT INTO classe (nome) VALUES 
('Guerreiro'),
('Mago'),
('Arqueiro'),
('Assassino'),
('Tanque'),
('Curandeiro');

-- ===============================
--      INSERIR HERÓIS PADRÃO
-- ===============================
INSERT INTO heroi (nome, classe_id, nivel, imagem_url, habilidades, forca, defesa, velocidade, descricao) VALUES
('Astra', 2, 12, 'astra.png', 'Magia Arcana, Orbe Estelar, Teleporte', 80, 40, 60, 'Uma maga ancestral capaz de manipular energias cósmicas.'),
('Ragnar', 1, 15, 'ragnar.png', 'Golpe Brutal, Fúria do Berserker', 95, 60, 30, 'Guerreiro lendário conhecido por sua força descomunal.'),
('Lyra', 3, 10, 'lyra.png', 'Tiro Preciso, Flecha Elemental', 70, 35, 85, 'Arqueira capaz de canalizar elementos em suas flechas.'),
('Shade', 4, 14, 'shade.png', 'Ataque Sombrio, Invisibilidade', 75, 30, 95, 'Assassino silencioso que atua nas sombras.'),
('Titanus', 5, 18, 'titanus.png', 'Escudo de Pedra, Provocação', 60, 100, 20, 'Tanque impenetrável formado por rochas místicas.'),
('Elowen', 6, 13, 'elowen.png', 'Cura Divina, Barreira Sagrada', 40, 50, 45, 'Curandeira que utiliza a energia vital da floresta.'),
('Draven', 1, 16, 'draven.png', 'Corte Flamejante, Grito de Guerra', 90, 55, 40, 'Espadachim que domina chamas.'),
('Seraphine', 2, 11, 'seraphine.png', 'Feitiço Glacial, Encanto', 65, 50, 50, 'Feiticeira com poderes de gelo e manipulação mental.'),
('Falkor', 3, 9, 'falkor.png', 'Rajada Tripla, Visão de Águia', 72, 40, 82, 'Arqueiro treinado por criaturas celestiais.'),
('Nyx', 4, 17, 'nyx.png', 'Golpe Fantasma, Veneno Sombrio', 78, 35, 92, 'Assassina ágil que controla sombras tóxicas.'),
('Bolder', 5, 20, 'bolder.png', 'Muralha Viva, Impacto Sísmico', 50, 120, 15, 'Tanque gigante capaz de causar terremotos.'),
('Lumina', 6, 15, 'lumina.png', 'Luz Purificadora, Ressurreição', 45, 55, 55, 'Sacerdotisa que utiliza magia luminosa.'),
('Gromm', 1, 19, 'gromm.png', 'Martelo Titânico, Pele de Ferra', 98, 70, 25, 'Guerreiro que empunha um martelo sagrado.'),
('Valyria', 2, 14, 'valyria.png', 'Tempestade Arcana, Controle Elemental', 85, 45, 60, 'Maga prodígio com domínio elemental.'),
('Rowan', 3, 13, 'rowan.png', 'Flecha Fantasma, Armadilha Natural', 68, 38, 88, 'Caçador da floresta com precisão mortal.'),
('Kairo', 4, 11, 'kairo.png', 'Lâmina Sangrenta, Passo Sombrio', 74, 32, 97, 'Assassino veloz que utiliza técnicas proibidas.'),
('Ironhide', 5, 18, 'ironhide.png', 'Pele de Aço, Investida', 55, 110, 22, 'Tanque revestido por armadura viva.'),
('Sael', 6, 12, 'sael.png', 'Cura Ancestral, Escudo Espiritual', 42, 60, 48, 'Xamã com poderes milenares.'),
('Thoran', 1, 17, 'thoran.png', 'Espada do Trovão, Rugido Celeste', 92, 58, 35, 'Guerreiro guardião das tempestades.'),
('Myrra', 2, 16, 'myrra.png', 'Feitiço Lunar, Ilusão Prateada', 83, 47, 62, 'Maga lunar que cria ilusões poderosas.'),
('Eldrin', 3, 15, 'eldrin.png', 'Tiro Solar, Fuga Acrobática', 76, 42, 86, 'Arqueiro que domina energia solar.'),
('Stryke', 4, 13, 'stryke.png', 'Lâmina Rápida, Veneno Imediato', 73, 34, 98, 'Assassino especialista em venenos.'),
('Juggar', 5, 21, 'juggar.png', 'Escudo Montanha, Choque Terrestre', 52, 125, 18, 'Tanque colossal.'),
('Melian', 6, 14, 'melian.png', 'Graça Divina, Flor Revigorante', 38, 58, 52, 'Curandeira que controla energia floral.'),
('Volrak', 1, 18, 'volrak.png', 'Lâmina Sombria, Fúria Demoníaca', 96, 53, 34, 'Guerreiro corrompido por energia sombria.'),
('Cordelia', 2, 13, 'cordelia.png', 'Feitiço Aquático, Hidroexplosão', 75, 48, 58, 'Maga do reino submerso.'),
('Ilyas', 3, 12, 'ilyas.png', 'Flecha de Gelo, Armadilha Congelante', 69, 37, 80, 'Arqueiro que utiliza magia de gelo.'),
('Raven', 4, 16, 'raven.png', 'Golpe Fatal, Sombras Cortantes', 79, 33, 94, 'Assassina mortal.'),
('Granitus', 5, 22, 'granitus.png', 'Escudo Absoluto, Queda Rochosa', 57, 130, 19, 'Tanque ancestral de rocha viva.'),
('Seris', 6, 17, 'seris.png', 'Benção Divina, Harmonizar', 41, 62, 50, 'Curandeira celestial.');