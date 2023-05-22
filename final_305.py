from musx import tools, Spectrum,  markov, markov_analyze, spectral
from musx.midi import gm
from musx import Score, Seq, MidiFile, Interval, Note, Pitch, rhythm, gens
import math, numpy, random
from musx.paint import brush, spray

def heal_or_express(condition):
    microdivs=2
    instruments = {
       0: gm.AcousticGrandPiano,
       1: gm.OrchestralHarp
        }
    track1 = Seq()
    score = Score(out=track1)
    instruments__ = MidiFile.metatrack(tempo = 80,timesig=[4,4], keysig=[0,0], ins=instruments, microdivs=microdivs)
    if condition == "physical" or condition == "emotional":
        spectrums = spectral.rmspectrum(174, 295, True)     
    elif condition == "self-expression":
        spectrums = spectral.rmspectrum(741, 963, True)
    else:       
        return NameError
    for i in range(40):
            yielded = random.randint(spectrums[0], spectrums[1])
            freq_to_keynum =  math.floor(math.log2((yielded/440.0)) * 12 + 69)
            
            first_pitch = Pitch.from_keynum(freq_to_keynum)     
            second_pitch = Pitch.from_keynum(freq_to_keynum + 3)     
            third_pitch = Pitch.from_keynum(freq_to_keynum + 6)
            fourth_pitch = Pitch.from_keynum(freq_to_keynum + 9)
            if i % 4 == 0:
                score.add(Note(i , 1/8, pitch= first_pitch, amplitude= .18, instrument= 1))
                score.add(Note(i+1/8 , 1/8, pitch= second_pitch, amplitude= .18, instrument= 1))
                score.add(Note(i + 1/4 , 1/8, pitch= third_pitch, amplitude= .18, instrument= 1))
                score.add(Note(i + 3/8, 1/8, pitch= fourth_pitch, amplitude= .18, instrument= 1))     
    for i in range(40):      
            yielded = random.randint(spectrums[0], spectrums[1])
            freq_to_keynum =  math.floor(math.log2((yielded/440.0)) * 12 + 69)
            pitched = Pitch.from_keynum(freq_to_keynum)
            score.add(Note(i, 1, pitch= pitched, amplitude= .3, instrument= 0))
    file = MidiFile("final.mid", [instruments__, track1, ]).write()
    file_2 = MidiFile("reflecting.mid", [instruments__, track1, ]).write()
    print(f"Wrote '{file.pathname}'.")
    
def no_preference():
    g = spectral.untemper(8)
    microdivs=2
    instruments = {
       0: gm.Trumpet,
       1: gm.ChurchOrgan,
       2: gm.Timpani
        }
    track1 = Seq()
    score = Score(out=track1)
    instruments__ = MidiFile.metatrack(tempo = 150,timesig=[4,4], keysig=[0,0], ins=instruments, microdivs=microdivs)
    rhys = [1/2, 1/2, 1/4, 1/8, 1/4, 1/2, 1/8, 1/8]
    interval_bank = [[Interval("M3"), Interval("m7")], [Interval("m3"), Interval("m7")], [Interval("+3"), Interval("M7")] ]
    randos = []
    for i in range(10):
        rando = (random.randint(60, 100))
        randos.append(rando)
    m_a = markov_analyze(randos, 1)
    mark = markov(m_a, stop= 200)
    time = 0
    for m in mark:
        int_choose = gens.choose(rhys, stop=1)
        i_ =  Pitch()
        for j in int_choose:
            i_ = j
        p_ = Pitch.from_keynum(m)  
        score.add(Note(time, i_, p_, .45, instrument= 0))
        time = time + i_
    c_notes = []
    for i in range(10):
        cnote = (random.randint(30, 65))
        c_notes.append(cnote)
    c_a = markov_analyze(randos, 1)
    cark = markov(m_a, stop= 60)
    time_church = 0
    for m in cark:
        int_choose = random.randint(0, 2)
        pair_ = interval_bank[int_choose]        
        p_ = Pitch.from_keynum(m)      
        score.add(Note(time_church, 1, p_, .5, instrument= 1))
        p_2 = pair_[0].transpose(p_)
        score.add(Note(time_church, 1, p_2, .5, instrument= 1))      
        p_3 = pair_[1].transpose(p_)
        score.add(Note(time_church, 1, p_3, .5, instrument= 1))
        time_church = time_church + 1   
    for i in range(180): 
        if i % 2 == 0:    
            score.add(Note(i * 1/3, 1/3, Pitch('C3'), amplitude=.6, instrument=2))
        else:
            score.add(Note(i * 1/3, 1/3, Pitch('G2'), amplitude=.6, instrument=2))
                 
    file = MidiFile("final.mid", [instruments__, track1, ]).write()
    file_2 = MidiFile("default.mid", [instruments__, track1, ]).write()
    print(f"Wrote '{file.pathname}'.")
    

