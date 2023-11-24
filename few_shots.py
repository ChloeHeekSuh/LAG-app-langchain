few_shots = [
  {
    'Question': "How many t-shirts do we have left for nike in extra small size and white color?",
    'SQLQuery': "SELECT SUM(stock_quantity) as total_quantity FROM atliq_tshirts.t_shirts WHERE brand='Nike' AND color='White' AND size = 'XS';",
    'SQLResult': "Result of the SQL query",
    'Answer': "23"
  },
  {
    'Question': "How much is the price of the inventory for all small size t-shirts?",
    'SQLQuery': "SELECT SUM(stock_quantity*price) as total_price FROM atliq_tshirts.t_shirts WHERE size = 'S';",
    'SQLResult': "Result of the SQL query",
    'Answer': "16375"
  },
  {
    'Question': "If we have to sell all the Adidas's t-shirts today with discounts applied, how much revenue our store will generate with the discount price?",
    'SQLQuery': "WITH Adidas AS (SELECT SUM(price * stock_quantity) AS total_amount, t_shirt_id FROM t_shirts WHERE brand = 'Adidas' GROUP BY t_shirt_id) SELECT SUM(a.total_amount * (1 - COALESCE(discounts.pct_discount, 0) / 100)) AS total_revenue FROM Adidas a LEFT JOIN discounts ON a.t_shirt_id = discounts.t_shirt_id;",
    'SQLResult': "Result of the SQL query",
    'Answer': "21129.50"
  },
  {
    'Question': "If we have to sell all the Adidas's t-shirts today, how much revenue our store will generate?",
    'SQLQuery': "SELECT SUM(price*stock_quantity) FROM atliq_tshirts.t_shirts WHERE brand = 'Adidas';",
    'SQLResult': "Result of the SQL query",
    'Answer': "22056"
  },
  {
    'Question': "How many white color Adidas's t-shirts we have are available?",
    'SQLQuery': "SELECT SUM(stock_quantity) as total_white_Shirts FROM t_shirts WHERE brand = 'Adidas' and color = 'White';",
    'SQLResult': "Result of the SQL query",
    'Answer': "198"
  }
]