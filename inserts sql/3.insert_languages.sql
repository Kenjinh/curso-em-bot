INSERT INTO tb_conversation_languages_ctg (name, id_area_id,created_at)
VALUES
        ('HTML e CSS', (SELECT id FROM tb_conversation_areas_ctg a WHERE a.name = 'Front-End'), DATE('now')),
        ('React JS', (SELECT id FROM tb_conversation_areas_ctg a WHERE a.name = 'Front-End'), DATE('now')),
        ('Angular JS', (SELECT id FROM tb_conversation_areas_ctg a WHERE a.name = 'Front-End'), DATE('now')),
        ('Java ', (SELECT id FROM tb_conversation_areas_ctg a WHERE a.name = 'Back-End'), DATE('now')),
        ('Python', (SELECT id FROM tb_conversation_areas_ctg a WHERE a.name = 'Back-End'), DATE('now')),
        ('JavaScript', (SELECT id FROM tb_conversation_areas_ctg a WHERE a.name = 'Back-End'), DATE('now')),
        ('Kotlin', (SELECT id FROM tb_conversation_areas_ctg a WHERE a.name = 'Mobile'), DATE('now')),
        ('Flutter', (SELECT id FROM tb_conversation_areas_ctg a WHERE a.name = 'Mobile'), DATE('now')),
        ('React-Native', (SELECT id FROM tb_conversation_areas_ctg a WHERE a.name = 'Mobile'), DATE('now')),
        ('Git e Github', (SELECT id FROM tb_conversation_areas_ctg a WHERE a.name = 'Git e GitHub'), DATE('now')),
        ('Redes de computadores', (SELECT id FROM tb_conversation_areas_ctg a WHERE a.name = 'Redes de computadores'), DATE('now')),
        ('Criação de automação de testes', (SELECT id FROM tb_conversation_areas_ctg a WHERE a.name = 'Criação de automação de testes'), DATE('now')),
        ('Banco de dados', (SELECT id FROM tb_conversation_areas_ctg a WHERE a.name = 'Banco de dados'), DATE('now')),
        ('Lógica de Programação', (SELECT id FROM tb_conversation_areas_ctg a WHERE a.name = 'Back-End'), DATE('now'));

