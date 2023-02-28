

CREATE TABLE [dbo].[personalinfo](
	[FirstName] [varchar](50) NULL,
	[LastName] [varchar](50) NULL,
	[DoB] [datetime] NULL,
	[ID] [int] NOT NULL
) ON [PRIMARY]
GO





CREATE TABLE [dbo].[personalinfo](
	[FirstName] [varchar](50) NULL,
	[LastName] [varchar](50) NULL,
	[DoB] [datetime] NULL,
	[ID] [int] NOT NULL,
 CONSTRAINT [PK_personalinfo] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

