def padel_court_cost(court_type):
    if court_type == "indoor" :
        return 30 
    
    elif court_type == "outdoor" :
        return 20
    
    

def rackets_cost(racket_brand):
    if racket_brand =="bullpadel":
        return 100
    elif racket_brand =="nox":
        return 140
    elif racket_brand =="siux":
          
        return 200
    else:
        False
        


def padel_balls_cost(ball_boxes):
    if ball_boxes==1:
        return 2
    elif ball_boxes==2:
        return 3.5
    elif  ball_boxes==3:
        return 5
 
    

def padel_game_cost():
    court_type= input("the court type")
    racket_brand =input("racket brand")
    ball_boxes= int(input("number of ball boxes"))
    result= padel_court_cost(court_type)+ rackets_cost(racket_brand) +padel_balls_cost(ball_boxes)
    return result

print(padel_game_cost())