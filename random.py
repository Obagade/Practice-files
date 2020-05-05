import random

plans = ["go to the movies",
		 "Watch Football",
		 "Learn Javascript"]

places =["Monte Carlo",
         "Santorini",
         "Philadephia"]

random_plan = random.choice(plans);
random_places = random.choice(places);

print(f"You can {random_plan} in {random_places}")