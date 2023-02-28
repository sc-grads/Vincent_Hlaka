/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (1000) [FirstName]
      ,[LastName]
      ,[DoB]
      ,[ID]
  FROM [OurFirstDatabase].[dbo].[personalinfo]