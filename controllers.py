import mysql.connector;
from models import *

class Controller:
    def _getConnection(self):
        return mysql.connector.connect(host = "localhost", user = 'root', password = 'abcd1234#', database = 'CarRentalDB')

class StaffController(Controller):
    def login(self, staffID, password):
        staff = None
        conn = self._getConnection()
        cursor = conn.cursor()

        cursor.execute("SELECT `Name` FROM Staff WHERE StaffID = %s AND Password = %s", (staffID, password))

        result = cursor.fetchone()

        if result:
            staff = Staff(staffID, password, result[0])

        conn.close()

        return staff
    
class CarController(Controller):
    def add(self, car):
        result = 0

        try:
            conn = self._getConnection()
            cursor = conn.cursor()

            cursor.execute("INSERT INTO Car (PlateNo, Model, Price) VALUES (%s, %s, %s)", (car.getPlateNo(), car.getModel(), car.getPrice()))
            conn.commit()

            result = cursor.lastrowid

            if result != 0:
                car.setCarID(result)

            conn.close()
        except Exception as e:
            print('Terjadi masalah', e)

        return result
    
    def edit(self, car):
        result = 0

        try:
            conn = self._getConnection()
            cursor = conn.cursor()

            cursor.execute("UPDATE Car SET PlateNo = %s, Model = %s, Price = %s WHERE CarID = %s", (car.getPlateNo(), car.getModel(), car.getPrice(), car.getCarID()))
            conn.commit()

            result = cursor.rowcount

            conn.close()
        except Exception as e:
            print('Terjadi masalah', e)

        return result
    
    def view(self):
        cars = []
        conn = self._getConnection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Car")

        result = cursor.fetchall()

        for r in result:
            cars.append(Car(r[0], r[1], r[2], r[3]))
        
        conn.close()

        return cars