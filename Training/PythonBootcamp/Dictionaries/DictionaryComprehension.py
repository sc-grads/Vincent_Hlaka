# exercise 24

# given...

visits = {'Monday': 5000,
          'Tuesday': 3000,
          'Wednesday': 4000,
          'Thursday': 4500,
          'Friday': 5000,
          'Saturday': 2000,
          'Sunday': 1500
          }

# work
total_visits = sum(visits.values())
print(total_visits)  # gives 25000

percentage = {k: (v / total_visits) * 100 for k, v in visits.items()}
print(percentage)
# {'Monday': 20.0, 'Tuesday': 12.0, 'Wednesday': 16.0,
# 'Thursday': 18.0, 'Friday': 20.0, 'Saturday': 8.0, 'Sunday': 6.0}
