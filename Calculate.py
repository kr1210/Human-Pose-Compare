from calculations import get_Score

action = "punch - side"
lookup = "lookup.pickle"
video = "alwin_punch_2.mp4"

g = get_Score(lookup)

final_score,score_list = g.calculate_Score(video,action)
print(final_score)
print(score_list)