# Queris for users
add_user = '''
    INSERT INTO {0}USERS (ID, USER_NAME, DESIRED_NAME) VALUES ({1}, "{2}", "{3}")
'''

find_user_for_id = '''
    SELECT ID FROM {}USERS WHERE ID = {}
'''

get_desire_user_name = '''
    SELECT DESIRED_NAME FROM {0}USERS WHERE ID = {1}
'''

set_locate_for_user = '''
    UPDATE {0}USERS SET LANG = "{2}" WHERE ID = {1}
'''

get_locate_for_user = '''
    SELECT LANG FROM {0}USERS WHERE ID = {1}
'''




# Queris for products
add_product = '''
    INSERT INTO PRODUCTS (NAME_PRODUCT, CATEGORY_ID, IMAGE_URL, DATE_TIME_ADD, USER_ID_ADD) VALUES ("{0}", {1}, "{2}", "{3}", {4})
'''

del_product_for_id = '''
    DELETE FROM PRODUCTS WHERE ID = {}
'''

del_product_for_category = '''
    DELETE FROM PRODUCTS WHERE CATEGORY_ID = {}
'''

add_product_type = '''
    INSERT INTO PRODUCT_TYPES (NAME_TYPES, IMAGE_URL, DATE_TIME_ADD, USER_ID_ADD) VALUES ("{0}", "{1}", "{2}", {3})
'''

get_product_type = '''
    SELECT ID, NAME_TYPES, IMAGE_URL, DATE_TIME_ADD, USER_ID_ADD FROM PRODUCT_TYPES
'''

select_product_from_product_type = '''
    SELECT ID FROM PRODUCTS WHERE CATEGORY_ID = {}
'''

del_product_type = '''
    DELETE FROM PRODUCTS WHERE ID = {}
'''


# Queris for basket

add_product_in_basket = '''
    INSERT INTO {0}BASKET (USER_ID, PRODUCT_ID) VALUES ({1}, {2})
'''


get_products_in_basket = '''
    SELECT PRODUCT_ID FROM {0}BASKET WHERE USER_ID = {1}
'''

del_product_in_basket = '''
    DELETE FROM {0}BASKET WHERE ID = {1}
'''

del_all_products_in_basket = '''
    DELETE FROM {0}BASKET WHERE USER_ID = {1}
'''



# Create tables scripts


table_users = '''
    CREATE TABLE IF NOT EXISTS {}USERS
    (
        ID INT,
        USER_NAME STRING,
        DESIRED_NAME STRING,
        USER_FIRST_NAME STRING,
        USER_SECOND_NAME STRING,
        PHONE INTEGER,
        LANG STRING
    )
'''

table_users_activity = '''
    CREATE TABLE IF NOT EXISTS {}USERS_ACTIVITY
    (
        USER_ID INT,
        USER_ACTIVITY_TEG STRING,
        DATE_TIME STRING
    )
'''

table_products = '''
    CREATE TABLE IF NOT EXISTS PRODUCTS
    (
        ID INTEGER PRIMARY KEY,
        NAME_PRODUCT STRING,
        CATEGORY_ID INT
        IMAGE_URL STRING,
        DATE_TIME_ADD STRING,
        USER_ID_ADD INT
    )
'''

table_product_types = '''
    CREATE TABLE IF NOT EXISTS PRODUCT_TYPES
    (
        ID INTEGER PRIMARY KEY,
        NAME_TYPES STRING,
        IMAGE_URL STRING,
        DATE_TIME_ADD STRING,
        USER_ID_ADD INT
    )
'''

table_basket = '''
    CREATE TABLE IF NOT EXISTS {}BASKET
    (
        USER_ID INT,
        PRODUCT_ID INT
    )
'''