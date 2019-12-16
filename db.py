import pymysql
import datetime

connection = {
    'host':'localhost',
    'user':'root',
    'password':None,
    'database':'dhl',
    'autocommit': True,
}

conn = pymysql.connect(**connection)
cur = conn.cursor()

def make_insertion(data):
    if data['Sales Document'] == "Sales Document":
        pass
    else:
        a  = data['Sales Document']
        b  = data['Delivery Number']
        c  = data['Plant']
        d  = data['Sold-to party']
        e  = data['Created on']
        f  = data['Material']
        id = '{}{}'.format(a,f)
        g  = data['Material Description']
        h  = data['Order Quantity']
        i  = data['Carrier']
        seconds = (e - 25569) * 86400.0
        cre = datetime.datetime.utcfromtimestamp(seconds)

        # print (data['Sales Document'], data['Delivery Number'], data['Plant'], data['Sold-to party'], data['Created on'], data['Material'], data['Material Description'], data['Order Quantity'], data['Carrier'])
        q = "REPLACE INTO orders(`T_id`,`Order_No`, `Delivery_No`, `Warehouse`, `Customer`, `Order_Date`, `Product_ID`, `Product_Description`, `Qty`, `Transporter`) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(id, a, b, c, d, cre, f, g, h, i)
        cur.execute(q)
