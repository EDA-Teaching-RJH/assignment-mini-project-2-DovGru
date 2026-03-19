In this assessment I developed a python based EE customer data mnagement system for a staff member to be able to add, store and manage customer data. The program is able to store customers name, phone number and the plan they are on, and allows the data to be saved and loaded from a CSV file.

One of the main concepts I used was OOP (Object-Oriented Programming). I created a Customer class to show individual customers and also used a subclass (PayMonthlycustomer) to show the use of inheritance by adding an additional attribute being the contract length. 

I also made sure that the mobile number entered foillowed a UK mobile format. This prevents from invalid data being stored. Additionally, I used try and except blocks to handle errors. this makes sure that the program doesnt crash incorrect data is entered.

Another important part of this system was file handling. I used the csv module to store customers data to a file and load back into the program. This also means that the data is saved on the program even once it has been closed, it can be opened again later and the data will be saved. 

I created test files using pytest to test validation functions and Customer class. The test included valid and invalid inputs. Running the pytest ensured that the tests passed sucessfuly showing that the program behaves as expected.

Overall, this programming assessment helped me develop a much better understanding of Python, especially in areas such as OOP, file handling, validation and testing. If I were to improve this program I would add additional features like removing a customer or editing an existing customer details. 