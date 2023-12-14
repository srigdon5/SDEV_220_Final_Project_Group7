-- SQLite

--Branches
INSERT INTO branch (name, address, phone)
VALUES
    ("Central", "200 SE Martin Luther King Blvd.", "812.428.8200"),
    ("East", "840 E. Chandler Ave.", "812.428.8231"),
    ("McCollough", "5115 Washington Ave.", "812.428.8236"),
    ("North Park", "960 Koehler Dr.", "812.428.8237"),
    ("Oaklyn", "3001 Oaklyn Dr.", "812.428.8237"),
    ("Red Bank", "120 S. Red Bank Rd.", "812.428.8205"),
    ("Stringtown ", "2100 Stringtown Rd.", "812.428.8233"),
    ("West", "2000 W. Franklin St.", "812.428.8232"),
    ("Washington Square-McCollough", "1108 Washington Square Mall", "812.428.8236");
    
-- Patrons
INSERT INTO patron (branch_id, name, phone, account_type, limit_reached, fees)
VALUES
    (1, "Bob Ross", "123.456.7890", "Adult", FALSE, 0),
    (1, "Rob Boss", "567.890.1234", "Child", FALSE, 0),
    (2, "Steve Irwin", "234.567.8901", "Adult", FALSE, 0),
    (2, "Robert Irwin", "789.012.3456", "Child", FALSE, 0),
    (3, "W. C. Handy", "456.789.0123", "Adult", FALSE, 0),
    (3, "Louis Armstrong", "901.234.5678", "Child", FALSE, 0),
    (4, "Heady Lamar", "345.678.9012", "Adult", FALSE, 0),
    (4, "Ada Lovelace", "890.123.4567", "Child", FALSE, 0),
    (5, "Margaret Hamilton", "678.901.2345", "Adult", FALSE, 0),
    (5, "Rona Ramon", "321.098.7654", "Child", FALSE, 0),
    (6, "Barbra Liskov", "876.543.2109", "Adult", FALSE, 0),
    (6, "Radia Perlman", "543.210.9876", "Child", FALSE, 0),
    (7, "Mary Kenneth Keller", "210.987.6543", "Adult", FALSE, 0),
    (7, "Shafi Goldwasser", "432.109.8765", "Child", FALSE, 0),
    (8, "Adele Goldberg", "987.654.3210", "Adult", FALSE, 0),
    (8, "Joan Hamilton Green", "654.321.0987", "Child", FALSE, 0),
    (9, "Radhika Nagpal", "789.765.4321", "Adult", FALSE, 0),
    (9, "Fran Allen", "876.543.2098", "Child", FALSE, 0);

-- Items(books
INSERT INTO item (branch_id, isbn, item_type, status, title, genre)
VALUES
    (1, "9780195153446", "book", "available", "Classical Mythology", "Myths"),
    (2, "9780002005012", "book", "available", "Clara Callan", "Historical Fiction"),
    (3, "9780060506070", "book", "available", "Clara Callan", "Historical Fiction"),
    (4, "9780393045215", "book", "available", "The Mummies of Urumchi", "Historical"),
    (5, "9780143038108", "book", "available", "The Kitchen God's Wife", "Historical Fiction"),
    (6, "9781538727157", "book", "available", "Pleading Guilty", "Thriller"),
    (7, "9780399150210", "book", "available", "Hercule Poirot's Casebook", "Mystery"),
    (8, "9780062073907", "book", "available", "Murder in Mesopotamia: A Hercule Poirot Mystery", "Mystery"),
    (9, "9780062573223", "book", "available", " The A.B.C Murders: A Hercule Poirot Mystery", "Mystery");
-- authors
INSERT INTO author (author_name)
VALUES
    ("Agatha Christie"),
    ("Mark P.O. Morford"),
    ("Richard Bruce Wright"),
    ("E.J.W. Barber"),
    ("Scott Turow"),
    ("Amy Tan");

--books
INSERT INTO book (isbn, author_id, medium, pages)
VALUES
    ("9780195153446", 2, "paperback", 844),
    ("9780002005012", 3, "hard cover", 414),
    ("9780060506070", 3, "paperback", 432),
    ("9780393045215", 4, "hard cover", 240),
    ("9780143038108", 6, "paperback", 416),
    ("9781538727157", 5, "paperback", 464),
    ("9780399150210", 1, "hard cover", 861),
    ("9780062073907", 1, "paperback", 288),
    ("9780062573223", 1, "hard cover", 272);

--item movies
INSERT INTO item (branch_id, isan, item_type, status, title, genre)
VALUES
    (1, "0000000611A10000Z000000006", "movie", "available", "Space Jam(1996)", "Family"),
    (2, "00000000401A0000700000000G", "movie", "available", "The Lord of The Rings: The Fellowship of The Ring", "Fantasy");

--movies
INSERT INTO movie (isan, runtime, medium)
VALUES
    ("0000000611A10000Z000000006", 81, "dvd"),
    ("00000000401A0000700000000G", 178, "blu-ray");