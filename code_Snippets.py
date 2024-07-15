from datetime import datetime, timedelta

# Current date and time
now = datetime.now()
print("Current Date and Time:", now)

# Adding 10 days to the current date and time
future_date = now + timedelta(days=10)
print("Date and Time after 10 days:", future_date)

# Subtracting 5 hours from the current date and time
past_time = now - timedelta(hours=5)
print("Date and Time 5 hours ago:", past_time)

#############################################################
