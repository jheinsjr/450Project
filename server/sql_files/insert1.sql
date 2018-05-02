/*dummy data for testing*/

INSERT INTO Status (Description) VALUES ("Not Started");
INSERT INTO Status (Description) VALUES ("Started");
INSERT INTO Status (Description) VALUES ("Finished");

INSERT INTO Event (Title, Description) VALUES ("Created", "double oof");
INSERT INTO Event (Title, Description) VALUES ("Edited", "oof");
INSERT INTO Event (Title, Description) VALUES ("Completed", "zomg");

/*EMPLOYEES*/
INSERT INTO Employee (First_Name, Last_Name, Admin, Username, Password)
VALUES ("Cameron", "Schaer", 1, "cbs", "password");
INSERT INTO Employee (First_Name, Last_Name, Admin, Username, Password)
VALUES ("Ralph", "Bradley", 0, "rb", "hunter2");
INSERT INTO Employee (First_Name, Last_Name, Admin, Username, Password) 
VALUES ("Jameswell", "Olson", 1, "james_af", "big_oofer_1");
INSERT INTO Employee (First_Name, Last_Name, Admin, Username, Password) 
VALUES ("Gabriel", "Keith", 1, "gabe", "admin");
INSERT INTO Employee (First_Name, Last_Name, Admin, Username, Password)
VALUES ("Bob", "King", 0, "bobert", "hunter2");
INSERT INTO Employee (First_Name, Last_Name, Admin, Username, Password)
VALUES ("Jack", "Tompkins", 0, "xx_noscopeKing_xx", "hunter2");

/*TASKS*/
INSERT INTO Task (Title, Description, Status_ID, Creation_TS, Created_by)
VALUES ("Do the thing!", "Lorem ipsum dolor sit amet.", 2, CURRENT_TIMESTAMP, 1);
INSERT INTO Task (Title, Description, Status_ID, Creation_TS, Created_by)
VALUES ("Call James", "Better not forget", 1, CURRENT_TIMESTAMP, 1);
INSERT INTO Task (Title, Description, Status_ID, Creation_TS, Created_by)
VALUES ("Install slite3", "On all them computers", 3, CURRENT_TIMESTAMP, 4);
INSERT INTO Task (Title, Description, Status_ID, Creation_TS, Created_by)
VALUES ("Refactor database code", "Gotta turn the mysql to sqlite, know what I mean?", 1, CURRENT_TIMESTAMP, 3);
INSERT INTO Task (Title, Description, Status_ID, Creation_TS, Created_by)
VALUES ("Statistical analysis for Client X", "- check data for innacuracies\n - perform regression analysis", 1, CURRENT_TIMESTAMP, 3);
INSERT INTO Task (Title, Description, Status_ID, Creation_TS, Created_by)
VALUES ("Acquire Pizza", "Preferably without anchovies", 1, CURRENT_TIMESTAMP, 1);
INSERT INTO Task (Title, Description, Status_ID, Creation_TS, Created_by)
VALUES ("Call Grandma", "Strictly Business", 3, CURRENT_TIMESTAMP, 4);
INSERT INTO Task (Title, Description, Status_ID, Creation_TS, Created_by)
VALUES ("Determine pronunciation of '.gif'", "It's pronounced 'gif'!", 2, CURRENT_TIMESTAMP, 3);
INSERT INTO Task (Title, Description, Status_ID, Creation_TS, Created_by)
VALUES ("Write sample data for testing", "Very important, please complete asap", 1, CURRENT_TIMESTAMP, 4);



INSERT INTO Employee_Task
(Employee_ID, Task_ID)
VALUES
(1, 2);

INSERT INTO Task_Event
(Event_ID, Task_ID, Event_TS, Employee_ID)
VALUES
(1, 2, CURRENT_TIMESTAMP, 1);

INSERT INTO Task_Event (Event_ID, Task_ID, Event_TS, Employee_ID)
VALUES (2, 2, CURRENT_TIMESTAMP, 3);
VALUES (2, 2, CURRENT_TIMESTAMP, 5);
VALUES (3, 3, CURRENT_TIMESTAMP, 1);

/*
SELECT * FROM Employee;
SELECT * FROM Task;
SELECT * FROM Employee_Task;
SELECT * FROM Status;
SELECT * FROM Task_Event;
SELECT * FROM Event;
*/