USE [furniture]
GO

/****** Object:  Table [dbo].[Customer]    Script Date: 2023/03/10 13:16:43 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Customer](
	[customer_id] [int] IDENTITY(1,1) NOT NULL,
	[customer_email] [nvarchar](50) NULL,
	[first_name] [nvarchar](50) NULL,
	[last_name] [nvarchar](50) NULL,
	[password] [nvarchar](50) NULL,
	[address] [nvarchar](max) NULL,
	[postcode] [nvarchar](50) NULL,
	[city] [nvarchar](50) NULL,
	[phone] [nvarchar](50) NOT NULL,
 CONSTRAINT [PK_Customer] PRIMARY KEY CLUSTERED 
(
	[customer_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO


