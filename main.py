import turtle
import pandas

counter = 0
screen = turtle.Screen()
screen.title("US STATES GAMES")
image = "D:/100python/day15to25/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

us_data = pandas.read_csv("D:/100python/day15to25/us-states-game-start/50_states.csv")
state_names = us_data['state']
state_names = state_names.tolist()


def get_user_answer():
    return screen.textinput(title=f"{counter} out of 50 done", prompt="Name another state").title()
    


def mark_on_map(answer_text):
    t=turtle.Turtle()
    t.hideturtle()
    t.penup()
    selected_state = us_data[us_data.state == answer_text]
    t.goto(int(selected_state.x),int(selected_state.y))
    t.write(answer_text)


already_answered = []

while True:
    answer_text =  get_user_answer()
    if(answer_text == 'Exit'):
        break
    if answer_text in state_names and answer_text not in already_answered:
        counter += 1
        mark_on_map(answer_text)
        already_answered.append(answer_text)
        print("correct")
    if counter == 50:
        print("all 50 done")
        break


missed_states = [st for st in state_names if st not in already_answered]


df = pandas.DataFrame({"States" : missed_states})
df.to_csv("D:/100python/day15to25/us-states-game-start/states_to_learn.csv")
