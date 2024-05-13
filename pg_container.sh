#!/bin/bash

while true; do
    read -p "Enter the username to connect to PostgreSQL (press Enter to skip): " username

    if [ -n "$username" ]; then
        if docker exec cs-inventory-helper-postgres-1 psql -U postgres -tAc "SELECT 1 FROM pg_roles WHERE rolname='$username'" | grep -q 1; then
            docker exec -it cs-inventory-helper-postgres-1 psql -U "$username"
            break
        else
            echo "User '$username' does not exist."
        fi
    else
        docker exec -it cs-inventory-helper-postgres-1 bash
        break
    fi
done
