USE [OurFirstDatabase]
GO

INSERT INTO [dbo].[personalinfo]
           ([FirstName]
           ,[LastName]
           ,[DoB]
           ,[ID])
     VALUES
           ('Vincent',
           'Hlaka'
           ,'02/05/1985'
           ,45828)
GO

Select * from [dbo].[personalinfo]
GO
