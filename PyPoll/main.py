import os

import csv

#initialize list to hold voter info from election_data.csv
voter_info = []
candidate_dic = {}

csvpath = os.path.join('Resources','election_data.csv')

#initialize counter for total number of votes(records) in election_data.csv file
total_Votes = 0

#define lists to be populated by csvfile without the header

with open(csvpath, newline = '') as csvfile:
    csvreader=csv.reader(csvfile, delimiter = ',')
    
     # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")
    
    total = 0
    for row in csvreader:
        total_Votes += 1
        voter_info.append(row[2])
    
    khan_Votes = 0
    correy_Votes = 0
    li_Votes = 0
    otooley_Votes = 0
    
    
    #tally up total votes for each candidate
    for row in voter_info:
        if row == 'Khan':
            khan_Votes += 1
        elif row == 'Correy':
            correy_Votes += 1
        elif row == 'Li':
            li_Votes += 1
        elif row == "O'Tooley":
            otooley_Votes += 1
        ##else:
            ##other += 1
            #add this candidate to the  candidate_dict dictionary
            ##print(row)
    
    candidate_dic = {'Kahn':khan_Votes,'Correy':correy_Votes,'Li':li_Votes,"O'Tooley":otooley_Votes}
    ##print(candidate_dic)
             
            
    #create a dictionary called candidates_list of key values (unique candidates)        
    #for row in voter_info:
        #if row is not one of the keys already in candidates_list then add it as a key value 
        #else find the matching key and add 1 to its value of total_votes
        ##'key1' = 
        
      
    #Calculate percentage of total votes for each candidate
    khan_percentage = round(float((khan_Votes/total_Votes)*100),5)
    correy_percentage = round(float((correy_Votes/total_Votes)*100),4)
    li_percentage = round(float((li_Votes/total_Votes)*100),4)
    otooley_percentage = round(float((otooley_Votes/total_Votes)*100),5)
    
    
    text_file = open('hw_3_Polloutput.txt', 'w')
    text_file.write("-----------------------------------------------------------------")
    text_file.write("'\n'")
    text_file.write("Election Results")
    text_file.write("'\n'")
    text_file.write("-----------------------------------------------------------------")
    text_file.write("'\n'")
    text_file.write("Total Votes: "+ str(total_Votes))  
    text_file.write("'\n'")
    text_file.write("-----------------------------------------------------------------")
    text_file.write("'\n'")
    text_file.write("'\n'")
    text_file.write("Kahn    " +str(khan_percentage) + "%   "+str(khan_Votes))
    text_file.write("'\n'")
    text_file.write("Correy  "+str(correy_percentage) + "%  "+str(correy_Votes))
    text_file.write("'\n'")
    text_file.write("Li      "+ str(li_percentage) + "%  " +str(li_Votes))
    text_file.write("'\n'")
    text_file.write("O'Tooley  "+ str(otooley_percentage) + "%  "+ str(otooley_Votes))
    text_file.write("'\n'")
    text_file.write("-----------------------------------------------------------------")
    text_file.write("'\n'")
    text_file.write("Winner: Khan Congratulations!")
    text_file.write("'\n'")
    text_file.write("-----------------------------------------------------------------")
    text_file.close()
    


           

        
print("Election Results")
print("---------------------------------------------------------------------")
print("Total Votes: ", total_Votes)
print("---------------------------------------------------------------------")
print("Kahn:     ", str(khan_percentage) + " %  " + str(khan_Votes))        
print("Correy:   ", str(correy_percentage) + " % " + str(correy_Votes))
print("Li:       ", str(li_percentage) + " %  " + str(li_Votes))
print("O'Tooley: ", str(otooley_percentage) + " %    " + str(otooley_Votes))
print("----------------------------------------------------------------------")
print("Winner : Khan Congratulations!!")
print("----------------------------------------------------------------------")