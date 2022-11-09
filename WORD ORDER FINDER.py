#It may take 10-20 minutes for the program to run, since I don't use any methods and write all of them myself.                 
def Word_Order_Frequency_One_Book(book1,number,result1):
    #It is a list of words to be removed from each book we choose.
    words_list = ["able", "about", "above", "abroad", "according", "accordingly", "across", "actually", "adj", "after",
              "afterwards", "again", "against", "ago", "ahead", "ain't", "all", "allow", "allows", "almost", "alone",
              "along", "alongside", "already", "also", "although", "always", "am", "amid", "amidst", "among", "amongst",
              "an", "and", "another", "any", "anybody", "anyhow", "anyone", "anything", "anyway", "anyways", "anywhere",
              "apart", "appear", "appreciate", "appropriate", "are", "aren't", "around", "as", "a's", "aside", "ask",
              "asking", "associated", "at", "available", "away", "awfully", "back", "backward", "backwards", "be",
              "became", "because", "become", "becomes", "becoming", "been", "before", "beforehand", "begin", "behind",
              "being", "believe", "below", "beside", "besides", "best", "better", "between", "beyond", "both", "brief",
              "but", "by", "came", "can", "cannot", "cant", "can't", "caption", "cause", "causes", "certain",
              "certainly", "changes", "clearly", "c'mon", "co", "co.", "com", "come", "comes", "concerning",
              "consequently", "consider", "considering", "contain", "containing", "contains", "corresponding", "could",
              "couldn't", "course", "c's", "currently", "dare", "daren't", "definitely", "described", "despite", "did",
              "didn't", "different", "directly", "do", "does", "doesn't", "doing", "done", "don't", "down", "downwards",
              "during", "each", "edu", "eg", "eight", "eighty", "either", "else", "elsewhere", "end", "ending",
              "enough", "entirely", "especially", "et", "etc", "even", "ever", "evermore", "every", "everybody",
              "everyone", "everything", "everywhere", "ex", "exactly", "example", "except", "fairly", "far", "farther",
              "few", "fewer", "fifth", "first", "five", "followed", "following", "follows", "for", "forever", "former",
              "formerly", "forth", "forward", "found", "four", "from", "further", "furthermore", "get", "gets",
              "getting", "given", "gives", "go", "goes", "going", "gone", "got", "gotten", "greetings", "had", "hadn't",
              "half", "happens", "hardly", "has", "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "hello",
              "help", "hence", "her", "here", "hereafter", "hereby", "herein", "here's", "hereupon", "hers", "herself",
              "he's", "hi", "him", "himself", "his", "hither", "hopefully", "how", "howbeit", "however", "hundred",
              "i'd", "ie", "if", "ignored", "i'll", "i'm", "immediate", "in", "inasmuch", "inc", "inc.", "indeed",
              "indicate", "indicated", "indicates", "inner", "inside", "insofar", "instead", "into", "inward", "is",
              "isn't", "it", "it'd", "it'll", "its", "it's", "itself", "i've", "just", "k", "keep", "keeps", "kept",
              "know", "known", "knows", "last", "lately", "later", "latter", "latterly", "least", "less", "lest", "let",
              "let's", "like", "liked", "likely", "likewise", "little", "look", "looking", "looks", "low", "lower",
              "ltd", "made", "mainly", "make", "makes", "many", "may", "maybe", "mayn't", "me", "mean", "meantime",
              "meanwhile", "merely", "might", "mightn't", "mine", "minus", "miss", "more", "moreover", "most", "mostly",
              "mr", "mrs", "much", "must", "mustn't", "my", "myself", "name", "namely", "nd", "near", "nearly",
              "necessary", "need", "needn't", "needs", "neither", "never", "neverf", "neverless", "nevertheless", "new",
              "next", "nine", "ninety", "no", "nobody", "non", "none", "nonetheless", "noone", "no-one", "nor",
              "normally", "not", "nothing", "notwithstanding", "novel", "now", "nowhere", "obviously", "of", "off",
              "often", "oh", "ok", "okay", "old", "on", "once", "one", "ones", "one's", "only", "onto", "opposite",
              "or", "other", "others", "otherwise", "ought", "oughtn't", "our", "ours", "ourselves", "out", "outside",
              "over", "overall", "own", "particular", "particularly", "past", "per", "perhaps", "placed", "please",
              "plus", "possible", "presumably", "probably", "provided", "provides", "que", "quite", "qv", "rather",
              "rd", "re", "really", "reasonably", "recent", "recently", "regarding", "regardless", "regards",
              "relatively", "respectively", "right", "round", "said", "same", "saw", "say", "saying", "says", "second",
              "secondly", "see", "seeing", "seem", "seemed", "seeming", "seems", "seen", "self", "selves", "sensible",
              "sent", "serious", "seriously", "seven", "several", "shall", "shan't", "she", "she'd", "she'll", "she's",
              "should", "shouldn't", "since", "six", "so", "some", "somebody", "someday", "somehow", "someone",
              "something", "sometime", "sometimes", "somewhat", "somewhere", "soon", "sorry", "specified", "specify",
              "specifying", "still", "sub", "such", "sup", "sure", "take", "taken", "taking", "tell", "tends", "th",
              "than", "thank", "thanks", "thanx", "that", "that'll", "thats", "that's", "that've", "the", "their",
              "theirs", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "there'd",
              "therefore", "therein", "there'll", "there're", "theres", "there's", "thereupon", "there've", "these",
              "they", "they'd", "they'll", "they're", "they've", "thing", "things", "think", "third", "thirty", "this",
              "thorough", "thoroughly", "those", "though", "three", "through", "throughout", "thru", "thus", "till",
              "to", "together", "too", "took", "toward", "towards", "tried", "tries", "truly", "try", "trying", "t's",
              "twice", "two", "un", "under", "underneath", "undoing", "unfortunately,""unless", "unlike", "unlikely",
              "until", "unto", "up", "upon", "upwards", "us", "use", "used", "useful", "uses", "using", "usually", "v",
              "value", "various", "versus", "very", "via", "viz", "vs", "want", "wants", "was", "wasn't", "way", "we",
              "we'd", "welcome", "well", "we'll", "went", "were", "we're", "weren't", "we've", "what", "whatever",
              "what'll", "what's", "what've", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby",
              "wherein", "where's", "whereupon", "wherever", "whether", "which", "whichever", "while", "whilst",
              "whither", "who", "who'd", "whoever", "whole", "who'll", "whom", "whomever", "who's", "whose", "why",
              "will", "willing", "wish", "with", "within", "without", "wonder", "won't", "would", "wouldn't", "yes",
              "yet", "you", "you'd", "you'll", "your", "you're", "yours", "yourself", "yourselves", "you've", "zero",
              "a", "how's", "i", "when's", "why's", "b", "c", "d", "e", "f", "g", "h", "j", "l", "m", "n", "o", "p",
              "q", "r", "s", "t", "u", "uucp", "w", "x", "y", "z", "I", "www", "amount", "bill", "bottom", "call",
              "computer", "con", "couldnt", "cry", "de", "describe", "detail", "due", "eleven", "empty", "fifteen",
              "fifty", "fill", "find", "fire", "forty", "front", "full", "give", "hasnt", "herse", "himse", "interest",
              "itse”", "mill", "move", "myse”", "part", "put", "show", "side", "sincere", "sixty", "system", "ten",
              "thick", "thin", "top", "twelve", "twenty", "abst", "accordance", "act", "added", "adopted", "affected",
              "affecting", "affects", "ah", "announce", "anymore", "apparently", "approximately", "aren", "arent",
              "arise", "auth", "beginning", "beginnings", "begins", "biol", "briefly", "ca", "date", "ed", "effect",
              "et-al", "ff", "fix", "gave", "giving", "heres", "hes", "hid", "home", "id", "im", "immediately",
              "importance", "important", "index", "information", "invention", "itd", "keys", "kg", "km", "largely",
              "lets", "line", "'ll", "means", "mg", "million", "ml", "mug", "na", "nay", "necessarily", "nos", "noted",
              "obtain", "obtained", "omitted", "ord", "owing", "page", "pages", "poorly", "possibly", "potentially",
              "pp", "predominantly", "present", "previously", "primarily", "promptly", "proud", "quickly", "ran",
              "readily", "ref", "refs", "related", "research", "resulted", "resulting", "results", "run", "sec",
              "section", "shed", "shes", "showed", "shown", "showns", "shows", "significant", "significantly",
              "similar", "similarly", "slightly", "somethan", "specifically", "state", "states", "stop", "strongly",
              "substantially", "successfully", "sufficiently", "suggest", "thered", "thereof", "therere", "thereto",
              "theyd", "theyre", "thou", "thoughh", "thousand", "throug", "til", "tip", "ts", "ups", "usefully",
              "usefulness", "'ve", "vol", "vols", "wed", "whats", "wheres", "whim", "whod", "whos", "widely", "words",
              "world", "youd", "youre"]
    if number == 1:
        with open(book1,encoding="UTF-8") as file_read:    
            content = file_read.read()
            encoded_string = content.encode("ascii", "ignore")
            decode_string = encoded_string.decode()
            #It is a list of punctuation marks to be removed from the book.
            chars = [',','.','?','-',';','-','"','!',':','(',')','[',']','*','_','0','1','2','3','4','5','6','7','8','9','/','#','$','%','&','<','=','>','@','^','€','...']
            #Removes punctuation marks from the book.
            for c in chars:
                decode_string = decode_string.replace(c,'')           
            decode_string = decode_string.lower()
            decode_string = decode_string.replace('\n',' ')            
            decode_string = decode_string.replace('   ','  ')
            decode_string = decode_string.replace('  ',' ')                
            listt = list(decode_string.split(' '))
            while '' in listt:                                
                listt.remove('')              
            #Removes words to be removed from the book.
            for indekss in listt[:]:                                   
                for indeks in words_list[:]:
                    if indekss == indeks:
                        listt.remove(indekss)
                        break
                                         
        with open (result1,'w') as yazilacak_dosya: 
            writing_dict = {}
            #Finds how many of a word are in the book and throws it into a dictionary.
            for element1 in listt[:]:
                count = 0
                for element2 in listt[:]:
                    if element1 == element2:
                        count = count+1
                        writing_dict[element1] = count                      
                while element1 in listt:
                    listt.remove(element1)
            #Sorts the dictionary from largest to smallest.
            sorted_writing_dict = {k: v for k, v in sorted(writing_dict.items(), key=lambda item: item[1],reverse=True)}
            count3=0
            #It prints the data to the text file entered while importing.
            for key in sorted_writing_dict.keys():                
                yazilacak_dosya.write(str(writing_dict[key]))
                yazilacak_dosya.write("||")
                yazilacak_dosya.write(key)
                yazilacak_dosya.write("\n")
                count3+=1
                if count3==100:
                    break
                                                                                                              
    elif number ==2:
         with open(book1,encoding="UTF-8") as file_read:             
             content = file_read.read()
             encoded_string = content.encode("ascii", "ignore")
             decode_string = encoded_string.decode()
             #It is a list of punctuation marks to be removed from the book.
             chars = [',','.','?','-',';','-','"','!',':','(',')','[',']','*','_','0','1','2','3','4','5','6','7','8','9','/','#','$','%','&','<','=','>','@','^','€','...']
             #Removes punctuation marks from the book.
             for c in chars:                                  
                 decode_string = decode_string.replace(c,'')           
             decode_string = decode_string.lower()
             decode_string = decode_string.replace('\n',' ')            
             decode_string = decode_string.replace('   ','  ')
             decode_string = decode_string.replace('  ',' ')
             listt = list(decode_string.split(' '))
             while '' in listt:
                 listt.remove('')
             list1 = []
             #Removes words to be removed from the book.
             for indekss in listt[:]:                   
                 for indeks in words_list[:]:
                     if indekss == indeks:
                         listt.remove(indekss)
                         break
             #Sorts the words in the book in pairs and assigns each pair to a new list.                 
             for i in range(len(listt)):                 
                 if i>=1:                     
                     list1.append(listt[i-1]+" "+listt[i])                    
                
         with open (result1,'w') as yazilacak_dosya:             
             writing_dict = {}
             #Finds how many of a word are in the book in pairs and throws it into a dictionary.
             for element1 in list1[:]:                                                      
                 count = 0
                 for element2 in list1[:]:                     
                     if element1 == element2:                         
                         count = count+1
                         writing_dict[element1] = count
                 while element1 in list1:                     
                    list1.remove(element1)
             #Sorts the dictionary from largest to smallest                      
             sorted_writing_dict = {k: v for k, v in sorted(writing_dict.items(), key=lambda item: item[1],reverse=True)}
             count3=0
             #It prints the data to the text file entered while importing.
             for key in sorted_writing_dict.keys():                
                yazilacak_dosya.write(str(writing_dict[key]))
                yazilacak_dosya.write("||")
                yazilacak_dosya.write(key)
                yazilacak_dosya.write("\n")
                count3+=1
                if count3==100:
                    break
    else:
        print("The number has to be 1 or 2. Please import again.")            
