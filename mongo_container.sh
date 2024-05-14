
#!/bin/bash

mongo_container_name="cs-inventory-helper-mongo-1"
default_username="mongoadmin"
default_password="secret"  

while true; do
    echo "Do you want to use the default database user? (yes/no)"
    read use_default

    if [[ $use_default == "yes" ]]; then
        if docker exec -it $mongo_container_name mongosh "mongodb://$default_username:$default_password@localhost:27017/?authSource=admin"; then
            echo "Successfully connected with default user: $default_username"
            break
        else
            echo "Connection failed with default user."
        fi
    else
        read -p "Enter the username to connect to MongoDB (press Enter to skip): " username

        if [ -n "$username" ]; then
            read -s -p "Enter the password: " password
            echo

            if docker exec -it $mongo_container_name mongosh "mongodb://$username:$password@localhost:27017/?authSource=admin"; then
                echo "Successfully connected with user: $username"
                break
            else
                echo "Connection failed or user '$username' does not exist."
            fi
        else
            docker exec -it $mongo_container_name bash
            break
        fi
    fi
done

