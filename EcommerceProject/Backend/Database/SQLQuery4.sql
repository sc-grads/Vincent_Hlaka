USE [furniture]
GO

/****** Object:  Table [dbo].[Order_details]    Script Date: 2023/03/10 13:16:59 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Order_details](
	[order_details_id] [int] IDENTITY(1,1) NOT NULL,
	[product_id] [int] NULL,
	[product_qty] [int] NULL,
	[product_price] [int] NULL,
	[order_id] [nvarchar](50) NOT NULL,
	[subtotal] [int] NULL,
 CONSTRAINT [PK_Order_details] PRIMARY KEY CLUSTERED 
(
	[order_details_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[Order_details]  WITH CHECK ADD  CONSTRAINT [FK_Order_details_Order.Tbl] FOREIGN KEY([order_id])
REFERENCES [dbo].[Order.Tbl] ([order_id])
GO

ALTER TABLE [dbo].[Order_details] CHECK CONSTRAINT [FK_Order_details_Order.Tbl]
GO

ALTER TABLE [dbo].[Order_details]  WITH CHECK ADD  CONSTRAINT [FK_Order_details_Product] FOREIGN KEY([product_id])
REFERENCES [dbo].[Product] ([product_id])
GO

ALTER TABLE [dbo].[Order_details] CHECK CONSTRAINT [FK_Order_details_Product]
GO


