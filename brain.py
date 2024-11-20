from functions import *
def protocols():
    while True:
        file = open("queries.txt", "a")
        # logic 
        query = takecommand().lower()

        if query in ['what is the time', 'can you tell the time']:
            file.write(query+"\n")
            query.replace("what", "")
            strtime = datetime.datetime.now().strftime("%H:%M")
            print(strtime)
            speak(f"sir the time is {strtime}")    
                        
        elif query in ['what is the day today']:
            file.write(query+"\n")
            query.replace("what", "")
            strdate = datetime.datetime.now().strftime("%d-%m-%y %H")  
            print(strdate)     
            speak(f"Sir today is{strdate}")
            
        elif 'who made you' in query:
            file.write(query+"\n")
            speak("Team HAZEL made me ") 

        elif 'who are you' in query or 'what is your name' in query:   
            file.write(query+"\n")        
            speak("I Am VAYU Your Virtual Assistant")
        
        elif 'hey' in query or 'hi' in query or 'hello' in query or 'whats up' in query:
            file.write(query+"\n")
            speak("Hi sir!")
            
            
        elif 'where do you live' in query:
            file.write(query+"\n")
            speak("I am a machine, leaving in machine.")  

        elif query in ['can i change your name', 'i liked to change your name']:  
            file.write(query+"\n")     
            speak("sorry sir but I like my name")
            
        elif 'awesome' in query or 'wow' in query or 'amazing' in query or 'wonderful' in query:        
            file.write(query+"\n")
            speak("Thanks for praising me.")
            
        elif 'do you know alexa' in query or 'is alexa is your friend' in query:  
            file.write(query+"\n")        
            speak("Alexa and I are best friend")
            
        elif 'how are you' in query or 'are you ok' in query or 'need any help' in query:    
            file.write(query+"\n")        
            speak("I am ok, what about you")
            
        elif 'I am ok' in query or 'I am good' in query or 'I am fine' in query:      
            file.write(query+"\n")     
            speak("Well, that is good to hear.")     

        # elif 'show my picture' in query:      
        #     file.write(query+"\n")    
        #     webcam()
            

        elif 'see you VAYU' in query or 'VAYU quit' in query or 'quit' in query or 'bye' in query:          
            file.write(query+"\n")
            speak("OK sir, going to sleep.")
            quit()

        # takecommand and deep learning
        
        elif 'search' in query:
            speak("What do you want to search for?")
            search = takecommand()
            url = 'http://www.google.com/search?&q=' + search
            webbrowser.get().open(url)
            speak("Here it is what I found on google")
            

        elif 'play video' in query or 'channel' in query:   
            file.write(query+"\n")      
            speak("Which type of video or channel?")
            search = takecommand()
            url = 'http://www.youtube.com/search?&q=' + search
            webbrowser.get().open(url)
            speak("This is it!!!")
            
            

        elif query in ['tell the temperature', 'weather']:   
            file.write(query+"\n")         
            speak("Sure sir, but of which city?")
            city = takecommand()
            weather(city)
            
            

        elif 'search for' in query:
            
            try:
                file.write(query+"\n")
                query.replace("search", "")
                query.replace("for", "")
                speak("Searching in data.")
                session = requests.Session()
                retry = Retry(connect=3, backoff_factor=0.5)
                adapter = HTTPAdapter(max_retries=retry)
                url = "https://www.wikipedia.org"
                session.mount('http://www.wikipedia.org', adapter)
                session.mount('https://www.wikipedia.org', adapter)
                session.get(url)
                results = wikipedia.summary(query, sentences=2)
                speak("I got it.")
                print(results, "\n")
                speak(results)

            except Exception as e:
                speak("Sorry, nothing found in data like this")
            

        # elif 'download song' in query:
        #     file.write(query+"\n")
        #     speak("Can you tell the song please?")
        #     s1 = takecommand()
        #     u1 = 'mp3quack.com/search?q=' + s1
        #     webbrowser.open(u1)
        #     speak("i think this is it")
            
            

        elif 'tell me some jokes' in query or 'jokes' in query or 'tell me a joke' in query:
            file.write(query+"\n")
            speak("Sure sir")
            jokes = pyjokes.get_joke(language='en', category='neutral')
            print(jokes)
            speak(jokes) 
            
            
       
        # commands

        elif 'open google' in query:
            file.write(query+"\n")
            speak("Of course sir")
            webbrowser.open('http://google.com')
            
            

        elif 'open wikipedia' in query:
            file.write(query+"\n")
            webbrowser.open("http://wikipedia.com") 
            
               

        elif 'open new tab' in query:
            file.write(query+"\n")
            speak("yes sir")
            webbrowser.open_new_tab('http://google.com')
            
            

        elif 'headlines' in query or 'news' in query or 'headline' in query:
            file.write(query + "\n")
            speak("Sure sir.")  # Consider making this non-blocking if needed
            givenews()
            
            

        elif 'screenshot' in query:
            file.write(query+"\n")
            speak("Ready!!!")
            speak("Five")
            speak("Four")
            speak("Three")
            speak("Two")
            speak("One")
            img = pyautogui.screenshot() 
            img.save("Screenshot.jpg")
            speak("Screenshot taken")  
                 

        elif 'wait a minute' in query or 'wait a minute please' in query: 
            file.write(query+"\n")
            speak("Ok sir , meet you after 1 minute.")
            time.sleep(60)
            speak("I am back sir ,can we start now.")  
            
        
        elif 'play a song' in query or 'play song' in query:
            file.write(query+"\n")
            speak("which song do you want to play?")
            song = takecommand()
            u10 = webbrowser.open_new_tab(f"https://open.spotify.com/search/{song.replace(' ', '%20')}")

            

        # hotstar    

        elif 'open hotstar' in query:
            file.write(query+"\n")
            speak("sure sir")
            webbrowser.open_new_tab('http://hotstar.com/in')
            

        elif 'open marvel movies' in query:
            file.write(query+"\n")
            speak("sure sir")
            webbrowser.open_new_tab('https://www.hotstar.com/in/channels/marvel')   
                     

        elif 'play latest episode ' in query or 'anupama' in query:
            file.write(query+"\n")
            speak("of course sir")
            webbrowser.open_new_tab("https://www.hotstar.com/in/tv/anupamaa/1260022017")
            

        # prime video
        elif 'open prime' in query:  
            file.write(query+"\n")          
            speak("sure sir")
            webbrowser.open_new_tab('https://primevideo.com')  
             

        # differents            

        # elif "open Flipkart" in query:
        #     webbrowser.open("www.flipkart.com")  
              

        elif 'open WhatsaApp' in query:  
            file.write(query+"\n")          
            speak("sure sir")
            webbrowser.open_new_tab("https://web.whatsapp.com/")    
                     

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open github" in query:
            webbrowser.open("https://github.com/")
        elif "open stack overflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "open keep" in query:
            webbrowser.open("https://keep.google.com/u/0/")

        
        
        else:
            file.write(query+"\n")
       

        
            

