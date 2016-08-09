DROP TABLE IF EXISTS breeds;
CREATE TABLE breeds(
    breed_id INT UNSIGNED NOT NULL AUTO_INCREMENT primary key,
    breedName VARCHAR(255) NOT NULL
);

INSERT INTO breeds (breedName) VALUES ('labrador');
INSERT INTO breeds (breedName) VALUES ('pug');
INSERT INTO breeds (breedName) VALUES ('retriever');
INSERT INTO breeds (breedName) VALUES ('yorkie');

DROP TABLE IF EXISTS dogs;
CREATE TABLE dogs(
    dogID INT UNSIGNED NOT NULL AUTO_INCREMENT primary key,
    breed_id INT UNSIGNED NOT NULL,
    photo_url VARCHAR(255),
    dogName VARCHAR(255),
    dogDescription TEXT
);

INSERT INTO dogs (breed_id, photo_url) VALUES (1, 'http://i.imgur.com/eE29vX4.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (1, 'http://i.imgur.com/xX2AeDR.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (1, 'http://i.imgur.com/hBFRUuW.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (1, 'http://i.imgur.com/WDWK4nF.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (1, 'http://i.imgur.com/zxtD5Zw.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (1, 'http://i.imgur.com/MrkAGKR.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (1, 'http://i.imgur.com/o3Nyw4R.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (1, 'http://i.imgur.com/SzP5370.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (1, 'http://i.imgur.com/oHaP6I3.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (1, 'http://i.imgur.com/kSU7Zca.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (1, 'http://i.imgur.com/SAJJ1oH.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (1, 'http://i.imgur.com/BYvRbs8.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (1, 'http://i.imgur.com/VzFTsGg.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (1, 'http://i.imgur.com/qigJZWa.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (1, 'http://i.imgur.com/gskym.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (2, 'http://i.imgur.com/ozJD7SC.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (2, 'http://i.imgur.com/E5vBM5Z.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (2, 'http://i.imgur.com/miiP4NI.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (2, 'http://i.imgur.com/GCE8dj5.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (2, 'http://i.imgur.com/NGG3Yir.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (2, 'http://i.imgur.com/q53cfRy.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (2, 'http://i.imgur.com/Flic3TB.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (2, 'http://i.imgur.com/zjgtrf9.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (2, 'http://i.imgur.com/Mda3xXr.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (2, 'http://i.imgur.com/IOh5mgB.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (2, 'http://i.imgur.com/Fl2ivvG.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (2, 'http://i.imgur.com/iLzWvSY.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (2, 'http://i.imgur.com/RQKBN3F.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (2, 'http://i.imgur.com/8c3RpI0.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (2, 'http://i.imgur.com/7ysJzS4.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (2, 'http://i.imgur.com/uccGfLn.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (2, 'http://i.imgur.com/HrscSnK.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (2, 'http://i.imgur.com/tUZhJYN.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (2, 'http://i.imgur.com/xAGJ0Ry.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (2, 'http://i.imgur.com/YxSvzWm.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (2, 'http://i.imgur.com/Y32LWO6.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (2, 'http://i.imgur.com/umJXx6S.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (2, 'http://i.imgur.com/R8Ju76x.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (2, 'http://i.imgur.com/xTg9j70.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (2, 'http://i.imgur.com/zUnR5lj.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (2, 'http://i.imgur.com/RUjOi8t.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (2, 'http://i.imgur.com/Dd1K1uR.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (2, 'http://i.imgur.com/Q5uksG8.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (2, 'http://i.imgur.com/7YxiavD.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (2, 'http://i.imgur.com/8B3HOrS.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (2, 'http://i.imgur.com/9YfjSxU.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (2, 'http://i.imgur.com/NSCW1Rz.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (2, 'http://i.imgur.com/ZwM4KY4.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (2, 'http://i.imgur.com/uy9pY3Y.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (2, 'http://i.imgur.com/ZFk0cgV.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (2, 'http://i.imgur.com/6Fz5JOg.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (2, 'http://i.imgur.com/mNQbxWo.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (2, 'http://i.imgur.com/C1MFoB0.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (2, 'http://i.imgur.com/Rdbawjx.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (3, 'http://i.imgur.com/wR38uBx.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (3, 'http://i.imgur.com/CHRlo0W.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (3, 'http://i.imgur.com/tXnch1O.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (3, 'http://i.imgur.com/VCgfaB2.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (3, 'http://i.imgur.com/Ror46i4.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (3, 'http://i.imgur.com/Ful5PwH.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (3, 'http://i.imgur.com/C4rrJdn.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (3, 'http://i.imgur.com/Ao9bR9A.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (3, 'http://i.imgur.com/R14AU0I.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (3, 'http://i.imgur.com/gpH8wIV.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (3, 'http://i.imgur.com/luPxoig.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (3, 'http://i.imgur.com/MiIDyfD.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (3, 'http://i.imgur.com/4qmmRFj.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (3, 'http://i.imgur.com/ZSzHQ2q.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (3, 'http://i.imgur.com/PoA6rLg.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (3, 'http://i.imgur.com/NYwynk3.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (3, 'http://i.imgur.com/ni8vK0U.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (3, 'http://i.imgur.com/NinMpda.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (3, 'http://i.imgur.com/4L8rMko.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (3, 'http://i.imgur.com/HoISzqN.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (3, 'http://i.imgur.com/FPISssi.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (3, 'http://i.imgur.com/SzP5370.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (3, 'http://i.imgur.com/oHaP6I3.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (3, 'http://i.imgur.com/wlVWJpY.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (3, 'http://i.imgur.com/rV4COi2.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (3, 'http://i.imgur.com/6WZFhJX.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (3, 'http://i.imgur.com/gFLzkPt.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (3, 'http://i.imgur.com/ULSe4AI.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (3, 'http://i.imgur.com/yDEa2a5.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (3, 'http://i.imgur.com/BYvRbs8.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (3, 'http://i.imgur.com/VzFTsGg.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (3, 'http://i.imgur.com/BnhbY54.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (3, 'http://i.imgur.com/ToYsMEC.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (4, 'http://i.imgur.com/oSieVUO.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (4, 'http://i.imgur.com/qtXIL.png');
INSERT INTO dogs (breed_id, photo_url) VALUES (4, 'http://i.imgur.com/qWLKy8a.jpg');

DROP TABLE IF EXISTS votes;
CREATE TABLE votes(
    dogID INT UNSIGNED NOT NULL,
    vote INT default '0'
);
