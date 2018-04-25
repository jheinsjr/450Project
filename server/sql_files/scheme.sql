DROP TABLE IF EXISTS Employee;
DROP TABLE IF EXISTS Task;
DROP TABLE IF EXISTS Employee_Task;
DROP TABLE IF EXISTS Status;
DROP TABLE IF EXISTS Task_Event;
DROP TABLE IF EXISTS Event;

CREATE TABLE Employee (
    Employee_ID integer ,
    First_Name varchar(30),
    Last_Name varchar(50) NOT NULL,
    Admin BOOLEAN NOT NULL,
    Username varchar(30) NOT NULL,
    Password varchar(30) NOT NULL,
    PRIMARY KEY (Employee_ID)
);

CREATE TABLE Status (
    Status_ID integer,
    Description varchar(50),
    PRIMARY KEY (Status_ID)
);

CREATE TABLE Task (
    Task_ID integer ,
    Title varchar(30) NOT NULL,
    Description varchar(400),
    Status_ID integer NOT NULL,
    Creation_TS TIMESTAMP,
    Update_DT DATETIME,
    Created_by integer NOT NULL,
    Updated_by integer,
    PRIMARY KEY (Task_ID),
    FOREIGN KEY (Status_ID) REFERENCES Status(Status_ID),
    FOREIGN KEY (Created_by) REFERENCES Employee(Employee_ID),
    FOREIGN KEY (Updated_by) REFERENCES Employee(Employee_ID)
);

CREATE TABLE Employee_Task (
    Employee_ID integer NOT NULL,
    Task_ID integer NOT NULL,
    PRIMARY KEY (Employee_ID, Task_ID),
    FOREIGN KEY (Employee_ID) REFERENCES Employee(Employee_ID),
    FOREIGN KEY (Task_ID) REFERENCES Task(Task_ID)
);

CREATE TABLE Event (
    Event_ID integer ,
    Title varchar(15) NOT NULL,
    Description varchar(50) NOT NULL,
    PRIMARY KEY (Event_ID)
);

CREATE TABLE Task_Event (
    Event_ID integer NOT NULL,
    Task_ID integer NOT NULL,
    Event_TS TIMESTAMP NOT NULL,
    Employee_ID integer NOT NULL,
    PRIMARY KEY (Event_ID,Task_ID),
    FOREIGN KEY (Event_ID) REFERENCES Event(Event_ID),
    FOREIGN KEY (Task_ID) REFERENCES Task(Task_ID),
    FOREIGN KEY (Employee_ID) REFERENCES Employee(Employee_ID)
);

CREATE TRIGGER employee_task_relation AFTER INSERT ON Task_Event
    BEGIN
    INSERT OR IGNORE INTO Employee_Task(Employee_ID,Task_ID) 
        VALUES (new.Employee_ID, new.Task_ID);
    UPDATE Task
        Set Update_DT = date('now')
        WHERE Task.Task_ID = new.Task_ID;
    END;

