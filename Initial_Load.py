import os 
import random
import numpy as np 
import pandas as pd 
from faker import Faker




def generate_fake_users(data_amount=70_000,real_amount = 35_000,column_names =['Fname','Lname','Age','Zip','Email','Tnumber','Pmethod']):
    tries = 0 
    users = "Start" 
    while len(users) < real_amount or tries > 10:
        faker = Faker()
        email_provider = ['gmail.com','yahoo.at','hotmail.com','gmx.at','web.at']
        delimiter = [".","_","-"]
        zip_code = ['1010', '1020', '1030', '1040', '1050', '1060', '1070', '1080', '1090',
        '1110', '1120', '1130', '1140', '1150', '1160', '1170', '1180', '1190','1200','1210','1220','1230']
        payment_method = ['Credit Card','Paypal','Sofortueberweisung']
        amount_of_data = data_amount
        # Name Generation
        fnames = [faker.first_name() for x in range(amount_of_data)]
        lnames = [faker.last_name() for x in range(amount_of_data)]
        
        # Age Generation -- Centred around 30 years
        age    = np.random.normal(30,4,amount_of_data)
        age    = [int(x) for x in age]

        # Zip Code Generation
        zip_codes = [zip_code[random.randint(0,21)] for x in range(amount_of_data)]

        # Email Generation 
        email = [f'{fnames[i]}{delimiter[random.randint(0,2)]}{lnames[i]}@{email_provider[random.randint(0,4)]}' for i in range(amount_of_data)]

        #Telephone Number
        tel = [str(faker.phone_number()).replace("x","").replace("(","").replace(")","").replace(".","").replace("-","").replace("+","").strip()[:10] for x in range(amount_of_data)]

        # Payment Methods 
        payment_methods = [payment_method[random.randint(0,2)] for x in range(amount_of_data) ]

        # Returning a Pandas DataFrame 
        users = pd.DataFrame(zip(fnames,lnames,age,zip_codes,email,
                                tel,payment_methods),columns=column_names)
        
        tries += 1 
        users = users.drop_duplicates(subset=['Fname','Lname','Age','Email']) 
        if len(users) < real_amount:
            data_amount = int(data_amount*1.1)
            print(f"Data_Amount increased to\t{data_amount}")
            continue
        users = users.iloc[:real_amount]
    users = users.reset_index()
    users = users.rename(columns={'index':'user_id'})
    users.to_csv("Customers.csv",index=False,sep=",",encoding='utf-8')
    print(f"{real_amount} Fake User were generated!")

    # MISSING RETURN
def generate_fake_escooters(amount_of_data=2500,column_names = ['Rented','Battery']):

    rented = [True,False]
    rents = [rented[random.randint(0,1)] for x in range(amount_of_data)]
    battery = np.random.normal(50,10,amount_of_data)
    battery = [int(x) for x in battery]
 
    scooters = pd.DataFrame(zip(rents,battery),columns=column_names)
    scooters.to_csv("Escooter.csv",index=False,sep=",",encoding='utf-8')
    print(f"{amount_of_data} Fake Scooters were generated!")
def generate_fake_usage(amount_of_data=500_000,customer_id_range=35_000,escooter_id_range=2500
                        ,schema = ['Escooter_id','User_id','Starting_Geolat','Starting_Geolong','Ending_Geolat','Ending_Geolong','Duration'],
                        table_name = 'Usage'):
    # Geo-Location of Vienna 
    geo_long = [16.219,16.475]
    geo_lat = [48.322,48.111]

    # Generating Random Data 
    user_id = np.random.randint(1,customer_id_range,amount_of_data)
    escooter_id  = np.random.randint(1,escooter_id_range,amount_of_data)
    durations = np.array([int(random.normalvariate(15,3)) for x in range(amount_of_data)])
    starting_Geolong = np.random.uniform(geo_long[0],geo_long[1],amount_of_data)
    ending_Geolong = np.random.uniform(geo_long[0],geo_long[1],amount_of_data)
    ending_Geolat = np.random.uniform(geo_lat[0],geo_lat[1],amount_of_data)
    starting_Geolat = np.random.uniform(geo_lat[0],geo_lat[1],amount_of_data)

    # Preparing DataSet 
    usage = pd.DataFrame(zip(escooter_id,user_id,starting_Geolat,starting_Geolong,
                            ending_Geolat,ending_Geolong,durations),
                            columns=schema)

    usage.to_csv(table_name+".csv",index=False,sep=",",encoding='utf-8')
    print(f"{amount_of_data} Fake Usage was generated!")






    






