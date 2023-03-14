USE [furniture]
GO

/****** Object:  Table [dbo].[Order.Tbl]    Script Date: 2023/03/10 13:16:52 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Order.Tbl](
	[order_id] [nvarchar](50) NOT NULL,
	[order_no] [int] IDENTITY(1,1) NOT NULL,
	[order_date] [datetime] NULL,
	[order_total] [int] NULL,
	[costumer_id] [int] NULL,
	[shipping_date] [datetime] NULL,
	[is_delivered] [nvarchar](50) NULL,
 CONSTRAINT [PK_Order.Tbl] PRIMARY KEY CLUSTERED 
(
	[order_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[Order.Tbl]  WITH CHECK ADD  CONSTRAINT [FK_Order.Tbl_Customer] FOREIGN KEY([costumer_id])
REFERENCES [dbo].[Customer] ([customer_id])
GO

ALTER TABLE [dbo].[Order.Tbl] CHECK CONSTRAINT [FK_Order.Tbl_Customer]
GO


