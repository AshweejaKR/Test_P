# =============================================================================
# ======================= IMPORT INBUILT LIB/MODULES ==========================
import json

# =============================================================================
# ========================== GLOBAL VARIABLES =================================
global data

# =============================================================================
data = ""

# =============================================================================
# =============================================================================
def get_api(user_input = "2"):
    global data
    
    ''' #for test debug
    #value1 = "NA"
    #value2 = "NA"
    #value3 = "NA"
    #value4 = "NA"
    #value5 = "NA"
    
    data =  {
                "key1" : value1,
                "key2" : value2,
                "key3" : value3,
                "key4" : value4,
                "key5" : value5
            }
    '''
    print("get_api() ... !")
    if(user_input != "2"):
        app_id = data["APP_ID"]
        api_secret = data["API_SECRET"]
        username = data["USERNAME"]
        password = data["PASSWORD"]
        twofa = data["TWOFA"]

    if(user_input == "0"):
        app_id = input("Enter Your APP_ID: \n")
        api_secret = input("Enter Your API_SECRET:\n")
    elif(user_input == "1"):
        username = input("Enter Your USERNAME:\n")
        password = input("Enter Your PASSWORD:\n")
        twofa = input("Enter Your DOB:\n")
    elif(user_input == "2"):
        app_id = input("Enter Your APP_ID: \n")
        api_secret = input("Enter Your API_SECRET:\n")
        username = input("Enter Your USERNAME:\n")
        password = input("Enter Your PASSWORD:\n")
        twofa = input("Enter Your DOB:\n")
    else:
        print("WRONG INPUT")
        print("QUITING ... !")
        exit(1)
        
    data =  {
                "APP_ID" : app_id,
                "API_SECRET" : api_secret,
                "USERNAME" : username,
                "PASSWORD" : password,
                "TWOFA" : twofa
            }

# =============================================================================
# =============================================================================
def update_api():
    global data

    print("update_api() ... !")

    api_path = 'src/api_data.json'
    try:
        with open(api_path) as data_file:    
            data = json.load(data_file)
        print("*********************************************************************")
        print("Select an operation to perform:")
        print("")
        print("MASTER_MENU:")
        print("0.  UPDATE YOUR API SECRET")
        print("1.  UPDATE YOUR USER LOGIN INFO")
        print("2.  UPDATE ALL")
        print("")
        print("=====================================================================")
        print("")
        user_input = input("Please select an option :\n")
        get_api(user_input)
    except FileNotFoundError as err:
        print(err)
        get_api()
    except Exception as err:
        print(err)
    finally:
        print("updating api ... \n")
        with open(api_path, 'w') as outfile:
            json.dump(data, outfile, sort_keys=True, indent=4)
            print("Saved Successfully ...!")

# =============================================================================
# =============================================================================
update_api()

# =============================================================================
