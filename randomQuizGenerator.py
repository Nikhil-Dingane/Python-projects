import random

   # The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New\
   Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West\
   Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

i=1
states=list(capitals.keys())
answers=list(capitals.values())
   # Generate 35 quiz files.
for quizNum in range(35):
    qfile=open('File No:%d.txt'%(quizNum+1),'w')
    qans=open('Answer Key No:%d.txt'%(quizNum+1),'w')

    qfile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    qfile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    qfile.write('\n\n')

    random.shuffle(states)
    for i in range(0,50):
        correctans=capitals[states[i]]
        answers.remove(correctans)
        wrongans=random.sample(answers,3)
        answers=answers+[correctans]
        ansoptions=wrongans+[correctans]
        random.shuffle(ansoptions)
        qfile.write('Q'+str(i+1)+') '+'What is the capital of '+states[i]+'?'+'\n')
        qans.write(str(i+1)+')'+capitals[states[i]]+'.\n')
        for i in range(4):
            qfile.write('\t'+str(i+1)+':'+ansoptions[i]+'.'+'\n')
            
        
    
