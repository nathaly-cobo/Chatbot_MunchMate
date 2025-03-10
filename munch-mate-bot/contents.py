# SYS_CONTENT="""
# Objective: You are Munch-mate, a smart, friendly virtual assistant tasked with assisting users in finding food recommendations, especially restaurants, and making reservations for the users, in places located in Milpitas, California.

# Procedure:
# Greeting and Personalization

# 1. Begin with a warm greeting.
# Use the user's name if available.
# Personalize the interaction based on any known preferences (e.g., vegetarian, favorite cuisine).
# Inquiry on Restaurant Recommendations

# 2. Ask the user what specific information they are interested in related to restaurant recommendations.
# Offer categories such as cuisine type, dietary preferences, occasion (e.g., casual dining, date night), or specific features (e.g., outdoor seating, kid-friendly).
# Specific Inquiry Handling

# 4. Provide relevant and personalized restaurant recommendations based on the user's input.
# Include details such as cuisine type, menu highlights, atmosphere, and user reviews.
# Suggest a few options to give the user a choice.
# Additional Assistance and Follow-Up Actions

# 5. Offer to provide the exact location of the recommended restaurants.
# Ask if the user would like to make a reservation at any of the suggested places.
# If yes, proceed with making the reservation and confirm the details with the user.
# Offer any additional help, such as directions or information about parking.

# """

SYS_CONTENT="""
Objective: You are Munch-mate, a smart, friendly virtual assistant tasked with assisting users in finding food recommendations, especially restaurants, and making reservations for the users, in places located in Milpitas, California.
"""

RESTAURANTS={
  "milpitas": [
    {"name": "Annapoorna Authentic Indian Cuisine", "location": "770 E Tasman Dr, Milpitas, CA 95035", "phone": "(408) 894-9839", "type": "INDIA"},
    {"name": "Biryaniz", "location": "18 S Abbott Ave, Milpitas, CA 95035", "phone": "(408) 945-5700", "type": "INDIA"},
    {"name": "Hyderabad Dum Biryani", "location": "55 Dempsey Rd, Milpitas, CA 95035", "phone": "(408) 493-6133", "type": "INDIA"},
    {"name": "Anjappar Chettinad Indian Restaurant", "location": "458 Barber Ln, Milpitas, CA 95035", "phone": "(408) 435-5500", "type": "INDIA"},
    {"name": "Sen Dai Sushi", "location": "248 N Abel St, Milpitas, CA 95035", "phone": "(408) 263-1472", "type": "CHINESE"},
    {"name": "Darda Seafood Restaurant", "location": "296  Barber Ln, Milpitas, CA 95035", "phone": "(408) 433-5199", "type": "CHINESE"},
    {"name": "Koi Palace", "location": "768 Barber Ln, Milpitas, CA 95035", "phone": "(408) 432-8833", "type": "CHINESE"},
    {"name": "Won Kee BBQ Restaurant", "location": "206 Barber Ct, Milpitas, CA 95035", "phone": "(408) 526-0227", "type": "CHINESE"},
    {"name": "Sen Dai Sushi", "location": "248 N Abel St, Milpitas, CA 95035", "phone": "(408) 263-1472", "type": "JAPANESE"},
    {"name": "Sushi Adachi", "location": "668 Barber Ln, Milpitas, CA 95035", "phone": "(408) 432-6270", "type": "JAPANESE"},
    {"name": "Uotomo Sushi", "location": "442 W Calaveras Blvd, Milpitas, CA 95035", "phone": "(408) 719-8882", "type": "JAPANESE"},
    {"name": "Bento Xpress", "location": "206 Barber Ct, Milpitas, CA 95035", "phone": "(408) 255-1388", "type": "JAPANESE"},
    {"name": "Zahir's Bistro", "location": "579 S Main St, MilpitasCA 95035", "phone": "(408) 946-4000", "type": "AMERICAN"},
    {"name": "In-N-Out Burger", "location": "50 Ranch Dr, Milpitas, CA 95035", "phone": "(800) 786-1000", "type": "AMERICAN"},
    {"name": "Denny's", "location": "333 S.Abbott, Miplitas, CA 95035", "phone": "(408) 262-9090", "type": "AMERICAN"},
    {"name": "Jack in the Box", "location": "1740 S Main St, MilpitasCA 95035", "phone": "(408) 956-8655", "type": "AMERICAN"},
    {"name": "Starbucks", "location": "127 Ranch Dr, Milpitas, CA 95-35", "phone": "(408) 934-9810", "type": "AMERICAN"},
    {"name": "Subway", "location": "1476 N Milpitas Blvd, Milpitas, CA 95035", "phone": "(408) 946-0221", "type": "AMERICAN"},
    {"name": "Burger King", "location": "602 Great Mall Dr Fc 2a, Milpitas, CA 95035", "phone": "(408) 791-6222", "type": "AMERICAN"},
  ],
  "san jose": [
    {"name": "fake name", "location": "just in san jose", "phone": "123456789"},
  ]
}

TOOLS=[
    {
        "type": "function",
        "function": {
            "name": "get_restaurants",
            "description": "Get the restaurants in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. Milpitas",
                    },
                    "type": {
                        "type": "string",
                        "description": "The type of the restaurant, e.g: American",
                    },
                },
                "required": ["location"],
            },
        }
    }
]

















