/*dummy data for testing*/

INSERT INTO Status (Description) VALUES ("Not Started");
INSERT INTO Status (Description) VALUES ("Started");
INSERT INTO Status (Description) VALUES ("Finished");

INSERT INTO Event (Title, Description) VALUES ("Created", "double oof");
INSERT INTO Event (Title, Description) VALUES ("Edited", "oof");
INSERT INTO Event (Title, Description) VALUES ("Completed", "zomg");

INSERT INTO Employee
(First_Name, Last_Name, Admin, Username, Password)
VALUES
("Cameron", "Schaer", 1, "cbs", "password");

INSERT INTO Employee
(First_Name, Last_Name, Admin, Username, Password)
VALUES
("Ralph", "Bradley", 0, "rb", "hunter2");

INSERT INTO Employee (First_Name, Last_Name, Admin, Username, Password) 
VALUES ("Jameswell", "Olson", 0, "jams", "oof1");
INSERT INTO Employee (First_Name, Last_Name, Admin, Username, Password) 
VALUES ("Gabriel", "Keith", 1, "admin", "admin");


INSERT INTO Task
(Title, Description, Status_ID, Creation_TS, Created_by)
VALUES
("Do the thing!", "Lorem ipsum dolor sit amet.", 1, CURRENT_TIMESTAMP, 1);

INSERT INTO Task
(Title, Description, Status_ID, Creation_TS, Created_by)
VALUES
("Call James", "Lorem ipsum dolor sit amet?", 1, CURRENT_TIMESTAMP, 1);

INSERT INTO Employee_Task
(Employee_ID, Task_ID)
VALUES
(1, 2);

INSERT INTO Task_Event
(Event_ID, Task_ID, Event_TS, Employee_ID)
VALUES
(1, 2, CURRENT_TIMESTAMP, 1);

INSERT INTO Task_Event
(Event_ID, Task_ID, Event_TS, Employee_ID)
VALUES
(2, 2, CURRENT_TIMESTAMP, 3);

/*
SELECT * FROM Employee;
SELECT * FROM Task;
SELECT * FROM Employee_Task;
SELECT * FROM Status;
SELECT * FROM Task_Event;
SELECT * FROM Event;
*/