def wake_up():
    microdivs=2
    instruments = {
        0: gm.Applause,
    1: gm.BirdTweet,
   2: gm.Seashore,
   3: gm.Helicopter,
   4: gm.OrchestralHarp,
   5: gm.TelephoneRing,
   6: gm.Vibraphone
        }
    track1 = Seq()
    score = Score(out=track1)
    instruments__ = MidiFile.metatrack(tempo = 30,timesig=[4,4], keysig=[0,0], ins=instruments, microdivs=microdivs)
    thistuple = ((1,23),2)
    s = Spectrum([])
    s.add(440, .5)
    s.add(420, .2)
    s.add(420, .1)
    s.add(310, .4)
    s.add(349, .2)
    s.add(540, .3)
    for i in range(20):
        a_ = 0
        amplitude = tools.rescale(a_, -5, 5, s.minamp(), s.maxamp())
        frequency = random.randint(s.minfreq(), s.maxfreq())
        freq_to_keynum =  math.floor(math.log2((frequency/440.0)) * 12 + 69)
        pitched = Pitch.from_keynum(freq_to_keynum)
        score.add(Note(i, 1, amplitude= .3, instrument= 1))
        if i % 3 == 0:
            score.add(Note(i, 3, amplitude= amplitude,pitch=Interval("P8").transpose(pitched), instrument= 6))
            score.add(Note(i, 3, amplitude= amplitude,pitch=pitched, instrument= 4))
        if i % 4 == 0:
            score.add(Note(i, 1, amplitude=.12, instrument= 2))
        if i % 6 == 0:
            score.add(Note(i, 1, amplitude=.08, instrument= 3))
        if i == 18:
            score.add(Note(i, 2, amplitude=1, instrument= 5))   
        if i == 19:
            score.add(Note(i, 1, amplitude=1, instrument= 0))
    file = MidiFile("final.mid", [instruments__, track1, ]).write()
    file_2 = MidiFile("alarm_clock.mid", [instruments__, track1, ]).write()
    print(f"Wrote '{file.pathname}'.")
    


def time_to_sleep():
    microdivs=2
    instruments = {
    1: gm.Cello,
    3: gm.Agogo,
    2: gm.Woodblock
        }
    track1 = Seq()
    score = Score(out=track1)
    instruments__ = MidiFile.metatrack(tempo = 50,timesig=[6,8], keysig=[0,0], ins=instruments, microdivs=microdivs)
    choir_cycle = [ Pitch("F#3"), Pitch("D3"),Pitch("E3"), Pitch("A2"),  Pitch("F#3"), Pitch("D3"),Pitch("E3"),Pitch("A3")]
    dynamic_tracker = 0
    d_c = 1/150
    for i in range(15):    
        score.add(Note(i, 1, choir_cycle[i % 8], .19-i*d_c, 1))
        dynamic_tracker = dynamic_tracker + 1
        
    for i in range(15): 
        score.add(Note(15+i, 1, Interval('-P4').transpose(choir_cycle[i % 8]), .19 -i*d_c, 1))
        dynamic_tracker = dynamic_tracker + 1
    for i in range(15): 
        score.add(Note(30+i, 1, Interval('m3').transpose(choir_cycle[i % 8]), .19 -i* d_c, 1))
        dynamic_tracker = dynamic_tracker + 1
    for i in range(15):
        score.add(Note(45+i, 1, Interval('A2').transpose(choir_cycle[i % 8]), .19 -i*d_c, 1))
        dynamic_tracker = dynamic_tracker + 1
    for i in range(180): 
        if (i) % 3== 0:  
            score.add(Note( i*.33, .33, amplitude=.1, instrument=3))
        else:
            score.add(Note( i*.33, .33, amplitude=.1, instrument=2))
    file = MidiFile("final.mid", [instruments__, track1, ]).write()
    file_2 = MidiFile("lullaby.mid", [instruments__, track1, ]).write()
    print(f"Wrote '{file.pathname}'.")
 
  
class Patient:
    def __init__(self, condition):
        self._condition = condition
    def __str__(self):
       return 'Patient Condition: ' + str(self._condition) 
  

def music_mapper(patient):
    diagnoser = {
        "physical" : "recupertate",
        "emotional" : "recupertate",
        "self-expression" : "recupertate",
        "" : "",
        "tired" : "need_to_sleep",
        "sleeping" : "need_to_wake_up"
    }   
    if type(patient) != Patient:
        return TypeError
    condition_ = patient._condition
    diagnosis = diagnoser[condition_]
    if diagnosis == "recupertate":
        heal_or_express(patient._condition)
    elif diagnosis == "need_to_sleep":
        time_to_sleep()
    elif diagnosis == "need_to_wake_up":
        wake_up()
    elif diagnosis== "":
        no_preference()
    else:
        return KeyError
      
      
#pat = Patient("tired")  


#pat = Patient("sleeping")



#pat = Patient("physical")
#pat = Patient("emotional")




pat = Patient("self-expression")



#pat = Patient("")

music_mapper(pat)    
        
    
        
    

        




# heal_or_express("self-expression")
#no_preference()
#wake_up()
#time_to_sleep()