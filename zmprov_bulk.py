import os
import pandas as pd
from time import sleep

"""
Created By Marius Niehaus 
Python script to create users from a csv file with passwords 
You need to su zimbra and then run the script like ex as zimbra user python3 script_name.py 

Zimbra attributes
email = name
pass = password
first_name = givenName 
last_name = sn
display_name = displayName
init = initials
discr = description
phone = telephoneNumber
company = company
job_title = title
csv must be in this format and above column names
{name@domain} {password} [attr1 value1 [attr2 value2...]]
email password name surname template format
su - zimbra -c "zmprov ca acc1@rsateam.co.za password01 displayName 'Jon Do'"; sample

"""


def CreateUser(create):
    """ Function to send new user creation to zimbra """
    # sleep(2)
    # return os.system(create)
    print(create)


# csv file
filename = "test.csv"

# Server connection paramaters create account command
create_acc = "su - zimbra -c "
zmprov = "zmprov ca"
# Create Dataframe from csv
list_df = pd.read_csv(filename, header=0, sep=';')

no_of_rows = len(list_df)
i = 0
while i < no_of_rows:
    name = list_df.iloc[i]["Email"]
    password = list_df.iloc[i]["Pass"]
    displayName = list_df.iloc[i]["FirstName"] + " " + list_df.iloc[i]["LastName"]

    # Build string to run command zmprov create user
    create_string = create_acc + "\"" + zmprov + " " + name + " " + password + " " + "displayName" + " " + "\'" + displayName + "\'" + "\"" + ";"

    # Call function passing command to to create users in zimbra
    CreateUser(create_string)
    i = i + 1
