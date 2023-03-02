--Creating a table [sales].[storenew]
CREATE TABLE [AdventureWorks2019].[sales].[storesnew] (
store_id INT  PRIMARY KEY NOT NULL,
sales INT
)
--Create a table
CREATE TABLE [AdventureWorks2019].[sales].[visists] (
visit_ID INT PRIMARY KEY IDENTITY (1,1),
first_name VARCHAR (50) not null,
last_name VARCHAR (50) not null,
visited_at datetime,
phone VARCHAR (20) not null,
store_id INT not null,
foreign key (store_id) References sales.storesnew (store_id)	
)

SELECT * From [AdventureWorks2019].[sales].[visists]
select * from [person].[person]

select [BusinessEntityID],[FirstName],[MiddleName],[Title]
 from [Person].[Person]
 where title ='mr.'

 -- SELECT INTO TEMPTABLE M1 (temporary table)
 select [BusinessEntityID],[FirstName],[MiddleName],[Title]
 into #TempPersonTable
 from [Person].[Person]
 where title = 'mr.'

 DROP TABLE #TempPersonTable

 -- CREATE TEMPTABLE AND POPULATE IT M2
 CREATE TABLE #TempPersonTable (
 BusinessEntityID INT,
 FirstName NVARCHAR(50),
 LastName NVARCHAR(50),
 Title NVARCHAR(50)
 )

 -- insert into for temptable

 Insert into #TempPersonTable
select [BusinessEntityID],[FirstName],[LastName],[Title]
 from [person].[person]
 where title = 'mr.'
 
 select * from #TempPersonTable