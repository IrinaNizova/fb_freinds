DELETE FROM fbusers.django_site;
INSERT INTO fbusers.django_site (id, domain, name) VALUES(1, 'localhost:8000', 'localhost:8000');
INSERT INTO fbusers.socialaccount_socialapp (id, provider, name, client_id, secret) VALUES (1, 'facebook', 'fbfriends', '451075868621096', '9a9b8254805657f53071b9b6edc30e08');