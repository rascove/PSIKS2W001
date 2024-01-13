class Staff:
    def __init__(self, staffID, password, name):
        self.__staffID = staffID
        self.__password = password
        self.__name = name

    def getStaffID(self):
        return self.__staffID
    
    def setStaffID(self, staffID):
        self.__staffID = staffID

    def getPassword(self):
        return self.__password
    
    def setPassword(self, password):
        self.__password = password

    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name

    def __str__(self):
        return self.__name

class Car:
    def __init__(self, carID, plateNo, model, price):
        self.__carID = carID
        self.__plateNo = plateNo
        self.__model = model
        self.__price = price

    def getCarID(self):
        return self.__carID
    
    def setCarID(self, carID):
        self.__carID = carID

    def getPlateNo(self):
        return self.__plateNo
    
    def setPlateNo(self, plateNo):
        self.__plateNo = plateNo

    def getModel(self):
        return self.__model
    
    def setModel(self, model):
        self.__model = model

    def getPrice(self):
        return self.__price
    
    def setPrice(self, price):
        self.__price = price

    def __str__(self):
        return self.__plateNo

class Customer:
    def __init__(self, customerID, name, licenceNo, phoneNo):
        self.__customerID = customerID
        self.__name = name
        self.__licenceNo = licenceNo
        self.__phoneNo = phoneNo

    def getCustomerID(self):
        return self.__customerID
    
    def setCustomerID(self, customerID):
        self.__customerID = customerID

    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name

    def getLicenceNo(self):
        return self.__licenceNo
    
    def setLicenceNo(self, licenceNo):
        self.__licenceNo = licenceNo

    def getPhoneNo(self):
        return self.__phoneNo
    
    def setPhoneNo(self, phoneNo):
        self.__phoneNo = phoneNo

    def __str__(self):
        return self.__name

class Rental:
    def __init__(self, carID, customerID, start, duration):
        self.__carID = carID
        self.__customerID = customerID
        self.__start = start
        self.__duration = duration

    def getCarID(self):
        return self.__carID
    
    def setCarID(self, carID):
        self.__carID = carID

    def getCustomerID(self):
        return self.__customerID
    
    def setCustomerID(self, customerID):
        self.__customerID = customerID

    def getStart(self):
        return self.__start
    
    def setStart(self, start):
        self.__start = start

    def getDuration(self):
        return self.__duration
    
    def setDuration(self, duration):
        self.__duration = duration

    def __str__(self):
        return self.__start