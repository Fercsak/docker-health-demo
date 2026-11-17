import sqlite3

con = sqlite3.connect("practice.db")
con.executescript("""
DROP TABLE IF EXISTS readings;
DROP TABLE IF EXISTS turbines;

CREATE TABLE turbines (
    id INTEGER PRIMARY KEY,
    name TEXT,
    site TEXT,
    type TEXT
);

CREATE TABLE readings (
    id INTEGER PRIMARY KEY,
    turbine_id INTEGER,
    read_date TEXT,
    power_kw REAL,
    FOREIGN KEY (turbine_id) REFERENCES turbines(id)
);

INSERT INTO turbines VALUES
(1,'T-01','Szeged','wind'), (2,'T-02','Szeged','wind'),
(3,'T-03','Pécs','gas'),    (4,'T-04','Győr','wind'),
(5,'T-05','Győr','gas'),    (6,'T-06','Miskolc','wind');

INSERT INTO readings (turbine_id, read_date, power_kw) VALUES
(1,'2026-11-01',1200),(1,'2026-11-02',1350),(1,'2026-11-03',900),
(2,'2026-11-01',1100),(2,'2026-11-02',NULL),(2,'2026-11-03',1000),
(3,'2026-11-01',2500),(3,'2026-11-02',2600),
(4,'2026-11-01',800),(4,'2026-11-02',950),(4,'2026-11-03',1020),
(5,'2026-11-01',2400),(5,'2026-11-03',2550);
""")

def q(sql):
    print()
    cur = con.execute(sql)
    print([c[0] for c in cur.description])
    for row in cur.fetchall():
        print(row)

"""
q("SELECT site, COUNT(*) AS turbine_count FROM turbines GROUP BY site")

q("SELECT id FROM turbines WHERE type='wind' ORDER BY name DESC")

q("SELECT turbine_id, AVG(power_kw) AS avg_kw FROM readings GROUP BY turbine_id HAVING AVG(power_kw) > 1000")
q("SELECT site FROM turbines WHERE type IS NOT NULL GROUP BY site")
q("SELECT turbine_id, AVG(power_kw) AS avg_kw FROM readings GROUP BY turbine_id")


q("SELECT t.name, r.read_date, r.power_kw FROM turbines t INNER JOIN readings r ON r.turbine_id = t.id")
q("SELECT t.name, COUNT(r.id) AS reading_count FROM turbines t LEFT JOIN readings r ON r.turbine_id = t.id GROUP BY t.name;")
q("SELECT t.name, t.site, r.power_kw FROM turbines t INNER JOIN readings r ON r.turbine_id = t.id")
q("SELECT t.name, t.site, r.power_kw FROM turbines t INNER JOIN readings r ON r.turbine_id = t.id GROUP BY t.name")
q("SELECT * FROM readings WHERE power_kw > (SELECT AVG(power_kw) FROM readings)")
q("SELECT * FROM readings WHERE power_kw < (SELECT AVG(power_kw) FROM readings) LIMIT 4")
q("SELECT AVG(power_kw) AS average_power FROM readings")
q("SELECT name FROM turbines WHERE id IN (SELECT turbine_id FROM readings)")
q("WITH avg_per_turbine AS (SELECT turbine_id, AVG(power_kw) AS avg_kw FROM readings GROUP BY turbine_id) SELECT t.name, a.avg_kw  FROM avg_per_turbine a JOIN turbines t ON t.id = a.turbine_id WHERE a.avg_kw > 1000;")
"""
#FELADATOK
q("SELECT name, site FROM turbines WHERE type='wind'")
q("SELECT site, COUNT(id) AS count FROM turbines GROUP BY site")
q("SELECT t.name, AVG(r.power_kw) AS average FROM turbines t JOIN readings r ON r.turbine_id = t.id GROUP BY t.name")
q("SELECT t.name FROM turbines t LEFT JOIN readings r ON r.turbine_id = t.id WHERE r.id IS NULL")
q("SELECT t.site, AVG(r.power_kw) AS avg_kw FROM turbines t JOIN readings r ON r.turbine_id = t.id GROUP BY t.site HAVING AVG(r.power_kw) > 1500")
q("SELECT COUNT(*) AS count FROM readings WHERE power_kw IS NULL")
q("SELECT t.name, r.power_kw FROM turbines t JOIN readings r ON r.turbine_id = t.id ORDER BY r.power_kw DESC LIMIT 3")
q("SELECT t.name, r.read_date FROM turbines t LEFT JOIN readings r ON r.turbine_id = t.id")