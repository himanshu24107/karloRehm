import mysql.connector

table = [
    ('Hydrogen', 'H', 1, 1.008),
    ('Helium', 'He', 2, 4.0026),
    ('Lithium', 'Li', 3, 6.94),
    ('Beryllium', 'Be', 4, 9.0122),
    ('Boron', 'B', 5, 10.81),
    ('Carbon', 'C', 6, 12.011),
    ('Nitrogen', 'N', 7, 14.007),
    ('Oxygen', 'O', 8, 15.999),
    ('Fluorine', 'F', 9, 18.998),
    ('Neon', 'Ne', 10, 20.180),
    ('Sodium', 'Na', 11, 22.990),
    ('Magnesium', 'Mg', 12, 24.305),
    ('Aluminum', 'Al', 13, 26.982),
    ('Silicon', 'Si', 14, 28.085),
    ('Phosphorus', 'P', 15, 30.974),
    ('Sulfur', 'S', 16, 32.06),
    ('Chlorine', 'Cl', 17, 35.453),
    ('Argon', 'Ar', 18, 39.948),
    ('Potassium', 'K', 19, 39.098),
    ('Calcium', 'Ca', 20, 40.078),
    ('Scandium', 'Sc', 21, 44.956),
    ('Titanium', 'Ti', 22, 47.867),
    ('Vanadium', 'V', 23, 50.942),
    ('Chromium', 'Cr', 24, 51.996),
    ('Manganese', 'Mn', 25, 54.938),
    ('Iron', 'Fe', 26, 55.845),
    ('Cobalt', 'Co', 27, 58.933),
    ('Nickel', 'Ni', 28, 58.693),
    ('Copper', 'Cu', 29, 63.546),
    ('Zinc', 'Zn', 30, 65.38),
    ('Gallium', 'Ga', 31, 69.723),
    ('Germanium', 'Ge', 32, 72.630),
    ('Arsenic', 'As', 33, 74.922),
    ('Selenium', 'Se', 34, 78.971),
    ('Bromine', 'Br', 35, 79.904),
    ('Krypton', 'Kr', 36, 83.798),
    ('Rubidium', 'Rb', 37, 85.468),
    ('Strontium', 'Sr', 38, 87.62),
    ('Yttrium', 'Y', 39, 88.906),
    ('Zirconium', 'Zr', 40, 91.224),
    ('Niobium', 'Nb', 41, 92.906),
    ('Molybdenum', 'Mo', 42, 95.95),
    ('Technetium', 'Tc', 43, 98.0),
    ('Ruthenium', 'Ru', 44, 101.07),
    ('Rhodium', 'Rh', 45, 102.91),
    ('Palladium', 'Pd', 46, 106.42),
    ('Silver', 'Ag', 47, 107.87),
    ('Cadmium', 'Cd', 48, 112.41),
    ('Indium', 'In', 49, 114.82),
    ('Tin', 'Sn', 50, 118.71),
    ('Antimony', 'Sb', 51, 121.76),
    ('Tellurium', 'Te', 52, 127.60),
    ('Iodine', 'I', 53, 126.90),
    ('Xenon', 'Xe', 54, 131.29),
    ('Cesium', 'Cs', 55, 132.91),
    ('Barium', 'Ba', 56, 137.33),
    ('Lanthanum', 'La', 57, 138.91),
    ('Cerium', 'Ce', 58, 140.12),
    ('Praseodymium', 'Pr', 59, 140.91),
    ('Neodymium', 'Nd', 60, 144.24),
    ('Promethium', 'Pm', 61, 145.0),
    ('Samarium', 'Sm', 62, 150.36),
    ('Europium', 'Eu', 63, 152.00),
    ('Gadolinium', 'Gd', 64, 157.25),
    ('Terbium', 'Tb', 65, 158.93),
    ('Dysprosium', 'Dy', 66, 162.50),
    ('Holmium', 'Ho', 67, 164.93),
    ('Erbium', 'Er', 68, 167.26),
    ('Thulium', 'Tm', 69, 168.93),
    ('Ytterbium', 'Yb', 70, 173.05),
    ('Lutetium', 'Lu', 71, 175.00),
    ('Hafnium', 'Hf', 72, 178.49),
    ('Tantalum', 'Ta', 73, 180.95),
    ('Tungsten', 'W', 74, 183.84),
    ('Rhenium', 'Re', 75, 186.21),
    ('Osmium', 'Os', 76, 190.23),
    ('Iridium', 'Ir', 77, 192.22),
    ('Platinum', 'Pt', 78, 195.08),
    ('Gold', 'Au', 79, 196.97),
    ('Mercury', 'Hg', 80, 200.59),
    ('Thallium', 'Tl', 81, 204.38),
    ('Lead', 'Pb', 82, 207.2),
    ('Bismuth', 'Bi', 83, 208.98),
    ('Polonium', 'Po', 84, 209.98),
    ('Astatine', 'At', 85, 210.00),
    ('Radon', 'Rn', 86, 222.00),
    ('Francium', 'Fr', 87, 223.00),
    ('Radium', 'Ra', 88, 226.00),
    ('Actinium', 'Ac', 89, 227.00),
    ('Thorium', 'Th', 90, 232.04),
    ('Protactinium', 'Pa', 91, 231.04),
    ('Uranium', 'U', 92, 238.03),
    ('Neptunium', 'Np', 93, 237.00),
    ('Plutonium', 'Pu', 94, 244.00),
    ('Americium', 'Am', 95, 243.00),
    ('Curium', 'Cm', 96, 247.00),
    ('Berkelium', 'Bk', 97, 247.00),
    ('Californium', 'Cf', 98, 251.00),
    ('Einsteinium', 'Es', 99, 252.00),
    ('Fermium', 'Fm', 100, 257.00),
    ('Mendelevium', 'Md', 101, 258.00),
    ('Nobelium', 'No', 102, 259.00),
    ('Lawrencium', 'Lr', 103, 262.00),
    ('Rutherfordium', 'Rf', 104, 267.00),
    ('Dubnium', 'Db', 105, 270.00),
    ('Seaborgium', 'Sg', 106, 271.00),
    ('Bohrium', 'Bh', 107, 270.00),
    ('Hassium', 'Hs', 108, 277.00)
]

mydb=mysql.connector.connect(host="localhost",user="root",passwd="root")
c = mydb.cursor()
c.execute('create database Chemistry;')
c.execute('use Chemistry;')
print("Database created successfully...............")
c.execute("create table elements(name varchar(20), symbol varchar(4), number int(5), mass float(6,2));")
# Insert data into the 'elements' table
for element in table:
    query = "INSERT INTO elements (name, symbol, number, mass) VALUES (%s, %s, %s, %s);"
    c.execute(query, element)

mydb.commit()
print("Data inserted successfully...............")

mydb.close()