def Word_Order_Frequency_Two_Books(book1,book2,number,result1):
    #It is a list of words to be removed from each book we choose.
    words_list = ["able", "about", "above", "abroad", "according", "accordingly", "across", "actually", "adj", "after",
              "afterwards", "again", "against", "ago", "ahead", "ain't", "all", "allow", "allows", "almost", "alone",
              "along", "alongside", "already", "also", "although", "always", "am", "amid", "amidst", "among", "amongst",
              "an", "and", "another", "any", "anybody", "anyhow", "anyone", "anything", "anyway", "anyways", "anywhere",
              "apart", "appear", "appreciate", "appropriate", "are", "aren't", "around", "as", "a's", "aside", "ask",
              "asking", "associated", "at", "available", "away", "awfully", "back", "backward", "backwards", "be",
              "became", "because", "become", "becomes", "becoming", "been", "before", "beforehand", "begin", "behind",
              "being", "believe", "below", "beside", "besides", "best", "better", "between", "beyond", "both", "brief",
              "but", "by", "came", "can", "cannot", "cant", "can't", "caption", "cause", "causes", "certain",
              "certainly", "changes", "clearly", "c'mon", "co", "co.", "com", "come", "comes", "concerning",
              "consequently", "consider", "considering", "contain", "containing", "contains", "corresponding", "could",
              "couldn't", "course", "c's", "currently", "dare", "daren't", "definitely", "described", "despite", "did",
              "didn't", "different", "directly", "do", "does", "doesn't", "doing", "done", "don't", "down", "downwards",
              "during", "each", "edu", "eg", "eight", "eighty", "either", "else", "elsewhere", "end", "ending",
              "enough", "entirely", "especially", "et", "etc", "even", "ever", "evermore", "every", "everybody",
              "everyone", "everything", "everywhere", "ex", "exactly", "example", "except", "fairly", "far", "farther",
              "few", "fewer", "fifth", "first", "five", "followed", "following", "follows", "for", "forever", "former",
              "formerly", "forth", "forward", "found", "four", "from", "further", "furthermore", "get", "gets",
              "getting", "given", "gives", "go", "goes", "going", "gone", "got", "gotten", "greetings", "had", "hadn't",
              "half", "happens", "hardly", "has", "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "hello",
              "help", "hence", "her", "here", "hereafter", "hereby", "herein", "here's", "hereupon", "hers", "herself",
              "he's", "hi", "him", "himself", "his", "hither", "hopefully", "how", "howbeit", "however", "hundred",
              "i'd", "ie", "if", "ignored", "i'll", "i'm", "immediate", "in", "inasmuch", "inc", "inc.", "indeed",
              "indicate", "indicated", "indicates", "inner", "inside", "insofar", "instead", "into", "inward", "is",
              "isn't", "it", "it'd", "it'll", "its", "it's", "itself", "i've", "just", "k", "keep", "keeps", "kept",
              "know", "known", "knows", "last", "lately", "later", "latter", "latterly", "least", "less", "lest", "let",
              "let's", "like", "liked", "likely", "likewise", "little", "look", "looking", "looks", "low", "lower",
              "ltd", "made", "mainly", "make", "makes", "many", "may", "maybe", "mayn't", "me", "mean", "meantime",
              "meanwhile", "merely", "might", "mightn't", "mine", "minus", "miss", "more", "moreover", "most", "mostly",
              "mr", "mrs", "much", "must", "mustn't", "my", "myself", "name", "namely", "nd", "near", "nearly",
              "necessary", "need", "needn't", "needs", "neither", "never", "neverf", "neverless", "nevertheless", "new",
              "next", "nine", "ninety", "no", "nobody", "non", "none", "nonetheless", "noone", "no-one", "nor",
              "normally", "not", "nothing", "notwithstanding", "novel", "now", "nowhere", "obviously", "of", "off",
              "often", "oh", "ok", "okay", "old", "on", "once", "one", "ones", "one's", "only", "onto", "opposite",
              "or", "other", "others", "otherwise", "ought", "oughtn't", "our", "ours", "ourselves", "out", "outside",
              "over", "overall", "own", "particular", "particularly", "past", "per", "perhaps", "placed", "please",
              "plus", "possible", "presumably", "probably", "provided", "provides", "que", "quite", "qv", "rather",
              "rd", "re", "really", "reasonably", "recent", "recently", "regarding", "regardless", "regards",
              "relatively", "respectively", "right", "round", "said", "same", "saw", "say", "saying", "says", "second",
              "secondly", "see", "seeing", "seem", "seemed", "seeming", "seems", "seen", "self", "selves", "sensible",
              "sent", "serious", "seriously", "seven", "several", "shall", "shan't", "she", "she'd", "she'll", "she's",
              "should", "shouldn't", "since", "six", "so", "some", "somebody", "someday", "somehow", "someone",
              "something", "sometime", "sometimes", "somewhat", "somewhere", "soon", "sorry", "specified", "specify",
              "specifying", "still", "sub", "such", "sup", "sure", "take", "taken", "taking", "tell", "tends", "th",
              "than", "thank", "thanks", "thanx", "that", "that'll", "thats", "that's", "that've", "the", "their",
              "theirs", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "there'd",
              "therefore", "therein", "there'll", "there're", "theres", "there's", "thereupon", "there've", "these",
              "they", "they'd", "they'll", "they're", "they've", "thing", "things", "think", "third", "thirty", "this",
              "thorough", "thoroughly", "those", "though", "three", "through", "throughout", "thru", "thus", "till",
              "to", "together", "too", "took", "toward", "towards", "tried", "tries", "truly", "try", "trying", "t's",
              "twice", "two", "un", "under", "underneath", "undoing", "unfortunately,""unless", "unlike", "unlikely",
              "until", "unto", "up", "upon", "upwards", "us", "use", "used", "useful", "uses", "using", "usually", "v",
              "value", "various", "versus", "very", "via", "viz", "vs", "want", "wants", "was", "wasn't", "way", "we",
              "we'd", "welcome", "well", "we'll", "went", "were", "we're", "weren't", "we've", "what", "whatever",
              "what'll", "what's", "what've", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby",
              "wherein", "where's", "whereupon", "wherever", "whether", "which", "whichever", "while", "whilst",
              "whither", "who", "who'd", "whoever", "whole", "who'll", "whom", "whomever", "who's", "whose", "why",
              "will", "willing", "wish", "with", "within", "without", "wonder", "won't", "would", "wouldn't", "yes",
              "yet", "you", "you'd", "you'll", "your", "you're", "yours", "yourself", "yourselves", "you've", "zero",
              "a", "how's", "i", "when's", "why's", "b", "c", "d", "e", "f", "g", "h", "j", "l", "m", "n", "o", "p",
              "q", "r", "s", "t", "u", "uucp", "w", "x", "y", "z", "I", "www", "amount", "bill", "bottom", "call",
              "computer", "con", "couldnt", "cry", "de", "describe", "detail", "due", "eleven", "empty", "fifteen",
              "fifty", "fill", "find", "fire", "forty", "front", "full", "give", "hasnt", "herse", "himse", "interest",
              "itse”", "mill", "move", "myse”", "part", "put", "show", "side", "sincere", "sixty", "system", "ten",
              "thick", "thin", "top", "twelve", "twenty", "abst", "accordance", "act", "added", "adopted", "affected",
              "affecting", "affects", "ah", "announce", "anymore", "apparently", "approximately", "aren", "arent",
              "arise", "auth", "beginning", "beginnings", "begins", "biol", "briefly", "ca", "date", "ed", "effect",
              "et-al", "ff", "fix", "gave", "giving", "heres", "hes", "hid", "home", "id", "im", "immediately",
              "importance", "important", "index", "information", "invention", "itd", "keys", "kg", "km", "largely",
              "lets", "line", "'ll", "means", "mg", "million", "ml", "mug", "na", "nay", "necessarily", "nos", "noted",
              "obtain", "obtained", "omitted", "ord", "owing", "page", "pages", "poorly", "possibly", "potentially",
              "pp", "predominantly", "present", "previously", "primarily", "promptly", "proud", "quickly", "ran",
              "readily", "ref", "refs", "related", "research", "resulted", "resulting", "results", "run", "sec",
              "section", "shed", "shes", "showed", "shown", "showns", "shows", "significant", "significantly",
              "similar", "similarly", "slightly", "somethan", "specifically", "state", "states", "stop", "strongly",
              "substantially", "successfully", "sufficiently", "suggest", "thered", "thereof", "therere", "thereto",
              "theyd", "theyre", "thou", "thoughh", "thousand", "throug", "til", "tip", "ts", "ups", "usefully",
              "usefulness", "'ve", "vol", "vols", "wed", "whats", "wheres", "whim", "whod", "whos", "widely", "words",
              "world", "youd", "youre"]
    
    if number == 1:        
        with open(book1,encoding="UTF-8") as file_read_1:                                                
            content_1 = file_read_1.read()
            encoded_string = content_1.encode("ascii", "ignore")
            decode_string = encoded_string.decode()
            #It is a list of punctuation marks to be removed from the book1.
            chars = [',','.','?','-',';','-','"','!',':','(',')','[',']','*','_','0','1','2','3','4','5','6','7','8','9','/','#','$','%','&','<','=','>','@','^','€','...']
            #Removes punctuation marks from the book1.
            for c in chars:
                decode_string = decode_string.replace(c,'')           
            decode_string = decode_string.lower()
            decode_string = decode_string.replace('\n',' ')            
            decode_string = decode_string.replace('   ','  ')
            decode_string = decode_string.replace('  ',' ')                
            list_1 = list(decode_string.split(' '))
            while '' in list_1:                                
                list_1.remove('')
            #Removes words to be removed from the book1.    
            for indekss in list_1[:]:                                   
                for indeks in words_list[:]:
                    if indekss == indeks:
                        list_1.remove(indekss)
                        break
                
        with open(book2,encoding="UTF-8") as file_read_2:    
            content_2 = file_read_2.read()
            encoded_string = content_2.encode("ascii", "ignore")
            decode_string = encoded_string.decode()
            #It is a list of punctuation marks to be removed from the book2.
            chars = [',','.','?','-',';','-','"','!',':','(',')','[',']','*','_','0','1','2','3','4','5','6','7','8','9','/','#','$','%','&','<','=','>','@','^','€','...']
            #Removes punctuation marks from the book2.
            for c in chars:
                decode_string = decode_string.replace(c,'')           
            decode_string = decode_string.lower()
            decode_string = decode_string.replace('\n',' ')            
            decode_string = decode_string.replace('   ','  ')
            decode_string = decode_string.replace('  ',' ')                
            list_2 = list(decode_string.split(' '))
            while '' in list_2:                                
                list_2.remove('')
            #Removes words to be removed from the book2.    
            for indekss in list_2[:]:                   
                for indeks in words_list[:]:
                    if indekss == indeks:
                        list_2.remove(indekss)
                        break 
                   
        with open (result1,'w') as yazilacak_dosya:
            #Assigns words from two books to a list.
            list_3 = list_1+list_2
            writing_dict = {}
            #It finds how many of any words are in the list and assigns those words with their values ​​to a dictionary.
            for element1 in list_3[:]:
                count = 0
                for element2 in list_3[:]:
                    if element1 == element2:
                        count = count+1
                        writing_dict[element1] = count                      
                while element1 in list_3:
                    list_3.remove(element1)
            #Sorts the dictionary from largest to smallest.        
            sorted_writing_dict = {k: v for k, v in sorted(writing_dict.items(), key=lambda item: item[1],reverse=True)}
            count3=0
            #It prints the data to the text file entered while importing.
            for key in sorted_writing_dict.keys():                
                yazilacak_dosya.write(str(writing_dict[key]))
                yazilacak_dosya.write("||")
                count_1 = 0
                count_2 = 0
                for x in list_1[:]:                   
                    if key == x:
                        count_1 = count_1+1
                for  y in list_2[:]:
                    if key == y:
                        count_2 = count_2 +1                        
                yazilacak_dosya.write(str(count_1))
                yazilacak_dosya.write("||")
                yazilacak_dosya.write(str(count_2))
                yazilacak_dosya.write("||")
                yazilacak_dosya.write(key)
                yazilacak_dosya.write("\n")
                count3+=1
                if count3==100:
                    break 
                   
    elif number ==2:
        with open(book1,encoding="UTF-8") as file_read_1:                                                
            content_1 = file_read_1.read()
            encoded_string = content_1.encode("ascii", "ignore")
            decode_string = encoded_string.decode()
            #It is a list of punctuation marks to be removed from the book1.
            chars = [',','.','?','-',';','-','"','!',':','(',')','[',']','*','_','0','1','2','3','4','5','6','7','8','9','/','#','$','%','&','<','=','>','@','^','€','...']
            #Removes punctuation marks from the book1.
            for c in chars:
                decode_string = decode_string.replace(c,'')           
            decode_string = decode_string.lower()
            decode_string = decode_string.replace('\n',' ')            
            decode_string = decode_string.replace('   ','  ')
            decode_string = decode_string.replace('  ',' ')                
            list_1 = list(decode_string.split(' '))
            while '' in list_1:                                
                list_1.remove('')
            list1 = []
            #Removes words to be removed from the book1.
            for indekss in list_1[:]:                   
                for indeks in words_list[:]:
                    if indekss == indeks:
                        list_1.remove(indekss)
                        break
            #Sorts the words in the book1 in pairs and assigns each pair to a new list.
            for i in range(len(list_1)):
                if i>=1:                    
                    list1.append(list_1[i-1]+" "+list_1[i])    
                        
        with open(book2,encoding="UTF-8") as file_read_2:    
            content_2 = file_read_2.read()
            encoded_string = content_2.encode("ascii", "ignore")
            decode_string = encoded_string.decode()
            #It is a list of punctuation marks to be removed from the book2.
            chars = [',','.','?','-',';','-','"','!',':','(',')','[',']','*','_','0','1','2','3','4','5','6','7','8','9','/','#','$','%','&','<','=','>','@','^','€','...']
            #Removes punctuation marks from the book2.            
            for c in chars:
                decode_string = decode_string.replace(c,'')           
            decode_string = decode_string.lower()
            decode_string = decode_string.replace('\n',' ')            
            decode_string = decode_string.replace('   ','  ')
            decode_string = decode_string.replace('  ',' ')                
            list_2 = list(decode_string.split(' '))
            while '' in list_2:                                
                list_2.remove('')
            list2 = []    
            #Removes words to be removed from the book2.
            for indekss in list_2[:]:                   
                for indeks in words_list[:]:
                    if indekss == indeks:
                        list_2.remove(indekss)
                        break
            #Sorts the words in the book2 in pairs and assigns each pair to a new list.
            for i in range(len(list_2)):
                if i>=1:
                    list2.append(list_2[i-1]+" "+list_2[i])    
                        
        with open (result1,'w') as yazilacak_dosya:
            #Assigns the pairs from both books to a single list.
            list_3 = list1+list2
            writing_dict = {}
            #It finds how many of any words are in the list and assigns those words with their values ​​to a dictionary.
            for element1 in list_3[:]:
                count = 0
                for element2 in list_3[:]:
                    if element1 == element2:
                        count = count+1
                        writing_dict[element1] = count                      
                while element1 in list_3:
                    list_3.remove(element1)
            #Sorts the dictionary from largest to smallest.        
            sorted_writing_dict = {k: v for k, v in sorted(writing_dict.items(), key=lambda item: item[1],reverse=True)}
            count3=0
            #It prints the data to the text file entered while importing.
            for key in sorted_writing_dict.keys():                
                yazilacak_dosya.write(str(writing_dict[key]))
                yazilacak_dosya.write("||")
                count_1 = 0
                count_2 = 0
                for x in list1[:]:                   
                    if key == x:
                        count_1 = count_1+1
                for  y in list2[:]:
                    if key == y:
                        count_2 = count_2 +1                        
                yazilacak_dosya.write(str(count_1))
                yazilacak_dosya.write("||")
                yazilacak_dosya.write(str(count_2))
                yazilacak_dosya.write("||")
                yazilacak_dosya.write(key)
                yazilacak_dosya.write("\n")
                count3+=1
                if count3==100:
                    break                                    
    else:
        print("The number has to be 1 or 2. Please import again.")
               
