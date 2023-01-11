from email.mime import image
import turtle
import pandas

screen = turtle.Screen()
screen.title("liloz in US")
image = "blank_states_img.gif" 
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
user_st = []
while len(user_st) < 50:
    user_answer = screen.textinput(f"Guess the State {len(user_st)}/50","What is a state name?").title()
    if user_answer == "Exit":
        missing_state = []
        for state in all_states:
            if state not in user_st:
                missing_state.append(state)
        new = pandas.DataFrame(missing_state)
        new.to_csv("lern.csv")
    

    if user_answer in all_states:
        user_st.append(user_answer)
        t= turtle.Turtle()
        t.hideturtle()
        t.penup()
        s = data[data.state == user_answer]
        t.goto(int(s.x),int(s.y))
        t.write(user_answer)
turtle.mainloop()
