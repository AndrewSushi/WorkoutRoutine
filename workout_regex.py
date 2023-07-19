from re import findall
from json import loads

def extract_json_object(text):
    regex = r"(?s)\{[\s\S]*?\}"
    matches = findall(regex, text)
    json_object_as_string = matches[0]
    json_object_as_dictionary = loads(json_object_as_string)
    return json_object_as_dictionary

# text = """
# Sure, here is a JSON workout plan that will help you get big and strong: ```json { "days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], "exercises": [ ["Bench press", "Squats", "Deadlifts"], ["Overhead press", "Pull-ups", "Rows"], ["Incline dumbbell press", "Leg press", "Calf raises"], ["Tricep pushdowns", "Bicep curls", "Hammer curls"], ["Chest flyes", "Lat pulldowns", "Face pulls"], ["Abs"] ], "sets": [3, 3, 3, 3, 3, 3], "reps": [8, 8, 8, 12, 12, 15] } ``` This workout plan is designed to be done 6 days a week, with each workout lasting for 120 minutes. The exercises are designed to target all of the major muscle groups in your body. The sets and reps are designed to help you build strength and size. Here is a breakdown of the exercises in the workout plan: * **Bench press:** This is a compound exercise that works the chest, triceps, and shoulders. * **Squats:** This is a compound exercise that works the quads, hamstrings, and glutes. * **Deadlifts:** This is a compound exercise that works the entire posterior chain, including the hamstrings, glutes, lower back, and traps. * **Overhead press:** This is a compound exercise that works the shoulders and triceps. * **Pull-ups:** This is a bodyweight exercise that works the back and biceps. * **Rows:** This is a compound exercise that works the back and biceps. * **Incline dumbbell press:** This is an isolation exercise that works the upper chest. * **Leg press:** This is a machine exercise that works the quads. * **Calf raises:** This is an isolation exercise that works the calves. * **Tricep pushdowns:** This is an isolation exercise that works the triceps. * **Bicep curls:** This is an isolation exercise that works the biceps. * **Hammer curls:** This is an isolation exercise that works the biceps and forearms. * **Chest flyes:** This is an isolation exercise that works the chest. * **Lat pulldowns:** This is a machine exercise that works the lats. * **Face pulls:** This is an isolation exercise that works the rear deltoids. * **Abs:** This is a group of muscles that includes the rectus abdominis, obliques, and transversus abdominis. This is just a sample workout plan, and you may need to adjust it based on your individual needs and goals. However, it should give you a good starting point for building strength and size. Here are some additional tips for getting big and strong: * Eat a healthy diet that is high in protein. * Get enough sleep. * Be consistent with your workouts. * Progressively overload your muscles. * Listen to your body and take rest days when needed. With hard work and dedication, you can achieve your fitness goals.

# """

# json_object = extract_json_object(text)
# print(json_object)