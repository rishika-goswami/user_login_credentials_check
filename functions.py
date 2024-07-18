def login(user, hashed_pwd, username, password):
    flag=1
    for i in password:
        if hashed_pwd==i:
            print("User logged in successfully!")
            flag=0
            break             

    if(flag) or user not in username:
        print("Unsucessful login attempt.\nPlease try again!")