import sqlite3

conn = sqlite3.connect('hotel.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        Ref TEXT PRIMARY KEY,
        Name TEXT NOT NULL,
        Mother TEXT NOT NULL,
        Gender TEXT NOT NULL,
        Post TEXT NOT NULL,
        Mobile TEXT NOT NULL UNIQUE,
        Email TEXT NOT NULL,
        Nationality TEXT NOT NULL,
        Id_proof TEXT NOT NULL,
        Id_number TEXT NOT NULL UNIQUE,
        Address TEXT NOT NULL
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS room_bookings (
        CustomerContact TEXT NOT NULL,
        CheckInDate TEXT NOT NULL,
        CheckOutDate TEXT NOT NULL,
        RoomType TEXT NOT NULL,
        RoomNumber TEXT NOT NULL,
        MealPlan TEXT NOT NULL,
        NumberOfDays INTEGER NOT NULL,
        PaidTax REAL NOT NULL,
        SubTotal REAL NOT NULL,
        TotalCost REAL NOT NULL
    )
''')
cursor.execute('''
               CREATE TABLE IF NOT EXISTS room_details (
               Floor TEXT NOT NULL,
               RoomNo TEXT PRIMARY KEY,
               RoomType TEXT NOT NULL
)''')

conn.commit()
conn.close()

print("Database and table created successfully!")
print("Room bookings table created successfully!")
print("Room details table created successfully!")
