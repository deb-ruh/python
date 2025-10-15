from graphics import *

# Intro and greetings
print("\nHello there!")
print("Let's see your average savings in a year and compare your monthly savings.\n")

# Ask user what year they want to see their saving average
year = input("What year do you want to see your savings average? ")

# List the months
months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "July", "Aug", "Sept", "Oct", "Nov", "Dec")

# Initialize variables and list
total = 0
amount_list = []

# Get user input for monthly savings
for month in months:
    while True:
        amount = input(f"How much did you save in {month}? ")
        if amount.isdigit():
            amount_list.append(int(amount))
            total += int(amount)
            break
        else:
            print(f"Please enter a positive number or 0 for {month}.")

# Calculate average savings
average = total / 12
print(f"Your average savings for the year {year} is {round(average, 2)} pesos.")

# Get the highest saving in twelve months to scale the bars
max_val = max(amount_list)

# Create the graphics window
win_width, win_height = 1080, 650
win = GraphWin(f"Average Savings for {year}", win_width, win_height)
win.setBackground("beige")

# Define margins for better spacing
left_margin, right_margin = 220, 50
top_margin, bottom_margin = 100, 80
chart_width = win_width - left_margin - right_margin
chart_height = win_height - top_margin - bottom_margin

# Draw title
title_text = Text(Point(win_width / 2, top_margin / 2), f"Monthly Savings for {year}")
title_text.setSize(20)
title_text.setStyle("bold")
title_text.setTextColor("black")
title_text.draw(win)

# Draw average savings text
avg_savings_text = Text(Point(win_width / 2, top_margin / 1.5), f"Monthly Savings Average: ₱{round(average, 2)}")
avg_savings_text.setSize(14)
avg_savings_text.setStyle("bold italic")
avg_savings_text.setTextColor("black")
avg_savings_text.draw(win)

# Draw axes
x_axis = Line(Point(left_margin, win_height - bottom_margin), Point(win_width - right_margin, win_height - bottom_margin))
y_axis = Line(Point(left_margin, top_margin), Point(left_margin, win_height - bottom_margin))
x_axis.setWidth(2)
y_axis.setWidth(2)
x_axis.draw(win)
y_axis.draw(win)

# Label axes
x_label = Text(Point(left_margin + chart_width / 2, win_height - bottom_margin / 2), "Months")
x_label.setSize(14)
x_label.draw(win)

y_label = Text(Point(left_margin / 2.5, win_height / 2), "Amount Saved")
y_label.setSize(14)
y_label.setStyle("bold")
y_label.draw(win)

# Define bar width and spacing
bar_width = (chart_width / len(months)) * 0.7
bar_spacing = (chart_width / len(months)) * 0.3

# Get the percentage of each bar and multiply it by the chart's height. It keeps proportions correct and makes dynamic scaling possible for any data range.
scaled_values = [(val / max_val) * chart_height for val in amount_list]

# Draw grid lines and Y-axis labels
step = max_val / 5  # Divide scale into 5 parts
for i in range(6):
    y_value = step * i
    y_position = win_height - bottom_margin - (y_value / max_val) * chart_height
    
    # Y-axis labels
    label = Text(Point(left_margin - 40, y_position), str(int(y_value)))
    label.setSize(10)
    label.draw(win)
    
    # Horizontal grid lines
    grid_line = Line(Point(left_margin, y_position), Point(win_width - right_margin, y_position))
    grid_line.setFill("lightgray")
    grid_line.draw(win)

# Draw bars
for i, (month, bar_height) in enumerate(zip(months, scaled_values)):
    x1 = left_margin + i * (bar_width + bar_spacing) + (155/12)
    x2 = x1 + bar_width
    y1 = win_height - bottom_margin
    y2 = y1 - bar_height
    
    # Draw the bar
    bar = Rectangle(Point(x1, y1), Point(x2, y2))
    bar.setFill("light green")
    bar.setOutline("black")
    bar.draw(win)
    
    # Draw month labels
    label_text = Text(Point((x1 + x2) / 2, y1 + 20), month)
    label_text.setSize(12)
    label_text.draw(win)
    
    # Draw values on top of bars
    value_text = Text(Point((x1 + x2) / 2, y2 - 10), str(amount_list[i]))
    value_text.setSize(12)
    value_text.setStyle("bold")
    value_text.draw(win)

# Close window on click
Text(Point(left_margin + chart_width / 2, win_height - 20), "Click anywhere to close").draw(win)
win.getMouse()
win.close()
