import APSJ20G2_SALES_DATA_ANALYSIS.connector as con
def reg_user():
        try:
                print("Enter your name:")
                name = input()
                print("#" * 50)
                print("Enter your email")
                email = input()
                print("#" * 50)
                query = "insert into reg_users (name,email) values('{}','{}');".format(name, email)
                con.cursor.execute(query)
                con.dbc.commit()
                print("SUCCESSFULLY REGISTERED")
        except Exception as e:
                print("The Error is: "+e)