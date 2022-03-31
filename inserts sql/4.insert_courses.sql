INSERT INTO tb_conversation_courses_ctg (name, id_language_id, id_level_id,created_at) VALUES
       ('HTML5 CSS3 Modulo 1', (SELECT id FROM tb_conversation_languages_ctg l WHERE l.name = 'HTML e CSS' ), (SELECT id FROM tb_conversation_level_ctg lv WHERE lv.name = 'Iniciante'), DATE ('now')),
       ('HTML5 CSS3 Modulo 2', (SELECT id FROM tb_conversation_languages_ctg l WHERE l.name = 'HTML e CSS' ), (SELECT id FROM tb_conversation_level_ctg lv WHERE lv.name = 'Intermediário'), DATE ('now')),
       ('HTML5 CSS3 Modulo 3', (SELECT id FROM tb_conversation_languages_ctg l WHERE l.name = 'HTML e CSS' ), (SELECT id FROM tb_conversation_level_ctg lv WHERE lv.name = 'Avançado'), DATE ('now')),
       ('React JS', (SELECT id FROM tb_conversation_languages_ctg l WHERE l.name = 'React JS'), (SELECT id FROM tb_conversation_level_ctg lv WHERE lv.name = 'Iniciante'), DATE ('now')),
       ('Angular JS', (SELECT id FROM tb_conversation_languages_ctg l WHERE l.name = 'Angular JS'), (SELECT id FROM tb_conversation_level_ctg lv WHERE lv.name = 'Iniciante'), DATE ('now')),
       ('Logica de Programação', (SELECT id FROM tb_conversation_languages_ctg l WHERE l.name = 'Lógica de Programação'), (SELECT id FROM tb_conversation_level_ctg lv WHERE lv.name = 'Iniciante'), DATE ('now')),
       ('Java Iniciante', (SELECT id FROM tb_conversation_languages_ctg l WHERE l.name = 'Java '), (SELECT id FROM tb_conversation_level_ctg lv WHERE lv.name = 'Iniciante'), DATE ('now')),
       ('Java Intermediário', (SELECT id FROM tb_conversation_languages_ctg l WHERE l.name = 'Java '), (SELECT id FROM tb_conversation_level_ctg lv WHERE lv.name = 'Intermediário'), DATE ('now')),
       ('Python Intermediário', (SELECT id FROM tb_conversation_languages_ctg l WHERE l.name = 'Python'), (SELECT id FROM tb_conversation_level_ctg lv WHERE lv.name = 'Intermediário'), DATE ('now')),
       ('Python Django', (SELECT id FROM tb_conversation_languages_ctg l WHERE l.name = 'Python'), (SELECT id FROM tb_conversation_level_ctg lv WHERE lv.name = 'Iniciante'), DATE ('now')),
       ('JavaScript Iniciante', (SELECT id FROM tb_conversation_languages_ctg l WHERE l.name = 'JavaScript'), (SELECT id FROM tb_conversation_level_ctg lv WHERE lv.name = 'Iniciante'), DATE ('now')),
       ('Node JS', (SELECT id FROM tb_conversation_languages_ctg l WHERE l.name = 'JavaScript'), (SELECT id FROM tb_conversation_level_ctg lv WHERE lv.name = 'Iniciante'), DATE ('now')),
       ('Kotlin', (SELECT id FROM tb_conversation_languages_ctg l WHERE l.name = 'Kotlin'), (SELECT id FROM tb_conversation_level_ctg lv WHERE lv.name = 'Iniciante'), DATE ('now')),
       ('Git e Github', (SELECT id FROM tb_conversation_languages_ctg l WHERE l.name = 'Git e Github'), (SELECT id FROM tb_conversation_level_ctg lv WHERE lv.name = 'Iniciante'), DATE ('now')),
       ('Redes de computadores', (SELECT id FROM tb_conversation_languages_ctg l WHERE l.name = 'Redes de computadores'), (SELECT id FROM tb_conversation_level_ctg lv WHERE lv.name = 'Iniciante'), DATE ('now')),
       ('Criação de automação de testes', (SELECT id FROM tb_conversation_languages_ctg l WHERE l.name = 'Criação de automação de testes'), (SELECT id FROM tb_conversation_level_ctg lv WHERE lv.name = 'Iniciante'), DATE ('now')),
       ('Banco de dados MySql', (SELECT id FROM tb_conversation_languages_ctg l WHERE l.name = 'Banco de dados'), (SELECT id FROM tb_conversation_level_ctg lv WHERE lv.name = 'Iniciante'), DATE ('now'));



