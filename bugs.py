#
# Cathrine Bien-Aime 
#
# bugs-updated.py
#
# Calculates the number of bugs collected during a week
#
# Input: Number of bugs collected each day of the week
#             
# Processing: total = total + bugs
# 
# Output: Total number of bugs collected during a week
#

def main():
    print("Bugs Collector App ...")
    print()

    # Initialize accumulator
    total=0

    # Calculate total number of bugs collected over the week
    for day in ["monday","Tuesday","Wednesday","Thursday","Friday",
                "Saturday","Sunday"]:
        # Prompt user for number of bugs collected that day
        bugs = eval(input("\t" + day + ": "))
        # Update accumulator
        total = total + bugs


    # Display result
    print()
    print("Total bugs collected this week:", total)

main()
 
    
